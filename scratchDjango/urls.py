"""scratchDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as snippets_views


urlpatterns = [
    path('', snippets_views.homepage, name="homepage"),
    path('snippets', snippets_views.display_snippets, name="display_snippets"),
    path('snippets/<int:snippet_pk>/edit_snippet', snippets_views.edit_snippet, name="edit_snippet"),
    path('snippets/<int:snippet_pk>/delete_snippet', snippets_views.delete_snippet, name="delete_snippet"),
    path('snippets/<int:snippet_pk>/display_a_snippet', snippets_views.display_a_snippet, name="display_a_snippet"),
    path('snippets/<str:tag_name>/', snippets_views.show_tag, name='show_tag'),
    path('snippets/add_snippet', snippets_views.add_snippet, name="add_snippet"),
    path('snippets/search', snippets_views.search, name="search"),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('snippets/<int:snippet_pk>/display_other_user_snippet', snippets_views.other_snippet, name="other_snippet"),
    # path('snippets/user/<str:user_name>/', snippets_views.other_user, name="other_user")
]   

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
