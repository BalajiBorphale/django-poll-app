# create_admin.py
from django.contrib.auth.models import User

# --- Set your desired username and password here ---
ADMIN_USERNAME = 'BalajiBorphale'
ADMIN_EMAIL = 'balajiborphale@gmail.com'
ADMIN_PASSWORD = 'Balaji999'
if not User.objects.filter(username=ADMIN_USERNAME).exists():
    print(f'Creating account for {ADMIN_USERNAME}')
    User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
else:
    print('Admin account has already been created.')
