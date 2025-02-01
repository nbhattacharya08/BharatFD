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



@api_view(['POST'])
def create_faq(request):
    serializer = FAQSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)