# Generated by Django 2.1.7 on 2019-04-09 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('upgradeDate', models.DateTimeField(auto_now=True)),
                ('images', models.ImageField(blank='True', upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id',)},
        ),
    ]
