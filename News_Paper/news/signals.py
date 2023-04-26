from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Post_News
from .tasks import articles_Created, news_Created


@receiver(post_save, sender=Post)
def articles_created(instance,  created,  **kwargs):
    #print('Создана статья', instance)
    if not created:
        return
    articles_Created.delay(instance.get_absolute_url)

    # emails = User.objects.filter(
    #     subscriptions__category=instance.category
    # ).values_list('email', flat=True)
    #
    # subject = f'Новая статья в категории {instance.category}'
    #
    # text_content = (
    #     f'Статья: {instance.post_header}\n'
    #     f'Ссылка на статью: http://127.0.0.1{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Статья: {instance.post_header}<br>'
    #     f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    #     f'Ссылка на статью</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()

@receiver(post_save, sender=Post_News)
def news_created(instance, created, **kwargs):
    #print('Создана статья', instance)
    if not created:
        return
    news_Created.delay(instance.get_absolute_url)



