# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offer.price'
        db.add_column('offers_offer', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offer.price'
        db.delete_column('offers_offer', 'price')


    models = {
        'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'offers.offer': {
            'Meta': {'object_name': 'Offer'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tourist_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObject']"})
        },
        'places.facilities': {
            'Meta': {'object_name': 'Facilities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.touristobject': {
            'Meta': {'object_name': 'TouristObject'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['places.Facilities']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'db_index': 'True', 'null': 'True'})
        },
        'places.touristobjectscity': {
            'Meta': {'object_name': 'TouristObjectsCity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['offers']