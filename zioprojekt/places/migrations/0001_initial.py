# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TouristObjectsCity'
        db.create_table('places_touristobjectscity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('places', ['TouristObjectsCity'])

        # Adding model 'HolidayCamp'
        db.create_table('places_holidaycamp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['HolidayCamp'])

        # Adding model 'RestCentre'
        db.create_table('places_restcentre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['RestCentre'])

        # Adding model 'Hotel'
        db.create_table('places_hotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['Hotel'])

        # Adding model 'Motel'
        db.create_table('places_motel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['Motel'])

        # Adding model 'Camping'
        db.create_table('places_camping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['Camping'])

        # Adding model 'GuestHouse'
        db.create_table('places_guesthouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('places', ['GuestHouse'])


    def backwards(self, orm):
        # Deleting model 'TouristObjectsCity'
        db.delete_table('places_touristobjectscity')

        # Deleting model 'HolidayCamp'
        db.delete_table('places_holidaycamp')

        # Deleting model 'RestCentre'
        db.delete_table('places_restcentre')

        # Deleting model 'Hotel'
        db.delete_table('places_hotel')

        # Deleting model 'Motel'
        db.delete_table('places_motel')

        # Deleting model 'Camping'
        db.delete_table('places_camping')

        # Deleting model 'GuestHouse'
        db.delete_table('places_guesthouse')


    models = {
        'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'places.camping': {
            'Meta': {'object_name': 'Camping'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.guesthouse': {
            'Meta': {'object_name': 'GuestHouse'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.holidaycamp': {
            'Meta': {'object_name': 'HolidayCamp'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.motel': {
            'Meta': {'object_name': 'Motel'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.restcentre': {
            'Meta': {'object_name': 'RestCentre'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.touristobjectscity': {
            'Meta': {'object_name': 'TouristObjectsCity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['places']