from rest_framework import generics,status
from .serializers import BlogPostSerializer
from .models import BlogPost
from django.http import HttpResponse
from rest_framework.response import Response


# Create your views here.
class BlogosPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
def home(request):
    return HttpResponse('This is the home page!') 