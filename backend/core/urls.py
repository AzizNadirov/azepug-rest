from pydoc import describe
from sysconfig import get_scheme_names
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.views import AccountCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),

    path('blogs/', include('apps.blog.urls')),
    path('events/', include('apps.event.urls')),
    path('news/', include('apps.news.urls')),
    path('vacancies/', include('apps.vacancy.urls')),
    path('qs/', include('apps.forum.urls')),
    path('user/', include('apps.account.urls')),

    path('register/', AccountCreateView.as_view(), name = 'register'),

    path('schema', get_schema_view(title='azepug', description='', version='1.0'), name='api-schema'),
    path('docs', include_docs_urls(title='AzePUG'), name='docs')
]
