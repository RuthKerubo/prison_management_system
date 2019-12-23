# Generated by Django 3.0 on 2019-12-17 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prisoners', '0002_auto_20191217_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LawyerClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyers.Lawyer')),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisoners.Prisoner')),
            ],
        ),
    ]
