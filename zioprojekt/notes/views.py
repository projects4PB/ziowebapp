from django.views.generic.edit import CreateView

from .forms import NoteForm

from .models import Note

from zioprojekt.events.models import Event


class CreateNoteView(CreateView):
    model = Note
    template_name = 'notes/create.html'
    form_class = NoteForm
    success_url = '/'

    def form_valid(self, form):
        event = Event.objects.get(id=self.kwargs['event_pk'])
        object = form.save(commit=False)
        object.author = self.request.user.get_profile()
        object.event = event
        object.save()

        return super(CreateNoteView, self) \
            .form_valid(form)
