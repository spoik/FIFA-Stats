from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from .forms import MatchForm

# TODO: Figure out why this form isn't saving to the model
class MatchFormView(FormView):
    form_class = MatchForm
    template_name = 'matches/create_match.html'
    success_url = reverse_lazy('matches:list')