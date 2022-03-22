# Generated by Django 4.0.2 on 2022-03-19 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices', models.FloatField(default=0)),
                ('description', models.TextField(max_length=8191)),
                ('header', models.TextField(max_length=1023)),
                ('discount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MobileDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=511)),
                ('batteryCapacity', models.CharField(max_length=255)),
                ('warrantyDuration', models.CharField(max_length=255)),
                ('warrantyType', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('screenSize', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.brand')),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhoneItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices', models.FloatField(default=0)),
                ('description', models.TextField(max_length=8191)),
                ('header', models.TextField(max_length=1023)),
                ('discount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('mobiledevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.mobiledevice')),
                ('laptopType', models.CharField(max_length=255)),
                ('storageType', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
            ],
            bases=('electronic.mobiledevice',),
        ),
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('mobiledevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.mobiledevice')),
                ('processorType', models.CharField(max_length=255)),
                ('storageCapacity', models.CharField(max_length=255)),
                ('mobileCableType', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
            ],
            bases=('electronic.mobiledevice',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('mobiledevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.mobiledevice')),
                ('eReader', models.BooleanField(default=False)),
                ('storageCapacity', models.CharField(max_length=255)),
            ],
            bases=('electronic.mobiledevice',),
        ),
        migrations.CreateModel(
            name='SmartPhoneItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/smartphone_item_images/')),
                ('smartPhoneItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.smartphoneitem')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/laptop_item_images/')),
                ('laptopItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.laptopitem')),
            ],
        ),
        migrations.CreateModel(
            name='TabletItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/tablet_item_images/')),
                ('tabletItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.tablet')),
            ],
        ),
        migrations.CreateModel(
            name='TabletItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices', models.FloatField(default=0)),
                ('description', models.TextField(max_length=8191)),
                ('header', models.TextField(max_length=1023)),
                ('discount', models.FloatField(default=0)),
                ('tablet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electronic.tablet')),
            ],
        ),
        migrations.AddField(
            model_name='smartphoneitem',
            name='smartPhone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electronic.smartphone'),
        ),
        migrations.AddField(
            model_name='laptopitem',
            name='laptop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electronic.laptop'),
        ),
    ]
