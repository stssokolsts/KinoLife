# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=120)),
                ('year', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to=b'')),
                ('trailer', models.URLField()),
                ('title_russian', models.CharField(max_length=120)),
                ('title_original', models.CharField(max_length=120)),
                ('url', models.URLField()),
                ('rating_k', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=150)),
                ('photo', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='moviebase',
            name='cast',
            field=models.ManyToManyField(related_name='cast_movie', null=True, to='movie.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moviebase',
            name='country',
            field=models.ManyToManyField(to='movie.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moviebase',
            name='director',
            field=models.ManyToManyField(related_name='director_movie', to='movie.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moviebase',
            name='genre',
            field=models.ManyToManyField(to='movie.Genre', null=True),
            preserve_default=True,
        ),
    ]
