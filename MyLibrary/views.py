from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
import requests


def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def savebook(request):
    if request.method=='POST':
        saveserialize=BookSerializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


def addbook(request):
    if request.method=='POST':
        bookname=request.POST.get('bookname')
        author=request.POST.get('author')
        quantity=request.POST.get('quantity')
        data={'bookname':bookname, 'author': author, 'quantity': quantity}
        headers={'Content-Type': 'application/json'}
        read=requests.post('http://127.0.0.1:7000/', json=data, headers=headers)
        return render(request, 'add.html')
    else:
        return render(request, 'add.html')


@api_view(['GET'])
def showbooks(request):
    if request.method=='GET':
        results=Book.objects.all()
        serialize=BookSerializer(results, many=True)
        return Response(serialize.data)


def displaybooks(request):
    callapi=requests.get('http://127.0.0.1:7000/showbooks/')
    results=callapi.json()
    return render(request, 'show.html', {'Book': results})


@api_view(['POST'])
def deletebooks(request):
    if request.method=='POST':
        bookid=request.POST.get('bookid')
        record=Book.objects.filter(id=bookid)
        record.delete()
        results = Book.objects.all()
        return render(request, 'show.html', {'Book': results})


def deletedbooks(request):
    return render(request, 'delete.html')


def bookupdate(request):
    return render(request, 'updated.html')

def updatedbooks(request):
    if request.method == 'POST':
        bookid = request.POST.get('bookid')
        book = Book.objects.filter(id=bookid)
        book.bookname = request.POST.get('bookname')
        book.author = request.POST.get('author')
        book.quantity = request.POST.get('quantity')
        # book.save()
        results = Book.objects.all()
        return render(request, 'show.html')





def updatebooks(request):
    return render(request, 'update.html')
