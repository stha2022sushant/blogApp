from django.contrib import admin
from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView
from blogApp.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', AsyncGraphQLView.as_view(schema=schema)),  # Direct mapping
    path('blogApp/', include('blogApp.urls')),  # Optional app URLs
]

