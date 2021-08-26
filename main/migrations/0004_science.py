# Generated by Django 3.2.6 on 2021-08-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_practice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_list', models.CharField(max_length=120, verbose_name='One list')),
                ('one_list_ru', models.CharField(max_length=120, null=True, verbose_name='One list')),
                ('one_list_en', models.CharField(max_length=120, null=True, verbose_name='One list')),
                ('one_list_uz', models.CharField(max_length=120, null=True, verbose_name='One list')),
                ('image', models.ImageField(upload_to='media/science', verbose_name='Image')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text1_ru', models.TextField(null=True, verbose_name='Text 1')),
                ('text1_en', models.TextField(null=True, verbose_name='Text 1')),
                ('text1_uz', models.TextField(null=True, verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('text2_ru', models.TextField(null=True, verbose_name='Text 2')),
                ('text2_en', models.TextField(null=True, verbose_name='Text 2')),
                ('text2_uz', models.TextField(null=True, verbose_name='Text 2')),
            ],
        ),
    ]
