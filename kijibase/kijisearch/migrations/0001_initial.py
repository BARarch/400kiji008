# Generated by Django 2.1.2 on 2018-11-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('course', models.TextField()),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=400)),
                ('zip_code', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=400)),
                ('website', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('grades', models.CharField(max_length=400)),
                ('ages', models.CharField(max_length=400)),
                ('overview', models.TextField()),
                ('time_of_year', models.CharField(max_length=400)),
                ('schedule', models.CharField(max_length=400)),
                ('daily_model', models.CharField(max_length=400)),
                ('focus_areas', models.TextField()),
                ('cost', models.CharField(max_length=400)),
                ('register', models.CharField(max_length=400)),
                ('camp_image_link', models.CharField(max_length=400)),
                ('camp_video_link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=400)),
                ('zip_code', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=400)),
                ('website', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('grades', models.CharField(max_length=400)),
                ('ages', models.CharField(max_length=400)),
                ('overview', models.TextField()),
                ('daily_model', models.CharField(max_length=400)),
                ('time_of_year', models.CharField(max_length=400)),
                ('focus_areas', models.TextField()),
                ('cost', models.CharField(max_length=400)),
                ('eligibility', models.TextField()),
                ('other_locations_of_operation', models.TextField()),
                ('profile_pic_link', models.CharField(max_length=400)),
            ],
        ),
    ]