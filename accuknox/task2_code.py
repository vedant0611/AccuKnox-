import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()}")

print(f"Main thread: {threading.get_ident()}")
my_instance = MyModel.objects.create(name='Test')
