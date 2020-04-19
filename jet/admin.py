from __future__ import absolute_import
from django.contrib import admin


class CompactInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/compact.html'
