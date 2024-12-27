import graphene 

from graphene_django.types import DjangoObjectType 
from graphene_django.filter import DjangoFilterConnectionField

from .models import BlogPost
from .filters import BlogPostFilter


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        filter_fields = ['title', 'created_at']
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    blog_post = graphene.Field(BlogPostType, id=graphene.Int())
    all_blog_posts = DjangoFilterConnectionField(BlogPostType, filterset_class=BlogPostFilter)

    def resolve_blog_post(self, info, id):
        return BlogPost.objects.get(id=id)

    def resolve_all_blog_posts(self, info, **kwargs):
        return BlogPost.objects.all()

class CreateBlogPost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    blog_post = graphene.Field(BlogPostType)

    def mutate(self, info, title, content):
        blog_post = BlogPost.objects.create(title=title, content=content)
        return CreateBlogPost(blog_post=blog_post)

class UpdateBlogPost(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        content = graphene.String()

    blog_post = graphene.Field(BlogPostType)

    def mutate(self, info, id, title, content):
        blog_post = BlogPost.objects.get(id=id)
        blog_post.title = title
        blog_post.content = content
        blog_post.save()
        return UpdateBlogPost(blog_post=blog_post)

class DeleteBlogPost(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        BlogPost.objects.get(id=id).delete()
        return DeleteBlogPost(success=True)

class Mutation(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    delete_blog_post = DeleteBlogPost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

