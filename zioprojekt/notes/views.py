from django.views.generic.edit import CreateView

from .models import Note


class CreateNoteView(CreateView):
    model = Note
    template_name = 'notes/create.html'
    success_url = '/'
