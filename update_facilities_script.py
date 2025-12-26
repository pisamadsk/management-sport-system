import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from ucasports.models import Facility

def update_facilities():
    # Update Padel
    try:
        padel = Facility.objects.get(name="Padel")
        padel.name = "Padel Court 1"
        padel.save()
        print("Renamed 'Padel' to 'Padel Court 1'")
    except Facility.DoesNotExist:
        if not Facility.objects.filter(name="Padel Court 1").exists():
            Facility.objects.create(name="Padel Court 1")
            print("Created 'Padel Court 1'")

    if not Facility.objects.filter(name="Padel Court 2").exists():
        Facility.objects.create(name="Padel Court 2")
        print("Created 'Padel Court 2'")
    
    if not Facility.objects.filter(name="Padel Court 3").exists():
        Facility.objects.create(name="Padel Court 3")
        print("Created 'Padel Court 3'")

    # Update Football
    try:
        football = Facility.objects.get(name="Football")
        football.name = "Football Field 1"
        football.save()
        print("Renamed 'Football' to 'Football Field 1'")
    except Facility.DoesNotExist:
        if not Facility.objects.filter(name="Football Field 1").exists():
            Facility.objects.create(name="Football Field 1")
            print("Created 'Football Field 1'")

    if not Facility.objects.filter(name="Football Field 2").exists():
        Facility.objects.create(name="Football Field 2")
        print("Created 'Football Field 2'")
    
    if not Facility.objects.filter(name="Football Field 3").exists():
        Facility.objects.create(name="Football Field 3")
        print("Created 'Football Field 3'")

    # Ensure others exist
    if not Facility.objects.filter(name="Musculation").exists():
        Facility.objects.create(name="Musculation")
        print("Created 'Musculation'")

    if not Facility.objects.filter(name="Fitness").exists():
        Facility.objects.create(name="Fitness")
        print("Created 'Fitness'")

if __name__ == "__main__":
    update_facilities()
