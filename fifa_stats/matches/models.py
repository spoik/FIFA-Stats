from django.db import models
from django.utils.translation import ugettext as _

from players.models import Player
from clubs.models import Team

class Match(models.Model):
    # When the match took place
    date = models.DateTimeField()

    # TODO: Validate upon save to make sure the winning team and losing team
    # do not share any players
    # Teams
    winning_players = models.ManyToManyField(Player, related_name='won_matches')
    losing_players = models.ManyToManyField(Player, related_name='lost_matches')

    # TODO: Make sure the winning team's score is greater than the loosing team's
    # Scores
    winning_players_score = models.IntegerField()
    losing_players_score = models.IntegerField()

    # The clubs that played in the match
    winning_club = models.ManyToManyField(Team, related_name='won_matches')
    losing_club = models.ManyToManyField(Team, related_name='lost_matches')

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        pass
    