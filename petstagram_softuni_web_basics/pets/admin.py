from django.contrib import admin

from common.models import Comment
from pets.models import Pet, Like


class LikeInlineAdmin(admin.TabularInline):
    model = Like


class CommentInlineAdmin(admin.TabularInline):
    model = Comment


class PetAdmin(admin.ModelAdmin):
    #fields = ('type', 'name')
    list_display = ('name', 'type')
    list_filter = ('type',)
    inlines = [
        LikeInlineAdmin,
        CommentInlineAdmin,
    ]


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
