from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated


class PostView(mixins.ListModelMixin,
mixins.CreateModelMixin,
generics.GenericAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(self,request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)



# class TestView(APIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self, request, *args, **kwargs):
#         qs=Post.objects.all()
#         post=qs.first()
#         #serializer=PostSerializer(qs,many=True)
#         serializer=PostSerializer(post)
#         return Response(serializer.data)
#     def post(self,request,*args,**kwargs):
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)  
#         return Response(serializer.errors)      


# Create your views here.
# def test_view(request):
#     data={
#         'name' : 'asmaa',
#         'age': 22
#     }
#     return JsonResponse(data)