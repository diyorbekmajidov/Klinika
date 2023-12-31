# Generated by Django 4.2.3 on 2023-08-02 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kilinikalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Xizmatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('klinika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xizmatlar', to='klinika.kilinikalar')),
            ],
        ),
        migrations.CreateModel(
            name='Shifokorlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qavat', models.IntegerField()),
                ('info', models.TextField()),
                ('ish_kunlari', models.CharField(max_length=100)),
                ('ish_vaqt', models.CharField(max_length=100)),
                ('img', models.ImageField(default='', upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('xizmatlar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifokorlar', to='klinika.xizmatlar')),
            ],
        ),
        migrations.CreateModel(
            name='Navbatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('shifokor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klinika.shifokorlar')),
                ('xizmat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klinika.xizmatlar')),
            ],
        ),
        migrations.CreateModel(
            name='Narxlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.IntegerField()),
                ('xizmat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='narxlar', to='klinika.xizmatlar')),
            ],
        ),
    ]
