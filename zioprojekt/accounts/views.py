from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from zioprojekt.events.models import Event
from zioprojekt.accounts.models import UserProfile
from zioprojekt.accounts.forms import UserProfileForm


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


class EditProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/edit.html'
