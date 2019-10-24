from django.contrib import admin
from .models import Article, Comment, Hashtag # import 해야 함
# Register your models here.

## 아래의 클래스를 작성하면 해당 Attribute를 확인할 수 있음
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content') # tuple로 적어 보낼 수 있음
    list_display_links = ('title',) # links를 지정 # tuple에선 single element는 꼭 comma를 써야 함

admin.site.register(Article, ArticleAdmin)


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Hashtag, HashtagAdmin)