# Generated by Django 2.1.2 on 2019-02-15 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20190214_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(default='patient_profile_pics/defaultPatient.jpg', upload_to='     patient_profile_pics'),
        ),
    ]
