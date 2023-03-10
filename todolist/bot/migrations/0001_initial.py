# Generated by Django 4.1.5 on 2023-01-13 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='tg id')),
                ('tg_chat_id', models.BigIntegerField(verbose_name='tg chat id')),
                ('username', models.CharField(blank=True, default=None, max_length=512, null=True, verbose_name='tg username')),
                ('verification_code', models.CharField(default='', max_length=32, verbose_name='код подтверждения')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь в системе')),
            ],
            options={
                'verbose_name': 'tg пользователь',
                'verbose_name_plural': 'tg пользователи',
            },
        ),
    ]
