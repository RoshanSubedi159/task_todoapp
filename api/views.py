from urllib import response
import django
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api
from .models import note
from .searializer import note_serializer
from api import searializer
# Create your views here.


@api_view(['GET'])
def getRoutes(routes):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = note.objects.all().order_by('-updated')
    serializer = note_serializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    notes = note.objects.get(id=pk)
    serializer = note_serializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    Note = note.objects.create(
        body=data['body']
    )
    searializer = note_serializer(Note, many=False)
    return Response(searializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    notee = note.objects.get(id=pk)
    serializer = note_serializer(instance=notee, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    Note = note.objects.get(id=pk)
    Note.delete()
    return Response('Note was deleted')
