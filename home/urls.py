from django.urls import path
from .views import  homepage, add_news, select_by_category, news_detail
urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_news', add_news, name='add_news'),
    path('category/<category_id>', select_by_category, name='categories'),
    path('news_detail/<news_id>', news_detail, name='news_detail'),
]