from django.urls import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'resume'

urlpatterns = [
    path('',main,name='main_page'),
    path('test',testing,name='testt'),
    path('pdf',pdf,name='pdf')
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)