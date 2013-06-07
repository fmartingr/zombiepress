# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Language', fields ['code']
        db.create_index(u'languages_language', ['code'])

        # Adding unique constraint on 'Language', fields ['code']
        db.create_unique(u'languages_language', ['code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Language', fields ['code']
        db.delete_unique(u'languages_language', ['code'])

        # Removing index on 'Language', fields ['code']
        db.delete_index(u'languages_language', ['code'])


    models = {
        u'languages.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2', 'db_index': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['languages']