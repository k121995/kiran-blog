from django.contrib import admin
from blogapp.models import Post,comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','createdate','updatedate','status']
    list_filter=('status',)
    search_fields=('title','body',)
    row_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}

class commentAdmin(admin.ModelAdmin):
    list_display=['name','email','body','Created','Updated','active']
    list_filter=('Created','active','Updated')
    search_fields=('name','email','body')



admin.site.register(Post,PostAdmin),
admin.site.register(comment,commentAdmin)
