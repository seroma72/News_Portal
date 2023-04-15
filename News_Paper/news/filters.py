from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Post_News

#создаём фильтр
# class CategoryFilter(FilterSet):
#     class Meta:
#         model = Category
#         fields = {
#
#             # по названию
#             'name': ['icontains'],
#             # позже даты создания
#            # 'input_date_time': ['gt'],
#         }
class PostFilter(FilterSet):

    added_after = DateTimeFilter(
        field_name='input_date_time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )

    )


    class Meta:
        model = Post

        fields = {
            'post_header': ['icontains'],

        }


class PostFilterNews(FilterSet):
    added_after = DateTimeFilter(
        field_name='input_date_time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )

    )

    class Meta:
        model = Post_News

        fields = {
            'post_header': ['icontains'],

        }




