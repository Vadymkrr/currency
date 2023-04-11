from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def format_phone_number(sender, instance, **kwargs):
    if instance.phone:
        phone = ''.join(instance.phone)
        phone = f'({phone[:3]})-{phone[3:6]}-{phone[6:8]}-{phone[8:]}'
        instance.phone = phone
