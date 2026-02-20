import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sms_project.settings")
django.setup()
from django.template import Context, Template
from datetime import time

t1 = time(11, 9)
t2 = time(0, 9)
t3 = time(13, 5)

tpl = Template("{{ t1|time:'h:i A' }} , {{ t2|time:'h:i A' }} , {{ t3|time:'h:i A' }}")
print("With time filter:", tpl.render(Context({'t1': t1, 't2': t2, 't3': t3})))

tpl2 = Template("{{ t1|date:'h:i A' }} , {{ t2|date:'h:i A' }} , {{ t3|date:'h:i A' }}")
print("With date filter:", tpl2.render(Context({'t1': t1, 't2': t2, 't3': t3})))
