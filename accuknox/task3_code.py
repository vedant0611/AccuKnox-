from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executed")
    raise Exception("Error in signal handler")

try:
    with transaction.atomic():
        MyModel.objects.create(name='Test')
except Exception as e:
    print(f"Transaction rolled back due to: {e}")

print(MyModel.objects.all())
