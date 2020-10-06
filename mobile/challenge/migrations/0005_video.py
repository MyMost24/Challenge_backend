# Generated by Django 3.0.3 on 2020-10-06 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0004_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='Video File')),
                ('image', models.FileField(null=True, upload_to='images/', verbose_name='Image File')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='challenge.Challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uservideos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]