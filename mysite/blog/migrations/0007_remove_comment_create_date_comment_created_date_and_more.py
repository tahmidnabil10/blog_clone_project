# Generated by Django 4.1 on 2023-01-05 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="create_date",),
        migrations.AddField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 5, 2, 3, 5, 857248, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 5, 2, 3, 5, 857248, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
