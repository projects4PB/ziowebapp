# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Facilities'
        db.create_table('places_facilities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('places', ['Facilities'])

        # Adding model 'TouristObjectsCity'
        db.create_table('places_touristobjectscity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('places', ['TouristObjectsCity'])

        # Adding model 'TouristObject'
        db.create_table('places_touristobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(null=True, default='', db_index=True)),
        ))
        db.send_create_signal('places', ['TouristObject'])

        # Adding M2M table for field facilities on 'TouristObject'
        m2m_table_name = db.shorten_name('places_touristobject_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('touristobject', models.ForeignKey(orm['places.touristobject'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['touristobject_id', 'facilities_id'])


    def backwards(self, orm):
        # Deleting model 'Facilities'
        db.delete_table('places_facilities')

        # Deleting model 'TouristObjectsCity'
        db.delete_table('places_touristobjectscity')

        # Deleting model 'TouristObject'
        db.delete_table('places_touristobject')

        # Removing M2M table for field facilities on 'TouristObject'
        db.delete_table(db.shorten_name('places_touristobject_facilities'))


    models = {
        'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['places.Facilities']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'null': 'True', 'default': "''", 'db_index': 'True'})
        },
        'places.touristobjectscity': {
            'Meta': {'object_name': 'TouristObjectsCity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['places']