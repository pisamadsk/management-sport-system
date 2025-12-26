import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from ucasports.models import Facility

facilities = ["Padel", "Football", "Musculation", "Fitness"]
for name in facilities:
    obj, created = Facility.objects.get_or_create(name=name)
    if created:
        print(f"Created facility: {name}")
    else:
        print(f"Facility already exists: {name}")
