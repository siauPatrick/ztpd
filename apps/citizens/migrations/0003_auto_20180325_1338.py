# Generated by Django 2.0.3 on 2018-03-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0002_auto_20180325_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citizen',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='citizen',
            old_name='kind',
            new_name='species',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='first_name',
        ),
        migrations.AddField(
            model_name='citizen',
            name='photo_url',
            field=models.URLField(default='https://vignette.wikia.nocookie.net/zootopia/images/d/d5/NoImage.PNG/revision/latest?cb=20161020234033', max_length=400),
            preserve_default=False,
        ),
    ]
