from django.contrib import admin
from .models import Post, Comment, Category


class CommentItemInline(admin.TabularInline):
	model=Comment
	raw_id_fields=['post']


class PostAdmin(admin.ModelAdmin):
	search_fields =['title', 'intro', 'body']
	list_display = ['title', 'slug', 'date_posted', 'status']
	list_filter=['category', 'date_posted']
	inlines =[CommentItemInline]
	prepopulated_fields={'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
	search_fields=['title']
	list_display=['title', 'slug']
	prepopulated_fields={'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_display=['post', 'name', 'comment_date']

# Register your models here.
admin.site.register(Post, PostAdmin )
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

