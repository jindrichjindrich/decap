from django.db import models
from django.core.exceptions import ValidationError
import yaml

# Create your models here.

class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content_yaml = models.TextField(
        help_text="""
YAML defining template variables for this page
<pre>
YAML authoring rules: 
✅ Multiline text
cs:
  section_text: |
    Line one
    Line two
✅ Lists
en:
  features:
    - Fast
    - Simple
    - Reliable
✅ Nested blocks
cs:
    hero:
    title: Welcome
    subtitle: Hello world

✅ In Template: 
{{ hero.title }}
</pre>
"""
    )

    def clean(self):
        try:
            data = yaml.safe_load(self.content_yaml)
            if data is not None and not isinstance(data, dict):
                raise ValidationError("YAML must define a dictionary")
        except yaml.YAMLError as e:
            raise ValidationError(f"Invalid YAML: {e}")

        for lang in ("cs", "en"):
            if lang not in data:
                raise ValidationError(f"Missing '{lang}' section")
            if not isinstance(data[lang], dict):
                raise ValidationError(f"'{lang}' must be a dictionary")

    def __str__(self):
        return self.slug

class SiteSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()