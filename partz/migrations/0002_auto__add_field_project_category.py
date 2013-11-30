# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.category'
        db.add_column(u'partz_project', 'category',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.category'
        db.delete_column(u'partz_project', 'category')


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
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'datedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partz.DatedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['partz']