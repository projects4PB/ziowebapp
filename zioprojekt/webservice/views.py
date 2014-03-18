from rest_framework.generics import ListAPIView

from .models import Note

from .serializers import NoteSerializer


class NotesListWS(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
