# coding=utf-8
from django.contrib import admin
from blog.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 包含了一个右侧边栏允许你根据list_filter属性中指定的字段来过滤返回结果
    list_filter = ('status', 'created', 'publish', 'author')
    # 搜索框
    search_fields = ('title', 'body')
    # 通过使用prepoupulated_fields属性告诉Django通过输入的标题来填充slug字段。
    prepopulated_fields = {'slug': ('title',)}
    # 现在的author字段展示显示为了一个搜索控件，这样当你的用户量达到成千上万级别的时候比再使用下拉框进行选择更加的人性化
    raw_id_fields = ('author',)

    date_hierarchy = 'publish'

    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
