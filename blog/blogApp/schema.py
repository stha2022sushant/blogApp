import graphene
from graphene_django import DjangoObjectType
from .models import BlogPost

class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        fields = ("id", "title", "content", "created_at")

class Query(graphene.ObjectType):
    blog_posts = graphene.List(BlogPostType)

    def resolve_blog_posts(self, info, **kwargs):
        return BlogPost.objects.all()
    
schema = graphene.Schema(query = Query)