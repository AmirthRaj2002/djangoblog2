# Generated by Django 4.0.3 on 2022-03-29 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_alter_post_author_alter_post_title_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.author'),
        ),
    ]
