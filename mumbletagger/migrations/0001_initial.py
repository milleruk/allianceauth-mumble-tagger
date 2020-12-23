# Generated by Django 3.1.1 on 2020-12-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=150)),
                ('enabled', models.BooleanField()),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
        ),
    ]