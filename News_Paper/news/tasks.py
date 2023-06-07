# from celery import shared_task
# from django.core.mail import EmailMultiAlternatives
# from django.contrib.auth.models import User
#
#
# @shared_task
# def news_Created(instance,  **kwargs):
#     #print('Создана статья', instance)
#
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новая новость в категории {instance.category}'
#
#     text_content = (
#         f'Новость: {instance.post_header}\n'
#         f'Ссылка на новость: http://127.0.0.1{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Новость: {instance.post_header}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на новость</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
# @shared_task
# def articles_Created(instance, **kwargs):
#     #print('Создана статья', instance)
#
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новая новость в категории {instance.category}'
#
#     text_content = (
#         f'Новость: {instance.post_header}\n'
#         f'Ссылка на новость: http://127.0.0.1{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Новость: {instance.post_header}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на новость</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
#
#
