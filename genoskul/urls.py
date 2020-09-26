
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from us.views import PrivacyTemplateView, TermOfServiceTemplateView, AboutTemplateView
from genoskul.views import HomeTemplateView
from filebrowser.sites import site

admin.site.site_header = 'Site d\'administration de GENOSKUL'
admin.site.index_title = 'Panel administration GENOSKUL'
admin.site.site_title = 'GENOSKUL Admin'


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('privacy/', PrivacyTemplateView.as_view(), name='privacy'),
    path('terms/', TermOfServiceTemplateView.as_view(), name='terms'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),
    path('registration/', include('accounts.urls', namespace="accounts")),
    path('jobs/', include('jobs.urls', namespace="jobs")),
    path('learning/', include('learning.urls', namespace="learning")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('ndjor/', include('ndjor.urls', namespace="ndjor")),
    path('admin/filebrowser/', site.urls),
    path('admin/staff/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
