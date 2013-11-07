# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Preference'
        db.create_table(u'config_preference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('pass_to_template', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'config', ['Preference'])


    def backwards(self, orm):
        # Deleting model 'Preference'
        db.delete_table(u'config_preference')


    models = {
        u'config.preference': {
            'Meta': {'object_name': 'Preference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'pass_to_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['config']
