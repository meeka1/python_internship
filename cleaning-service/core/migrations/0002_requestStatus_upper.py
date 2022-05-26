from django.db import migrations

class Migration(migrations.Migration):

    def custom_task(self, schema_editor):
        RequestStatus = self.get_model("core", "RequestStatus")
        for rs in RequestStatus.objects.all():
            rs.status = rs.status.upper()
            rs.save()

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(custom_task, migrations.RunPython.noop)
    ]
