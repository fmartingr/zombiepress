# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.core.management import call_command


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        call_command("loaddata", "config_initial.json")
        
    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
