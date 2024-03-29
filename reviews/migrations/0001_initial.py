# Generated by Django 3.0.5 on 2020-05-15 14:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(
                    1), django.core.validators.MaxValueValidator(10)])),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='reviews',
                                   to=settings.AUTH_USER_MODEL)),
                ('review_object',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='reviews',
                                   to='categories.Title')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='comments',
                                   to=settings.AUTH_USER_MODEL)),
                ('review',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='comments',
                                   to='reviews.Review')),
            ],
        ),
    ]
