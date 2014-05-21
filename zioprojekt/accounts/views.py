from django.views.generic import TemplateView

from zioprojekt.events.models import Event


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self) \
            .get_context_data(**kwargs)

        events = Event.objects.user_events(
            self.request.user.get_profile())

        context.update({
            'events': events
        })

        return context
