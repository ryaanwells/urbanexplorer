# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RouteProgress'
        db.create_table(u'api_routeprogress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('progress', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='progress+', null=True, to=orm['api.Progress'])),
            ('time', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['RouteProgress'])

        # Adding M2M table for field allProgress on 'RouteProgress'
        m2m_table_name = db.shorten_name(u'api_routeprogress_allProgress')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('routeprogress', models.ForeignKey(orm[u'api.routeprogress'], null=False)),
            ('progress', models.ForeignKey(orm[u'api.progress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['routeprogress_id', 'progress_id'])

        # Deleting field 'Session.route'
        db.delete_column(u'api_session', 'route_id')

        # Deleting field 'Session.currentProgress'
        db.delete_column(u'api_session', 'currentProgress_id')

        # Adding field 'Session.routesCompleted'
        db.add_column(u'api_session', 'routesCompleted',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.RoutesCompleted'], null=True),
                      keep_default=False)

        # Removing M2M table for field allProgress on 'Session'
        db.delete_table(db.shorten_name(u'api_session_allProgress'))

        # Deleting field 'RoutesCompleted.totalTime'
        db.delete_column(u'api_routescompleted', 'totalTime')

        # Deleting field 'RoutesCompleted.totalDistance'
        db.delete_column(u'api_routescompleted', 'totalDistance')

        # Adding field 'RoutesCompleted.currentJourney'
        db.add_column(u'api_routescompleted', 'currentJourney',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.RouteProgress'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'RoutesCompleted.bestTime'
        db.add_column(u'api_routescompleted', 'bestTime',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding M2M table for field allJourneys on 'RoutesCompleted'
        m2m_table_name = db.shorten_name(u'api_routescompleted_allJourneys')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('routescompleted', models.ForeignKey(orm[u'api.routescompleted'], null=False)),
            ('routeprogress', models.ForeignKey(orm[u'api.routeprogress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['routescompleted_id', 'routeprogress_id'])


    def backwards(self, orm):
        # Deleting model 'RouteProgress'
        db.delete_table(u'api_routeprogress')

        # Removing M2M table for field allProgress on 'RouteProgress'
        db.delete_table(db.shorten_name(u'api_routeprogress_allProgress'))

        # Adding field 'Session.route'
        db.add_column(u'api_session', 'route',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Route'], null=True),
                      keep_default=False)

        # Adding field 'Session.currentProgress'
        db.add_column(u'api_session', 'currentProgress',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', to=orm['api.Progress']),
                      keep_default=False)

        # Deleting field 'Session.routesCompleted'
        db.delete_column(u'api_session', 'routesCompleted_id')

        # Adding M2M table for field allProgress on 'Session'
        m2m_table_name = db.shorten_name(u'api_session_allProgress')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('session', models.ForeignKey(orm[u'api.session'], null=False)),
            ('progress', models.ForeignKey(orm[u'api.progress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['session_id', 'progress_id'])

        # Adding field 'RoutesCompleted.totalTime'
        db.add_column(u'api_routescompleted', 'totalTime',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RoutesCompleted.totalDistance'
        db.add_column(u'api_routescompleted', 'totalDistance',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'RoutesCompleted.currentJourney'
        db.delete_column(u'api_routescompleted', 'currentJourney_id')

        # Deleting field 'RoutesCompleted.bestTime'
        db.delete_column(u'api_routescompleted', 'bestTime')

        # Removing M2M table for field allJourneys on 'RoutesCompleted'
        db.delete_table(db.shorten_name(u'api_routescompleted_allJourneys'))


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
        u'api.routeprogress': {
            'Meta': {'object_name': 'RouteProgress'},
            'allProgress': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'allProgress+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['api.Progress']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'progress+'", 'null': 'True', 'to': u"orm['api.Progress']"}),
            'time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'api.routescompleted': {
            'Meta': {'object_name': 'RoutesCompleted'},
            'allJourneys': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'allJourneys+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['api.RouteProgress']"}),
            'bestTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completionDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'currentJourney': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.RouteProgress']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'routeID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Route']"}),
            'userID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.UserProfile']"})
        },
        u'api.session': {
            'Meta': {'object_name': 'Session'},
            'distance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'excessDistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastLat': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'lastLon': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'lastTime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'routesCompleted': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.RoutesCompleted']", 'null': 'True'}),
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