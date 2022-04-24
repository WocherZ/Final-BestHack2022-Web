from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls, name='admin'),
    path('', include('app.urls')),
]

handler404 = 'app.views.error_404'
