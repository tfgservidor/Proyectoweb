# Generated by Django 4.0.4 on 2022-05-03 18:33

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recomendaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacion',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]