
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.translation import get_language

from .models import Page
from .utils import parse_yaml_context

DEFAULT_LANGUAGE = "cs"

#@cache_page(60 * 15)  # Cache the page for 15 minutes
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)

    data = parse_yaml_context(page.content_yaml)

    lang = get_language() or DEFAULT_LANGUAGE
    lang = lang.split("-")[0]  # "cs-CZ" → "cs"

    page_context = data.get(lang) or data.get(DEFAULT_LANGUAGE, data)

    context = {
        "page": page,
        **page_context,
    }

    return render(request, f"pages/{slug}.html", context)