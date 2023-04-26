from django.urls import path
from .views import NewsList, NewsDetail, AuthorsList, AuthorDetail,\
    ArticlesList, ArticlesDetail, ArticlesCreate, ArticlesUpdate, ArticlesDelete,\
    NewsCreate, NewsDelete, NewsUpdate, subscriptions


# импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('news/', NewsList.as_view(), name = 'news_list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>/', ArticlesDetail.as_view(), name='articles_detail'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('subscriptions/', subscriptions, name='subscriptions'),

]