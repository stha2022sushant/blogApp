import strawberry
from strawberry_django import type
from . models import BlogPost
from strawberry import auto

@type(BlogPost)
class BlogPostType:
    id: auto
    title: auto
    content: str
    created_at: auto
    updated_at: auto
