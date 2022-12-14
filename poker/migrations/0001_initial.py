# Generated by Django 4.1.3 on 2022-11-13 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_denomination', models.IntegerField(choices=[(0, 'Two'), (1, 'Three'), (2, 'Four'), (3, 'Five'), (4, 'Six'), (5, 'Seven'), (6, 'Eight'), (7, 'Nine'), (8, 'Ten'), (9, 'Jack'), (10, 'Quin'), (11, 'King'), (12, 'Ace')])),
                ('card_suit', models.IntegerField(choices=[(0, 'Heart'), (1, 'Diamond'), (2, 'Cross'), (3, 'Spade')])),
            ],
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_at', models.DateTimeField(auto_now=True)),
                ('hand_num', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField()),
                ('small_blind', models.PositiveIntegerField()),
                ('big_blind', models.PositiveIntegerField()),
                ('min_limit', models.PositiveIntegerField()),
                ('max_limit', models.PositiveIntegerField()),
                ('ante', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField(choices=[(0, 'Bet'), (1, 'Fold')])),
                ('bet', models.IntegerField(blank=True, null=True)),
                ('card1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='poker.card')),
                ('hand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poker.hand')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('buy_in', models.PositiveIntegerField()),
                ('chips', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flop',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='poker.order')),
            ],
            bases=('poker.order',),
        ),
        migrations.CreateModel(
            name='PreFlop',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='poker.order')),
            ],
            bases=('poker.order',),
        ),
        migrations.CreateModel(
            name='River',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='poker.order')),
            ],
            bases=('poker.order',),
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='poker.order')),
            ],
            bases=('poker.order',),
        ),
        migrations.CreateModel(
            name='Struct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('level', models.ManyToManyField(to='poker.level')),
            ],
        ),
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_level_hands', models.PositiveIntegerField()),
                ('struct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poker.struct')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poker.table')),
            ],
        ),
    ]
