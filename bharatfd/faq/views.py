from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializer import FAQSerializer

@api_view(['GET'])
def get_faq(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_faq_by_language(request, lang):
    faqs = FAQ.objects.all()
    translated_faqs = []

    for faq in faqs:
        question, answer = faq.get_translation(lang)
        translated_faqs.append({
            'id': faq.id,
            'question': question,
            'answer': answer
        })

    return Response(translated_faqs, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_faq(request):
    serializer = FAQSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        print("hello")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)