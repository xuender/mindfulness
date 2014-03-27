# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Follow', fields ['create_by', 'user']
        db.delete_unique(u'book_follow', ['create_by_id', 'user_id'])

        # Adding field 'Follow.book'
        db.add_column(u'book_follow', 'book',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='followers', to=orm['book.Book']),
                      keep_default=False)

        # Adding unique constraint on 'Follow', fields ['create_by', 'user', 'book']
        db.create_unique(u'book_follow', ['create_by_id', 'user_id', 'book_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Follow', fields ['create_by', 'user', 'book']
        db.delete_unique(u'book_follow', ['create_by_id', 'user_id', 'book_id'])

        # Deleting field 'Follow.book'
        db.delete_column(u'book_follow', 'book_id')

        # Adding unique constraint on 'Follow', fields ['create_by', 'user']
        db.create_unique(u'book_follow', ['create_by_id', 'user_id'])


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
        'book.annotation': {
            'Meta': {'ordering': "['row', 'start']", 'unique_together': "(('create_by', 'chapter', 'row', 'start', 'end', 'style'),)", 'object_name': 'Annotation'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': "orm['book.Book']"}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': "orm['book.Chapter']"}),
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'end': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '1'})
        },
        'book.bast': {
            'Meta': {'ordering': "['-create_at']", 'unique_together': "(('book', 'author'),)", 'object_name': 'Bast'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'basts'", 'to': u"orm['auth.User']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'basts'", 'to': "orm['book.Book']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'book.chapter': {
            'Meta': {'ordering': "['id']", 'object_name': 'Chapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chapters'", 'to': "orm['book.Book']"}),
            'context': ('django.db.models.fields.TextField', [], {}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'book.employee': {
            'Meta': {'object_name': 'Employee'},
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'book.follow': {
            'Meta': {'ordering': "['-create_at']", 'unique_together': "(('create_by', 'user', 'book'),)", 'object_name': 'Follow'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'followers'", 'to': "orm['book.Book']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'followers'", 'to': u"orm['auth.User']"})
        },
        'book.star': {
            'Meta': {'ordering': "['-create_at']", 'unique_together': "(('create_by', 'book'),)", 'object_name': 'Star'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stars'", 'to': "orm['book.Book']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'create_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'book.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
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