from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.shortcuts import render
from .models import Author, Category, Post, Post_News, Subscription
from datetime import datetime
from .filters import PostFilter, PostFilterNews
from .forms import PostForm, PostFormNews
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class AuthorsList(ListView):
    model = Author
    # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    template_name = 'authors.html'
    # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    context_object_name = 'authors'

    def get_queryset(self):
        # return Author.objects.filter(author_name="author2")
        return Author.objects.all()

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре
    # context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом
    # обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context


class AuthorDetail(DetailView):
    model = Author
    # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    template_name = 'author.html'
    # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    context_object_name = 'author'


class NewsList(ListView):
    model = Post_News
    template_name = 'newslist.html'
    context_object_name = 'newslist'
    paginate_by = 10  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # показываем только новости в порядке убывания даты публикации
        #return Post_News.objects.filter(post_type='1').order_by('-input_date_time')
        # return Post.objects.all()
        queryset = super().get_queryset()
        self.filterset = PostFilterNews(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #context['news_count'] = self.get_queryset().count()
        #Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post_News
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post_News.objects.filter(post_type='1')  # показываем только новости

class ArticlesList(ListView):
    model = Post
    template_name = 'articleslist.html'
    context_object_name = 'articleslist'
    paginate_by = 10 # вот так мы можем указать количество записей на странице



    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()

        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset,)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # def get_queryset(self):
    #     # показываем только новости в порядке убывания даты публикации
    #    return Post.objects.filter(post_type='0').order_by('-input_date_time')
    #     # return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['news_count'] = self.get_queryset().count()
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset


        return context


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Post.objects.filter(post_type='0')  # показываем только статьи



# Добавляем новое представление для создания статей.
class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_articles',)
    # raise_exception = True
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

# Добавляем новое представление для создания статей.
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    raise_exception = True
    # Указываем нашу разработанную форму
    form_class = PostFormNews
    # модель товаров
    model = Post_News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_create.html'

# Добавляем представление для изменения статьи
class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_articles',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

# Добавляем представление для изменения статьи
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    # Указываем нашу разработанную форму
    form_class = PostFormNews
    # модель товаров
    model = Post_News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

# Представление удаляющее товар.
class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_articles',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    model = Post_News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )

