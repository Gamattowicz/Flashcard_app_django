from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer


@api_view(['GET'])
def home(request):
    return Response('Hello World!')
