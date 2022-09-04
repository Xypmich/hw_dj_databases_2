from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


# class ScopeInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             var = form.cleaned_data
#             if var:
#                 raise ValidationError('Может быть только 1 основной тег!')
#         return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    # formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


