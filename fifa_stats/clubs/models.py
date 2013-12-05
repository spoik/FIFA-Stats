from django.db import models
from django.utils.translation import ugettext as _

class Team(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
    	ordering = ['name']
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __unicode__(self):
        return u'%s' % self.name
    