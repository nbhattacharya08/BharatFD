import pytest
from django.core.cache import cache
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question="What is Docker?", answer="Docker is a platform for developing, shipping, and running applications.")
    
    # Test English translation
    question, answer = faq.get_translation('en')
    assert question == "What is Docker?"
    assert answer == "Docker is a platform for developing, shipping, and running applications."
    
    # Test Hindi translation
    question_hi, answer_hi = faq.get_translation('hi')
    assert question_hi is not None
    assert answer_hi is not None
    
    # Test Bengali translation
    question_bn, answer_bn = faq.get_translation('bn')
    assert question_bn is not None
    assert answer_bn is not None

    # Ensure translations are cached
    cache_key_hi = f'faq_{faq.question}_{faq.answer}_hi'
    cached_translation_hi = cache.get(cache_key_hi)
    assert cached_translation_hi == (question_hi, answer_hi)

    cache_key_bn = f'faq_{faq.question}_{faq.answer}_bn'
    cached_translation_bn = cache.get(cache_key_bn)
    assert cached_translation_bn == (question_bn, answer_bn)