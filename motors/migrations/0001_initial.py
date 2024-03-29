# Generated by Django 4.1.4 on 2023-04-17 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=2000)),
                ('name_en', models.CharField(max_length=2000)),
                ('name_ru', models.CharField(max_length=2000)),
                ('description_uz', models.TextField(max_length=15000)),
                ('description_en', models.TextField(max_length=15000)),
                ('description_ru', models.TextField(max_length=15000)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=2000)),
                ('name_en', models.CharField(max_length=2000)),
                ('name_ru', models.CharField(max_length=2000)),
                ('description_uz', models.TextField(max_length=5000)),
                ('description_en', models.TextField(max_length=5000)),
                ('description_ru', models.TextField(max_length=5000)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.TextField(max_length=5000)),
                ('question_en', models.TextField(max_length=5000)),
                ('question_ru', models.TextField(max_length=5000)),
                ('answer_uz', models.TextField(max_length=5000)),
                ('answer_en', models.TextField(max_length=5000)),
                ('answer_ru', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_uz', models.CharField(max_length=5000)),
                ('description_en', models.CharField(max_length=5000)),
                ('description_ru', models.CharField(max_length=5000)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_uz', models.TextField(max_length=5000)),
                ('description_en', models.TextField(max_length=5000)),
                ('description_ru', models.TextField(max_length=5000)),
                ('video', models.FileField(null=True, upload_to='')),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=2000)),
                ('name_en', models.CharField(max_length=2000)),
                ('name_ru', models.CharField(max_length=2000)),
                ('description_uz', models.TextField(max_length=5000)),
                ('description_en', models.TextField(max_length=5000)),
                ('description_ru', models.TextField(max_length=5000)),
                ('image1', models.FileField(null=True, upload_to='')),
                ('image2', models.FileField(null=True, upload_to='')),
                ('image3', models.FileField(null=True, upload_to='')),
                ('image4', models.FileField(null=True, upload_to='')),
                ('used', models.CharField(choices=[('new', 'new'), ('used', 'used')], max_length=100)),
                ('produced', models.CharField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], max_length=200)),
                ('run', models.FloatField(default=0)),
                ('top', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motors.brand')),
            ],
        ),
    ]
