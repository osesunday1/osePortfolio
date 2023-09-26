
from django.urls import path, include
from .  import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',  views.home, name = 'home'),
    path('clientfeedback/', include('clientfeedback.urls')),
    path('downloadfile/', views.downloadfile, name='downloadfile')
]