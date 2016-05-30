# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .forms import GenericAttributeInlineForm, TitleMetaAdminForm
from .models import GenericMetaAttribute, PageMeta, TitleMeta


class GenericAttributePageInline(admin.TabularInline):
    model = GenericMetaAttribute
    form = GenericAttributeInlineForm
    fields = ('page', 'attribute', 'name', 'value')
    extra = 1


class GenericAttributeTitleInline(admin.TabularInline):
    model = GenericMetaAttribute
    form = GenericAttributeInlineForm
    fields = ('title', 'attribute', 'name', 'value')
    extra = 1


class PageMetaAdmin(PageExtensionAdmin):
    raw_id_fields = ('og_author',)
    inlines = (GenericAttributePageInline,)
    fieldsets = (
        (None, {'fields': ('image',)}),
        (_('OpenGraph'), {
            'fields': (
                'og_type', ('og_author', 'og_author_url', 'og_author_fbid'),
                ('og_publisher', 'og_app_id', 'fb_pages')
            ),
            'classes': ('collapse',)
        }),
        (_('Twitter Cards'), {
            'fields': ('twitter_type', 'twitter_author'),
            'classes': ('collapse',)
        }),
        (_('Google+ Snippets'), {
            'fields': ('gplus_type', 'gplus_author'),
            'classes': ('collapse',)
        }),
    )

    class Media:
        css = {
            'all': ('%sdjangocms_page_meta/css/%s' % (
                settings.STATIC_URL, 'djangocms_page_meta_admin.css'),)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(PageMeta, PageMetaAdmin)


class TitleMetaAdmin(TitleExtensionAdmin):
    form = TitleMetaAdminForm
    inlines = (GenericAttributeTitleInline,)

    class Media:
        css = {
            'all': ('%sdjangocms_page_meta/css/%s' % (
                settings.STATIC_URL, 'djangocms_page_meta_admin.css'),)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(TitleMeta, TitleMetaAdmin)
