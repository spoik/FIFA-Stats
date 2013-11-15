from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Match
from .forms import MatchForm

# TODO: Figure out why this form isn't saving to the model
class MatchCreateView(CreateView):
    model = Match
    # template_name = 'matches/create_match.html'
    form_class = MatchForm
    success_url = reverse_lazy('matches:list')