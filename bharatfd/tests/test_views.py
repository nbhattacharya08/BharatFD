import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_get_faq():
    client = APIClient()
    FAQ.objects.create(question="What is Docker?", answer="Docker is a platform for developing, shipping, and running applications.")
    
    response = client.get(reverse('faq'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['question'] == "What is Docker?"
    assert response.data[0]['answer'] == "Docker is a platform for developing, shipping, and running applications."

@pytest.mark.django_db
def test_get_faq_by_language():
    client = APIClient()
    faq = FAQ.objects.create(question="What is Docker?", answer="Docker is a platform for developing, shipping, and running applications.")
    
    response = client.get(reverse('faq_by_language', args=['hi']))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['question'] is not None
    assert response.data[0]['answer'] is not None

@pytest.mark.django_db
def test_add_faq():
    client = APIClient()
    data = {
        "question": "What is Docker?",
        "answer": "Docker is a platform for developing, shipping, and running applications."
    }
    response = client.post(reverse('add_faq'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['question'] == "What is Docker?"
    assert response.data['answer'] == "Docker is a platform for developing, shipping, and running applications."