# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TouristObject.search_index'
        db.delete_column(u'places_touristobject', 'search_index')


    def backwards(self, orm):
        # Adding field 'TouristObject.search_index'
        db.add_column(u'places_touristobject', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)


    models = {
        u'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'places.facilities': {
            'Meta': {'object_name': 'Facilities'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'places.touristobject': {
            'Meta': {'object_name': 'TouristObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.Facilities']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'places.touristobjectscity': {
            'Meta': {'object_name': 'TouristObjectsCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['places']