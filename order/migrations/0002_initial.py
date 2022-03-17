# Generated by Django 4.0.2 on 2022-03-17 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('user', '0001_initial'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shipment', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderbookitem',
            name='bookItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookitem'),
        ),
        migrations.AddField(
            model_name='orderbookitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookItems', to='order.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartbookitem',
            name='bookItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookitem'),
        ),
        migrations.AddField(
            model_name='cartbookitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookItems', to='order.cart'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transfer',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transfer', to='order.order'),
        ),
        migrations.AddField(
            model_name='credit',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='order.order'),
        ),
        migrations.AddField(
            model_name='cash',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cash', to='order.order'),
        ),
    ]
