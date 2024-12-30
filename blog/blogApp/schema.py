import strawberry
from typing import List
from strawberry.types import Info
from asgiref.sync import sync_to_async
from . types import BlogPostType
from . models import BlogPost

@strawberry.type
class Query:
    @strawberry.field
    async def blog_posts(self, info: Info) -> List[BlogPostType]:
        return await sync_to_async(list)(BlogPost.objects.all())

    @strawberry.field
    async def blog_post(self, info: Info, id: strawberry.ID) -> BlogPostType:
        return await sync_to_async(BlogPost.objects.get)(pk=id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_blog_post(self, title: str, content: str) -> BlogPostType:
        blog_post = await sync_to_async(BlogPost.objects.create)(title=title, content=content)
        return blog_post

    @strawberry.mutation
    async def update_blog_post(self, id: strawberry.ID, title: str, content: str) -> BlogPostType:
        blog_post = await sync_to_async(BlogPost.objects.get)(pk=id)
        blog_post.title = title
        blog_post.content = content
        await sync_to_async(blog_post.save)()
        return blog_post

    @strawberry.mutation
    async def delete_blog_post(self, id: strawberry.ID) -> str:
        blog_post = await sync_to_async(BlogPost.objects.get)(pk=id)
        await sync_to_async(blog_post.delete)()
        return f"Blog post with ID {id} was deleted."

schema = strawberry.Schema(query=Query, mutation=Mutation)
