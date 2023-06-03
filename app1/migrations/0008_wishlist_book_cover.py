# Generated by Django 4.2.1 on 2023-06-02 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_wishlist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='book_cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover', to='app1.books'),
        ),
    ]