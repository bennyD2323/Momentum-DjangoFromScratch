from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CodeSnippet
from .models import Tag
from .forms import CodeSnippetForm

# Create your views here.


def homepage(request):
    # if request.user.is_authenticated:
        # return redirect(to=display_snippet)

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
            return redirect(to="display_a_snippet", snippet_pk=snippet.pk)
    else:
        form=CodeSnippetForm(instance=snippet)

    return render(request, "snippets/edit_snippet.html", {"form":form, "snippet":snippet})

@login_required
def delete_snippet(request, snippet_pk):
    snippet= get_object_or_404(request.user.snippets, pk=snippet_pk)
    
    if request.method == "POST":
        snippet.delete()
        return redirect(to='display_snippets')
    return render(request, 'snippets/delete_snippet.html', {"snippet":snippet})
        
