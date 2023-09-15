# Generated by Django 4.2.3 on 2023-08-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('SF', 'SlimFitPants'), ('LJ', 'LycraJeans'), ('OT', 'OversizedTee'), ('KP', 'HighwaistKoreanPant'), ('PS', 'PulloverSweater'), ('CT', 'Croptop'), ('AK', 'Anarkali'), ('SH', 'Shara'), ('SL', 'Salwar'), ('KT', 'Kurta'), ('KI', 'Kurti'), ('MS', 'MysoreSilk'), ('KS', 'KanchipuramSilks'), ('BS', 'BanarasSilks'), ('LS', 'Lehenga'), ('SS', 'SoftSilk'), ('CW', 'CasualWatch'), ('FW', 'FormalWatch'), ('EW', 'EthnicWatch'), ('SW', 'SportWatch'), ('JB', 'JuteHandbag'), ('EB', 'EcofriendlyBag'), ('WP', 'WaterproofBag'), ('EM', 'EmbroidedBag'), ('AV', 'Aviater'), ('RD', 'Round'), ('SQ', 'Square'), ('WF', 'Wayfarer'), ('BH', 'Blockheels'), ('FL', 'Flats'), ('CR', 'Crocswomen'), ('RS', 'RegularSandals'), ('BL', 'Ballerian')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]