# Generated by Django 4.0.4 on 2022-05-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_requeststatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeststatus',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('canceled', 'Canceled'), ('pending', 'Pending')], max_length=15, verbose_name='Request status'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='roles_id',
            field=models.CharField(choices=[('company', 'Company'), ('client', 'Client')], max_length=20),
        ),
    ]
