# Generated by Django 2.1.5 on 2019-02-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0007_auto_20190206_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]