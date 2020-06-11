from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CodeSnippet, Tag
from .forms import CodeSnippetForm

from django.db.models import Q
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect(to=display_snippets)
    return render(request, 'snippets/home.html')

@login_required
def display_snippets(request):
    your_snippets = request.user.snippets.all()
    return render(request, 'snippets/display_snippets.html',
                    {"snippets": your_snippets})

@login_required
def display_a_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)
    return render(request, "snippets/display_a_snippet.html", {'snippet': snippet})
    
@login_required
def add_snippet(request):
    if request.method == "POST":
        form = CodeSnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='display_a_snippet', snippet_pk=snippet.pk)
    else:
        form = CodeSnippetForm()
    return render(request, 'snippets/add_snippet.html', {"form": form})

@login_required
def edit_snippet(request, snippet_pk):
    snippet= get_object_or_404(request.user.snippets, pk=snippet_pk)

    if request.method == "POST":
        form = CodeSnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet=form.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to="display_a_snippet", snippet_pk=snippet.pk)
    else:
        form = CodeSnippetForm(instance=snippet, initial={"tag_names": snippet.get_tag_names()})

    return render(request, "snippets/edit_snippet.html", {"form":form, "snippet":snippet})

@login_required
def delete_snippet(request, snippet_pk):
    snippet= get_object_or_404(request.user.snippets, pk=snippet_pk)
    
    if request.method == "POST":
        snippet.delete()
        return redirect(to='display_snippets')
    return render(request, 'snippets/delete_snippet.html', {"snippet":snippet})
        
@login_required
def show_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    snippets = tag.snippets.filter(user=request.user)
    return render(request, "snippets/show_tag.html", {"tag":tag, "snippets":snippets})

@login_required
def other_snippet(request, snippet_pk):
    snippet= get_object_or_404(CodeSnippet, pk=snippet_pk)
    return render(request, "snippets/other_snippet.html", {"snippet": snippet})

@login_required
def search(request):
    person_id = request.user.id
    query = request.GET.get("q")
    if query is not None:
        # snippets = search_snippets_for_user(request.user, query)
        snippets = CodeSnippet.objects.filter(Q(title__icontains=query) | Q(tags__tag__icontains=query)).distinct()
    else:
        snippets = None
    
    return render(request, "snippets/search.html", {"snippets":snippets, "person_id": person_id, "query":query})


# @login_required
# def other_user(request):
    # users_snippets = CodeSnippet.
#     return render(request, "snippets.other_user.html",{})



# @login_required
#     def copy_recipe(request, snippet_pk):
#         original_snippet = get_object_or_404(Snippet, pk=recipe_pk)
#         cloned_snippet = Snippet(
#             title=original_recipe.title
#         )