from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('snippets/api/', views.SnippetListAPI.as_view()),
    path('snippets/api/<int:pk>', views.SnippetDetailAPI.as_view()),
    path('snippets/mixin/', views.SnippetListMX.as_view()),
    path('snippets/mixin/<int:pk>', views.SnippetDetailMX.as_view()),
    path('snippets/generic/', views.SnippetListGB.as_view()),
    path('snippets/generic/<int:pk>', views.SnippetDetailGB.as_view()),
    path('snippets/users/', views.UserList.as_view()),
    path('snippets/users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)