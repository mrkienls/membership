# Generated by Django 2.2.7 on 2019-12-02 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('user_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberships.UserMembership')),
            ],
        ),
    ]
