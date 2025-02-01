from django.urls import path
from .views import get_faq , get_faq_by_language

urlpatterns = [
    path('faq/', get_faq, name='faq'),
    path('faq/<str:lang>/', get_faq_by_language, name='faq_by_language'),
]
