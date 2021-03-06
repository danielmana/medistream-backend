# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Talk', fields ['event', 'order']
        db.delete_unique(u'medistream_talk', ['event_id', 'order'])

        # Deleting field 'Talk.order'
        db.delete_column(u'medistream_talk', 'order')


        # Changing field 'Talk.start_time'
        db.alter_column(u'medistream_talk', 'start_time', self.gf('django.db.models.fields.DateTimeField')())
        # Adding unique constraint on 'Talk', fields ['event', 'start_time']
        db.create_unique(u'medistream_talk', ['event_id', 'start_time'])


    def backwards(self, orm):
        # Removing unique constraint on 'Talk', fields ['event', 'start_time']
        db.delete_unique(u'medistream_talk', ['event_id', 'start_time'])

        # Adding field 'Talk.order'
        db.add_column(u'medistream_talk', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Talk.start_time'
        db.alter_column(u'medistream_talk', 'start_time', self.gf('django.db.models.fields.DateTimeField')(null=True))
        # Adding unique constraint on 'Talk', fields ['event', 'order']
        db.create_unique(u'medistream_talk', ['event_id', 'order'])


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
            'Meta': {'ordering': "('start_time',)", 'unique_together': "(('event', 'start_time'),)", 'object_name': 'Talk'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'talks'", 'to': u"orm['medistream.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pod_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'talks'", 'null': 'True', 'to': u"orm['medistream.Speaker']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['medistream']