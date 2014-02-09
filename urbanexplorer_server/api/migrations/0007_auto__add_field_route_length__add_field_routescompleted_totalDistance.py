# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Route.length'
        db.add_column(u'api_route', 'length',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RoutesCompleted.totalDistance'
        db.add_column(u'api_routescompleted', 'totalDistance',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Route.length'
        db.delete_column(u'api_route', 'length')

        # Deleting field 'RoutesCompleted.totalDistance'
        db.delete_column(u'api_routescompleted', 'totalDistance')


    models = {
        u'api.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Route']", 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'B'", 'max_length': '1'})
        },
        u'api.mission': {
            'Meta': {'object_name': 'Mission'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'api.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Mission']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'api.progress': {
            'Meta': {'object_name': 'Progress'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completionDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stageID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Stage']"}),
            'totalDistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'totalTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'userID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.UserProfile']"})
        },
        u'api.route': {
            'Meta': {'object_name': 'Route'},
            'endPlace': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['api.Place']"}),
            'endStage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['api.Stage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Mission']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'stages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Stage']", 'symmetrical': 'False'}),
            'startPlace': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['api.Place']"}),
            'startStage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['api.Stage']"})
        },
        u'api.routescompleted': {
            'Meta': {'object_name': 'RoutesCompleted'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completionDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'routeID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Route']"}),
            'totalDistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'totalTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'userID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.UserProfile']"})
        },
        u'api.session': {
            'Meta': {'object_name': 'Session'},
            'allProgress': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['api.Progress']"}),
            'currentProgress': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['api.Progress']"}),
            'distance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'excessDistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastLat': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'lastLon': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'lastTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Route']", 'null': 'True'}),
            'totalTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'userID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.UserProfile']"})
        },
        u'api.stage': {
            'Meta': {'object_name': 'Stage'},
            'distance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nextStage': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'+'", 'unique': 'True', 'null': 'True', 'to': u"orm['api.Stage']"}),
            'previousStage': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'+'", 'unique': 'True', 'null': 'True', 'to': u"orm['api.Stage']"})
        },
        u'api.userachievement': {
            'Meta': {'object_name': 'UserAchievement'},
            'achievementID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Achievement']"}),
            'completionDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.UserProfile']"})
        },
        u'api.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'age': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'deviceID': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'totalDistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'totalTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']