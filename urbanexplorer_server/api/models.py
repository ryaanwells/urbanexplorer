import os
import sys
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

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
    class Meta:
        verbose_name = "achievement"
        verbose_name_plural = "achievements"

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
    class Meta:
        verbose_name = "user achievement"
        verbose_name_plural = "user achievements"

    userID = models.ForeignKey(User)
    achievementID = models.ForeignKey('Achievement')
    completionDate = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.userID

class Mission(models.Model):
    class Meta:
        verbose_name = "mission"
        verbose_name_plural = "missions"

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name

class Place(models.Model):
    class Meta:
        verbose_name = "place"
        verbose_name_plural = "places"

    name = models.CharField(max_length=128)
    mission = models.ForeignKey('Mission')

    def __unicode__(self):
        return self.name

class Route(models.Model):
    class Meta:
        verbose_name = "route"
        verbose_name_plural = "routes"

    name = models.CharField(max_length=128)
    mission = models.ForeignKey('Mission')
    startPlace = models.ForeignKey('Place', related_name='+')
    endPlace = models.ForeignKey('Place', related_name='+')
    startStage = models.ForeignKey('Stage', related_name='+')
    endStage = models.ForeignKey('Stage', related_name='+')
    # Also geolocation here, implementation TBD.
    # Interesting: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/

    def __unicode__(self):
        return self.name

class Stage(models.Model):
    class Meta:
        verbose_name = "stage"
        verbose_name_plural = "stages"

    name = models.CharField(max_length=128)
    distance = models.FloatField()
    nextStage = models.OneToOneField('Stage', blank=True, null=True, related_name='+')
    previousStage = models.OneToOneField('Stage', blank=True, null=True, related_name='+')
    # Also geolocation here, implementation TBD.
    # Interesting: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/

    def __unicode__(self):
        return self.name

class Progress(models.Model):
    class Meta:
        verbose_name = "progress"
        verbose_name_plural = "progressions"

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
    class Meta:
        verbose_name = "route completed"
        verbose_name_plural = "routes completed"

    routeID = models.ForeignKey('Route')
    userID = models.ForeignKey(User)
    completionDate = models.DateField(blank=True, null=True)
    totalTime = models.TimeField(blank=True, null=True)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.routeID

class Session(models.Model):
    class Meta:
        verbose_name = "sessions"
        verbose_name_plural = "sessions"

    userID = models.ForeignKey(User)
    distance = models.PositiveIntegerField(blank=True, null=True)
    maxSpeed = models.PositiveIntegerField(blank=True, null=True)
    totalTime = models.TimeField(blank=True, null=True)

    def __unicode__(self):
        return self.userID
