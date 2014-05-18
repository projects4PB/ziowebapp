from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from zioprojekt.notes.models import Note

from .serializers import NoteSerializer


class NotesListWS(ListAPIView):
    authentication_class = BasicAuthentication
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        #return Note.objects.get_for_user(self.request.user)
        return Note.objects.all()
