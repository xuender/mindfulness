# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Volume'
        db.delete_table(u'book_volume')

        # Adding model 'Chapter'
        db.create_table(u'book_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('create_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('modify_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modify_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'book', ['Chapter'])


    def backwards(self, orm):
        # Adding model 'Volume'
        db.create_table(u'book_volume', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('modify_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('modify_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'book', ['Volume'])

        # Deleting model 'Chapter'
        db.delete_table(u'book_chapter')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'book.chapter': {
            'Meta': {'ordering': "['id']", 'object_name': 'Chapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['book']