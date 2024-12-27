import django_filters
from .models import BlogPost 

class BlogPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = BlogPost
        fields = ['title', 'created_at']
        
