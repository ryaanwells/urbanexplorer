from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Session, RoutesCompleted, Achievement, UserAchievement

# @receiver(post_save, sender=RoutesCompleted)
# def handler(sender, instance, **kwargs):
#     print instance.completed
#     if instance.completed:
#         achievement = Achievement.objects.get(route=instance.routeID)
#         UserAchievement.objects.get_or_create(achievementID=achievement,
#                                               userID=instance.userID)

        
