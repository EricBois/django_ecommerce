from __future__ import unicode_literals
from django.db import migrations
from payments.models import User
from django.contrib.auth.hashers import make_password


def create_default_user(apps, schema_editor):
	new_user = apps.get_model("payments", "User")
	try:
		burn = new_user.objects.get(email="burn@burn.com")
		burn.delete()
	except new_user.DoesNotExist:
		pass

	u = new_user(
		name='burn', email="burn@burn.com",
		last_4_digits="1234", password= make_password("burn")).save()

class Migration(migrations.Migration):

	dependencies = [
		('payments', '0001_initial'),
	]

	operations = [
		migrations.RunPython(create_default_user)
	]
