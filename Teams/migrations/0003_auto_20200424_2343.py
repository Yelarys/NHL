# Generated by Django 3.0.5 on 2020-04-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0002_auto_20200424_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='conference/', verbose_name='Логотип')),
                ('stars', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(upload_to='players/', verbose_name='Изображение'),
        ),
    ]
