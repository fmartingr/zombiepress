# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Preference', fields ['key']
        db.create_index(u'config_preference', ['key'])

        # Adding unique constraint on 'Preference', fields ['key']
        db.create_unique(u'config_preference', ['key'])


    def backwards(self, orm):
        # Removing unique constraint on 'Preference', fields ['key']
        db.delete_unique(u'config_preference', ['key'])

        # Removing index on 'Preference', fields ['key']
        db.delete_index(u'config_preference', ['key'])


    models = {
        u'config.preference': {
            'Meta': {'object_name': 'Preference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'pass_to_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['config']