from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Session, RoutesCompleted, Achievement, UserAchievement, Route
from django.conf import settings

# @receiver(post_save, sender=RoutesCompleted)
# def handler(sender, instance, **kwargs):
#     print instance.completed
#     if instance.completed:
#         achievement = Achievement.objects.get(route=instance.routeID)
#         UserAchievement.objects.get_or_create(achievementID=achievement,
#                                               userID=instance.userID)

@receiver(post_save, sender=Route)
def handler(sender, instance, **kwargs):
    Achievement.objects.get_or_create(name="{} - Bronze".format(instance.name),
                                      description="{} - Bronze".format(instance.name),
                                      value="B",
                                      metric=(instance.length/settings.BRONZE_SPEED)*1000,
                                      route=instance)
    Achievement.objects.get_or_create(name="{} - Silver".format(instance.name),
                                      description="{} - Bronze".format(instance.name),
                                      value="S",
                                      metric=(instance.length/settings.SILVER_SPEED)*1000,
                                      route=instance)
    Achievement.objects.get_or_create(name="{} - Gold".format(instance.name),
                                      description="{} - Gold".format(instance.name),
                                      value="G",
                                      metric=(instance.length/settings.GOLD_SPEED)*1000,
                                      route=instance)
