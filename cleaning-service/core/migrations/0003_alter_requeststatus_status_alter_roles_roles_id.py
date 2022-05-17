# Generated by Django 4.0.4 on 2022-05-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_request_status_id_alter_request_total_cost_and_more'),
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