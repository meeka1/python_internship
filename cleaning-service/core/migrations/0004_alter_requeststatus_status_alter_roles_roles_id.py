# Generated by Django 4.0.4 on 2022-05-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_requeststatus_status_alter_roles_roles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeststatus',
            name='status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('pending', 'Pending'), ('completed', 'Completed')], max_length=15, verbose_name='Request status'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='roles_id',
            field=models.CharField(choices=[('client', 'Client'), ('company', 'Company')], max_length=20),
        ),
    ]
