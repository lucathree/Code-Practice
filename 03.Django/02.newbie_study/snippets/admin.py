from django.contrib import admin
from snippets.models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    fields = ['title', 'code', 'linenos', 'language', 'style', 'highlighted', 'owner']