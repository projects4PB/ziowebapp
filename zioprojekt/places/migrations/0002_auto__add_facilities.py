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

        # Adding M2M table for field facilities on 'HolidayCamp'
        m2m_table_name = db.shorten_name('places_holidaycamp_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('holidaycamp', models.ForeignKey(orm['places.holidaycamp'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['holidaycamp_id', 'facilities_id'])

        # Adding M2M table for field facilities on 'Hotel'
        m2m_table_name = db.shorten_name('places_hotel_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotel', models.ForeignKey(orm['places.hotel'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hotel_id', 'facilities_id'])

        # Adding M2M table for field facilities on 'Motel'
        m2m_table_name = db.shorten_name('places_motel_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('motel', models.ForeignKey(orm['places.motel'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['motel_id', 'facilities_id'])

        # Adding M2M table for field facilities on 'RestCentre'
        m2m_table_name = db.shorten_name('places_restcentre_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restcentre', models.ForeignKey(orm['places.restcentre'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['restcentre_id', 'facilities_id'])

        # Adding M2M table for field facilities on 'GuestHouse'
        m2m_table_name = db.shorten_name('places_guesthouse_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guesthouse', models.ForeignKey(orm['places.guesthouse'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guesthouse_id', 'facilities_id'])

        # Adding M2M table for field facilities on 'Camping'
        m2m_table_name = db.shorten_name('places_camping_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('camping', models.ForeignKey(orm['places.camping'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['camping_id', 'facilities_id'])


    def backwards(self, orm):
        # Deleting model 'Facilities'
        db.delete_table('places_facilities')

        # Removing M2M table for field facilities on 'HolidayCamp'
        db.delete_table(db.shorten_name('places_holidaycamp_facilities'))

        # Removing M2M table for field facilities on 'Hotel'
        db.delete_table(db.shorten_name('places_hotel_facilities'))

        # Removing M2M table for field facilities on 'Motel'
        db.delete_table(db.shorten_name('places_motel_facilities'))

        # Removing M2M table for field facilities on 'RestCentre'
        db.delete_table(db.shorten_name('places_restcentre_facilities'))

        # Removing M2M table for field facilities on 'GuestHouse'
        db.delete_table(db.shorten_name('places_guesthouse_facilities'))

        # Removing M2M table for field facilities on 'Camping'
        db.delete_table(db.shorten_name('places_camping_facilities'))


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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.facilities': {
            'Meta': {'object_name': 'Facilities'},
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['places.Facilities']", 'symmetrical': 'False'}),
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