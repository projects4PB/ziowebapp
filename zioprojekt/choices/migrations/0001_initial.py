# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TripTypeChoice'
        db.create_table('choices_triptypechoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('choices', ['TripTypeChoice'])

        # Adding M2M table for field category on 'TripTypeChoice'
        m2m_table_name = db.shorten_name('choices_triptypechoice_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triptypechoice', models.ForeignKey(orm['choices.triptypechoice'], null=False)),
            ('touristobjectscategory', models.ForeignKey(orm['categories.touristobjectscategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triptypechoice_id', 'touristobjectscategory_id'])

        # Adding M2M table for field facilities on 'TripTypeChoice'
        m2m_table_name = db.shorten_name('choices_triptypechoice_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triptypechoice', models.ForeignKey(orm['choices.triptypechoice'], null=False)),
            ('facilities', models.ForeignKey(orm['places.facilities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triptypechoice_id', 'facilities_id'])


    def backwards(self, orm):
        # Deleting model 'TripTypeChoice'
        db.delete_table('choices_triptypechoice')

        # Removing M2M table for field category on 'TripTypeChoice'
        db.delete_table(db.shorten_name('choices_triptypechoice_category'))

        # Removing M2M table for field facilities on 'TripTypeChoice'
        db.delete_table(db.shorten_name('choices_triptypechoice_facilities'))


    models = {
        'categories.touristobjectscategory': {
            'Meta': {'object_name': 'TouristObjectsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'choices.triptypechoice': {
            'Meta': {'object_name': 'TripTypeChoice'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['categories.TouristObjectsCategory']"}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['places.Facilities']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'places.facilities': {
            'Meta': {'object_name': 'Facilities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['choices']