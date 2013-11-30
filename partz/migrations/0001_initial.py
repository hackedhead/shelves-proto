# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DatedModel'
        db.create_table(u'partz_datedmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'partz', ['DatedModel'])

        # Adding model 'Project'
        db.create_table(u'partz_project', (
            (u'datedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partz.DatedModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'partz', ['Project'])

        # Adding model 'Note'
        db.create_table(u'partz_note', (
            (u'datedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partz.DatedModel'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partz.Project'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'partz', ['Note'])

        # Adding model 'Media'
        db.create_table(u'partz_media', (
            (u'datedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partz.DatedModel'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partz.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'partz', ['Media'])


    def backwards(self, orm):
        # Deleting model 'DatedModel'
        db.delete_table(u'partz_datedmodel')

        # Deleting model 'Project'
        db.delete_table(u'partz_project')

        # Deleting model 'Note'
        db.delete_table(u'partz_note')

        # Deleting model 'Media'
        db.delete_table(u'partz_media')


    models = {
        u'partz.datedmodel': {
            'Meta': {'object_name': 'DatedModel'},
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'partz.media': {
            'Meta': {'object_name': 'Media', '_ormbases': [u'partz.DatedModel']},
            u'datedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partz.DatedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['partz.Project']"})
        },
        u'partz.note': {
            'Meta': {'object_name': 'Note', '_ormbases': [u'partz.DatedModel']},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'datedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partz.DatedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['partz.Project']"})
        },
        u'partz.project': {
            'Meta': {'object_name': 'Project', '_ormbases': [u'partz.DatedModel']},
            u'datedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partz.DatedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['partz']