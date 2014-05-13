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

        # Adding model 'HolidayCamp'
        db.create_table('places_holidaycamp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['HolidayCamp'])

        # Adding M2M table for field facilities on 'HolidayCamp'
        m2m_table_name = db.shorten_name('places_holidaycamp_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('holidaycamp', models.ForeignKey(orm['places.holidaycamp'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['holidaycamp_id', 'facilities_id'])

        # Adding model 'RestCentre'
        db.create_table('places_restcentre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['RestCentre'])

        # Adding M2M table for field facilities on 'RestCentre'
        m2m_table_name = db.shorten_name('places_restcentre_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restcentre', models.ForeignKey(orm['places.restcentre'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['restcentre_id', 'facilities_id'])

        # Adding model 'Hotel'
        db.create_table('places_hotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['Hotel'])

        # Adding M2M table for field facilities on 'Hotel'
        m2m_table_name = db.shorten_name('places_hotel_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotel', models.ForeignKey(orm['places.hotel'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hotel_id', 'facilities_id'])

        # Adding model 'Motel'
        db.create_table('places_motel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['Motel'])

        # Adding M2M table for field facilities on 'Motel'
        m2m_table_name = db.shorten_name('places_motel_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('motel', models.ForeignKey(orm['places.motel'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['motel_id', 'facilities_id'])

        # Adding model 'Camping'
        db.create_table('places_camping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['Camping'])

        # Adding M2M table for field facilities on 'Camping'
        m2m_table_name = db.shorten_name('places_camping_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('camping', models.ForeignKey(orm['places.camping'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['camping_id', 'facilities_id'])

        # Adding model 'GuestHouse'
        db.create_table('places_guesthouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.TouristObjectsCategory'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.TouristObjectsCity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('search_index', self.gf('djorm_pgfulltext.fields.VectorField')(db_index=True, default='', null=True)),
        ))
        db.send_create_signal('places', ['GuestHouse'])

        # Adding M2M table for field facilities on 'GuestHouse'
        m2m_table_name = db.shorten_name('places_guesthouse_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guesthouse', models.ForeignKey(orm['places.guesthouse'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guesthouse_id', 'facilities_id'])


    def backwards(self, orm):
        # Deleting model 'Facilities'
        db.delete_table('places_facilities')

        # Deleting model 'TouristObjectsCity'
        db.delete_table('places_touristobjectscity')

        # Deleting model 'HolidayCamp'
        db.delete_table('places_holidaycamp')

        # Removing M2M table for field facilities on 'HolidayCamp'
        db.delete_table(db.shorten_name('places_holidaycamp_facilities'))

        # Deleting model 'RestCentre'
        db.delete_table('places_restcentre')

        # Removing M2M table for field facilities on 'RestCentre'
        db.delete_table(db.shorten_name('places_restcentre_facilities'))

        # Deleting model 'Hotel'
        db.delete_table('places_hotel')

        # Removing M2M table for field facilities on 'Hotel'
        db.delete_table(db.shorten_name('places_hotel_facilities'))

        # Deleting model 'Motel'
        db.delete_table('places_motel')

        # Removing M2M table for field facilities on 'Motel'
        db.delete_table(db.shorten_name('places_motel_facilities'))

        # Deleting model 'Camping'
        db.delete_table('places_camping')

        # Removing M2M table for field facilities on 'Camping'
        db.delete_table(db.shorten_name('places_camping_facilities'))

        # Deleting model 'GuestHouse'
        db.delete_table('places_guesthouse')

        # Removing M2M table for field facilities on 'GuestHouse'
        db.delete_table(db.shorten_name('places_guesthouse_facilities'))


    models = {
        'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'places.camping': {
            'Meta': {'object_name': 'Camping'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.facilities': {
            'Meta': {'object_name': 'Facilities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'places.guesthouse': {
            'Meta': {'object_name': 'GuestHouse'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.holidaycamp': {
            'Meta': {'object_name': 'HolidayCamp'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.motel': {
            'Meta': {'object_name': 'Motel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.restcentre': {
            'Meta': {'object_name': 'RestCentre'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.TouristObjectsCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.TouristObjectsCity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'db_index': 'True', 'default': "''", 'null': 'True'})
        },
        'places.touristobjectscity': {
            'Meta': {'object_name': 'TouristObjectsCity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['places']