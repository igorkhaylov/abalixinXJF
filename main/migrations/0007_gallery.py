# Generated by Django 3.2.6 on 2021-08-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_conference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Gallery', max_length=120, verbose_name='Gallery')),
                ('image1', models.ImageField(upload_to='media/gallery/', verbose_name='Image 1')),
                ('image2', models.ImageField(upload_to='media/gallery/', verbose_name='Image 2')),
                ('image3', models.ImageField(upload_to='media/gallery/', verbose_name='Image 3')),
                ('image4', models.ImageField(upload_to='media/gallery/', verbose_name='Image 4')),
                ('image5', models.ImageField(upload_to='media/gallery/', verbose_name='Image 5')),
                ('image6', models.ImageField(upload_to='media/gallery/', verbose_name='Image 6')),
                ('image7', models.ImageField(upload_to='media/gallery/', verbose_name='Image 7')),
                ('image8', models.ImageField(upload_to='media/gallery/', verbose_name='Image 8')),
            ],
        ),
    ]
