# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'api_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('deviceID', self.gf('django.db.models.fields.CharField')(max_length=128, primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='', max_length=1)),
            ('age', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'api', ['UserProfile'])

        # Adding model 'Stage'
        db.create_table(u'api_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('distance', self.gf('django.db.models.fields.FloatField')()),
            ('nextStage', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='+', unique=True, null=True, to=orm['api.Stage'])),
            ('previousStage', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='+', unique=True, null=True, to=orm['api.Stage'])),
        ))
        db.send_create_signal(u'api', ['Stage'])

        # Adding model 'Mission'
        db.create_table(u'api_mission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'api', ['Mission'])

        # Adding model 'Place'
        db.create_table(u'api_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('mission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Mission'])),
        ))
        db.send_create_signal(u'api', ['Place'])

        # Adding model 'Route'
        db.create_table(u'api_route', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('mission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Mission'])),
            ('startPlace', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['api.Place'])),
            ('endPlace', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['api.Place'])),
            ('startStage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['api.Stage'])),
            ('endStage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['api.Stage'])),
        ))
        db.send_create_signal(u'api', ['Route'])

        # Adding M2M table for field stages on 'Route'
        m2m_table_name = db.shorten_name(u'api_route_stages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('route', models.ForeignKey(orm[u'api.route'], null=False)),
            ('stage', models.ForeignKey(orm[u'api.stage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['route_id', 'stage_id'])

        # Adding model 'Progress'
        db.create_table(u'api_progress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stageID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Stage'])),
            ('userID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.UserProfile'])),
            ('completionDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('totalTime', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('totalDistance', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['Progress'])

        # Adding model 'Session'
        db.create_table(u'api_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.UserProfile'])),
            ('currentProgress', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['api.Progress'])),
            ('distance', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('lastLon', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('lastLat', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('totalTime', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('lastTime', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('excessDistance', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Session'])

        # Adding M2M table for field allProgress on 'Session'
        m2m_table_name = db.shorten_name(u'api_session_allProgress')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('session', models.ForeignKey(orm[u'api.session'], null=False)),
            ('progress', models.ForeignKey(orm[u'api.progress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['session_id', 'progress_id'])

        # Adding model 'Achievement'
        db.create_table(u'api_achievement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('value', self.gf('django.db.models.fields.CharField')(default='B', max_length=1)),
            ('criteria', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'api', ['Achievement'])

        # Adding model 'UserAchievement'
        db.create_table(u'api_userachievement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.UserProfile'])),
            ('achievementID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Achievement'])),
            ('completionDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['UserAchievement'])

        # Adding model 'RoutesCompleted'
        db.create_table(u'api_routescompleted', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('routeID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Route'])),
            ('userID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.UserProfile'])),
            ('completionDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('totalTime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['RoutesCompleted'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'api_userprofile')

        # Deleting model 'Stage'
        db.delete_table(u'api_stage')

        # Deleting model 'Mission'
        db.delete_table(u'api_mission')

        # Deleting model 'Place'
        db.delete_table(u'api_place')

        # Deleting model 'Route'
        db.delete_table(u'api_route')

        # Removing M2M table for field stages on 'Route'
        db.delete_table(db.shorten_name(u'api_route_stages'))

        # Deleting model 'Progress'
        db.delete_table(u'api_progress')

        # Deleting model 'Session'
        db.delete_table(u'api_session')

        # Removing M2M table for field allProgress on 'Session'
        db.delete_table(db.shorten_name(u'api_session_allProgress'))

        # Deleting model 'Achievement'
        db.delete_table(u'api_achievement')

        # Deleting model 'UserAchievement'
        db.delete_table(u'api_userachievement')

        # Deleting model 'RoutesCompleted'
        db.delete_table(u'api_routescompleted')


    models = {
        u'api.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'criteria': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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
            'totalTime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'age': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'deviceID': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
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