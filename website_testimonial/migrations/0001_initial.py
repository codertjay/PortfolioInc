# Generated by Django 3.2.8 on 2021-10-22 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField(blank=True, null=True)),
                ('detail', models.CharField(max_length=200)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.website')),
            ],
        ),
    ]
