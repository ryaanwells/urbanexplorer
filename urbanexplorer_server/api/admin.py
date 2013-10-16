from django.contrib import admin
from api.models import UserProfile, Achievement, UserAchievement, Mission, Route, Stage, Progress, RoutesCompleted, Session

admin.site.register(UserProfile)
admin.site.register(Achievement)
admin.site.register(UserAchievement)
admin.site.register(Mission)
admin.site.register(Route)
admin.site.register(Stage)
admin.site.register(Progress)
admin.site.register(RoutesCompleted)
admin.site.register(Session)
