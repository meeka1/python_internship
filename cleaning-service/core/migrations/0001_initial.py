# Generated by Django 4.0.4 on 2022-05-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_area', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('canceled', 'Canceled'), ('pending', 'Pending')], max_length=15, verbose_name='Request status')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roles_id', models.CharField(choices=[('client', 'Client'), ('company', 'Company')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('cost', models.FloatField()),
                ('company', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('feedback', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('request_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.request')),
                ('service_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.service')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='status_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.requeststatus'),
        ),
        migrations.AddField(
            model_name='request',
            name='total_cost',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.service'),
        ),
        migrations.AddField(
            model_name='request',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]