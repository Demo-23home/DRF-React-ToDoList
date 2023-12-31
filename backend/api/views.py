from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerailizers
from .models import Note
# Create your views here.

@api_view(["GET"])
def getRoute(request):
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


@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerailizers(notes, many=True)
    return Response({"Notes": serializer.data})


@api_view(['GET'])
def getNote (request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerailizers(notes, many=False)
    return Response({"Notes": serializer.data})