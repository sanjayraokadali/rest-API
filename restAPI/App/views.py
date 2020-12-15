from django.shortcuts import render
from rest_framework import serializers
from App.models import BookModel
from App.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from App import views
# Create your views here.
@api_view(['GET','POST'])
def base(request):

    if request.method == 'GET':

        books = BookModel.objects.all()

        s = BookSerializer(books, many=True)

        return Response(s.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)

        s = BookSerializer(data = data)

        if s.is_valid():

            s.save()

            return Response(s.data)
