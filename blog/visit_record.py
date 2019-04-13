from django.utils import timezone
from .models import Visit


def record_visit():
    date = timezone.now().date()
    today = Visit.objects.filter(visit_date=date)
    if today:
        temp = today[0]
        count = str(int(temp.count) + 1)
        temp.count = count
    else:
        temp = Visit()
        temp.visit_date = date
        temp.count = 1
    temp.save()