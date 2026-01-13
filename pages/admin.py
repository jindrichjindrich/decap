from django.contrib import admin

# Register your models here.

from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("admin/yaml_help.css",)}
        js = ("admin/yaml_help.js",)
    list_display = ("slug", "title")
    prepopulated_fields = {"slug": ("title",)}