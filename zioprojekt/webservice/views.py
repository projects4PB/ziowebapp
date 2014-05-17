from rest_framework.generics import ListAPIView

from zioprojekt.notes.models import Note

from .serializers import NoteSerializer


class NotesListWS(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
