import os
import sys
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('', 'None'),
    )
    user = models.OneToOneField(User)
    deviceID = models.CharField(max_length=128, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='')
    age = models.DateField(null=True)

    def __unicode__(self):
        return self.deviceID

class Achievement(models.Model):
    LEVEL = (
        ('G', 'Gold'),
        ('S', 'Silver'),
        ('B', 'Bronze'),
    )
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    value = models.CharField(max_length=1, choices=LEVEL, default='B')
    criteria = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name

class UserAchievement(models.Model):
    userID = models.ForeignKey(User)
    achievementID = models.ForeignKey('Achievement')
    completionDate = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.userID

class Mission(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=128)
    mission = models.ForeignKey('Mission')
    startConnections = models.ManyToManyField('Route', related_name='start+', null=True, blank=True)
    endConnections = models.ManyToManyField('Route', related_name='end+', null=True, blank=True)
    startStage = models.ForeignKey('Stage', related_name='+')
    endStage = models.ForeignKey('Stage', related_name='+')
    # Also geolocation here, implementation TBD.
    # Interesting: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/

    def __unicode__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=128)
    distance = models.FloatField()
    nextStage = models.OneToOneField('Stage', blank=True, null=True, related_name='+')
    previousStage = models.OneToOneField('Stage', blank=True, null=True, related_name='+')
    # Also geolocation here, implementation TBD.
    # Interesting: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/

    def __unicode__(self):
        return self.name

class Progress(models.Model):
    stageID = models.ForeignKey('Stage')
    userID = models.ForeignKey(User)
    completionDate = models.DateField(blank=True, null=True)
    # total time and distance so far
    totalTime = models.TimeField(blank=True, null=True)
    totalDistance = models.PositiveIntegerField(blank=True, null=True)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.userID

class RoutesCompleted(models.Model):
    routeID = models.ForeignKey('Route')
    userID = models.ForeignKey(User)
    completionDate = models.DateField(blank=True, null=True)
    totalTime = models.TimeField(blank=True, null=True)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.routeID

class Session(models.Model):
    userID = models.ForeignKey(User)
    distance = models.PositiveIntegerField(blank=True, null=True)
    averageSpeed = models.PositiveIntegerField(blank=True, null=True)
    maxSpeed = models.PositiveIntegerField(blank=True, null=True)
    totalTime = models.TimeField(blank=True, null=True)

    def __unicode__(self):
        return self.userID
