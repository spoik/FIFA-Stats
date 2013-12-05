from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
    	ordering = ['first_name', 'last_name']
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

