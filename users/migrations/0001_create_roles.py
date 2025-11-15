from django.db import migrations

def create_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    roles = ["Reader", "Editor"]

    for role in roles:
        Group.objects.get_or_create(name=role)

def delete_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=["Reader", "Editor"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_roles, delete_roles),
    ]
