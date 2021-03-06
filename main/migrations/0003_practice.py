# Generated by Django 3.2.6 on 2021-08-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210824_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=120, verbose_name='Phrase')),
                ('phrase_ru', models.CharField(max_length=120, null=True, verbose_name='Phrase')),
                ('phrase_en', models.CharField(max_length=120, null=True, verbose_name='Phrase')),
                ('phrase_uz', models.CharField(max_length=120, null=True, verbose_name='Phrase')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text1_ru', models.TextField(null=True, verbose_name='Text 1')),
                ('text1_en', models.TextField(null=True, verbose_name='Text 1')),
                ('text1_uz', models.TextField(null=True, verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('text2_ru', models.TextField(null=True, verbose_name='Text 2')),
                ('text2_en', models.TextField(null=True, verbose_name='Text 2')),
                ('text2_uz', models.TextField(null=True, verbose_name='Text 2')),
                ('image1', models.ImageField(upload_to='media/practice', verbose_name='Image 1')),
                ('image2', models.ImageField(upload_to='media/practice', verbose_name='Image 2')),
                ('image3', models.ImageField(upload_to='media/practice', verbose_name='Image 3')),
                ('image4', models.ImageField(upload_to='media/practice', verbose_name='Image 4')),
            ],
        ),
    ]
