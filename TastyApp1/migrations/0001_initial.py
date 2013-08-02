# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'A1M1_information'
        db.create_table(u'TastyApp1_a1m1_information', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Fname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Lname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'TastyApp1', ['A1M1_information'])

        # Adding model 'A1M2_extainfo'
        db.create_table(u'TastyApp1_a1m2_extainfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('users_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TastyApp1.A1M1_information'])),
            ('Fextra', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('Lextra', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'TastyApp1', ['A1M2_extainfo'])


    def backwards(self, orm):
        # Deleting model 'A1M1_information'
        db.delete_table(u'TastyApp1_a1m1_information')

        # Deleting model 'A1M2_extainfo'
        db.delete_table(u'TastyApp1_a1m2_extainfo')


    models = {
        u'TastyApp1.a1m1_information': {
            'Fname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Lname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'A1M1_information'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'TastyApp1.a1m2_extainfo': {
            'Fextra': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'Lextra': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'object_name': 'A1M2_extainfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'users_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TastyApp1.A1M1_information']"})
        }
    }

    complete_apps = ['TastyApp1']