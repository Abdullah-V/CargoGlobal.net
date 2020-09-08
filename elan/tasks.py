# from celery.schedules import crontab
# from celery.task import periodic_task
# from django.utils import timezone
# from elan.models import elan
# import cronjobs
# @periodic_task(name = 'autopostsil', run_every=crontab(minute='*/5'))
# def autopostsil():
#     # Query all the foos in our database
#     taskelanlar = elan.objects.all()

#     # Iterate through them
#     for birtaskelan in taskelanlar:
#         # If the expiration date is bigger than now delete it
#         if birtaskelan.silinme_vaxti < timezone.now():
#             birtaskelan.delete()
#             # log deletion
#     return "completed deleting foos at {}".format(timezone.now())


# #*/5 * * * * /home/linux/Masaüstü/elansayti/elanvenv/bin/python3 /home/linux/Masaüstü/elansayti/manage.py crontab run b6fa098b0e26160743046261f3fa6abb 


