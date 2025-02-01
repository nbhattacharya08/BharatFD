from django.urls import path
from .views import get_faq , create_faq

urlpatterns = [
    path('faq/', get_faq, name='faq'),
    path('faq/create_faq/', create_faq, name='create_faq')
]
