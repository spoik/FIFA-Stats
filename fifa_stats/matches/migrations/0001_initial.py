# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Match'
        db.create_table(u'matches_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('winning_players_score', self.gf('django.db.models.fields.IntegerField')()),
            ('losing_players_score', self.gf('django.db.models.fields.IntegerField')()),
            ('winning_club', self.gf('django.db.models.fields.related.ForeignKey')(related_name='won_matches', to=orm['clubs.Team'])),
            ('losing_club', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lost_matches', to=orm['clubs.Team'])),
        ))
        db.send_create_signal(u'matches', ['Match'])

        # Adding M2M table for field winning_players on 'Match'
        m2m_table_name = db.shorten_name(u'matches_match_winning_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm[u'matches.match'], null=False)),
            ('player', models.ForeignKey(orm[u'players.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['match_id', 'player_id'])

        # Adding M2M table for field losing_players on 'Match'
        m2m_table_name = db.shorten_name(u'matches_match_losing_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm[u'matches.match'], null=False)),
            ('player', models.ForeignKey(orm[u'players.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['match_id', 'player_id'])


    def backwards(self, orm):
        # Deleting model 'Match'
        db.delete_table(u'matches_match')

        # Removing M2M table for field winning_players on 'Match'
        db.delete_table(db.shorten_name(u'matches_match_winning_players'))

        # Removing M2M table for field losing_players on 'Match'
        db.delete_table(db.shorten_name(u'matches_match_losing_players'))


    models = {
        u'clubs.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'matches.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losing_club': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lost_matches'", 'to': u"orm['clubs.Team']"}),
            'losing_players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lost_matches'", 'symmetrical': 'False', 'to': u"orm['players.Player']"}),
            'losing_players_score': ('django.db.models.fields.IntegerField', [], {}),
            'winning_club': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'won_matches'", 'to': u"orm['clubs.Team']"}),
            'winning_players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'won_matches'", 'symmetrical': 'False', 'to': u"orm['players.Player']"}),
            'winning_players_score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'players.player': {
            'Meta': {'object_name': 'Player'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['matches']