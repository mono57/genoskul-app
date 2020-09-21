
from django.contrib import admin
from django.urls import path, include

from genoskul.views import HomeTemplateView


admin.site.site_header = 'Site d\'administration de GENOSKUL'
admin.site.index_title = 'Panel administration GENOSKUL'
admin.site.site_title = 'GENOSKUL Admin'


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),
    path('registration/', include('accounts.urls', namespace="accounts")),
    path('jobs/', include('jobs.urls', namespace="jobs")),
    path('learning/', include('learning.urls', namespace="learning")),
    path('ndjor/', include('ndjor.urls', namespace="ndjor")),
    path('admin/', admin.site.urls),
]
