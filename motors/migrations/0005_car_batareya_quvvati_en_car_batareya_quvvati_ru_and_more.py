# Generated by Django 4.2.1 on 2023-07-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0004_blog_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='batareya_quvvati_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='batareya_quvvati_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='batareya_quvvati_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='drayv_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='drayv_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='drayv_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='elektr_dvigateli_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='elektr_dvigateli_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='elektr_dvigateli_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='olchamlari_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='olchamlari_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='olchamlari_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='otirish_hajmi_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='otirish_hajmi_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='otirish_hajmi_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='taxminiy_masofa_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='taxminiy_masofa_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='taxminiy_masofa_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='tezlashuv_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='tezlashuv_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='yuk_tashish_hajmi_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='yuk_tashish_hajmi_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='yuk_tashish_hajmi_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_porti_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_porti_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_porti_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_vaqti_en',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_vaqti_ru',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='zaryadlash_vaqti_uz',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
