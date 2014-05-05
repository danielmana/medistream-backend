# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organizer'
        db.create_table(u'medistream_organizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'medistream', ['Organizer'])

        # Adding model 'Event'
        db.create_table(u'medistream_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['medistream.Organizer'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('finish_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'medistream', ['Event'])

        # Adding model 'Speaker'
        db.create_table(u'medistream_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'medistream', ['Speaker'])

        # Adding model 'Talk'
        db.create_table(u'medistream_talk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='talks', to=orm['medistream.Event'])),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='talks', null=True, to=orm['medistream.Speaker'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pod_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'medistream', ['Talk'])

        # Adding unique constraint on 'Talk', fields ['event', 'order']
        db.create_unique(u'medistream_talk', ['event_id', 'order'])


    def backwards(self, orm):
        # Removing unique constraint on 'Talk', fields ['event', 'order']
        db.delete_unique(u'medistream_talk', ['event_id', 'order'])

        # Deleting model 'Organizer'
        db.delete_table(u'medistream_organizer')

        # Deleting model 'Event'
        db.delete_table(u'medistream_event')

        # Deleting model 'Speaker'
        db.delete_table(u'medistream_speaker')

        # Deleting model 'Talk'
        db.delete_table(u'medistream_talk')


    models = {
        u'medistream.event': {
            'Meta': {'ordering': "('start_date', 'title')", 'object_name': 'Event'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'finish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['medistream.Organizer']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'medistream.organizer': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'medistream.speaker': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Speaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'medistream.talk': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('event', 'order'),)", 'object_name': 'Talk'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'talks'", 'to': u"orm['medistream.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'pod_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'talks'", 'null': 'True', 'to': u"orm['medistream.Speaker']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['medistream']