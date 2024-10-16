# Generated by Django 5.1.2 on 2024-10-10 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('status', models.CharField(default='Available', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservationId', models.AutoField(primary_key=True, serialize=False)),
                ('reservationDate', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loanId', models.AutoField(primary_key=True, serialize=False)),
                ('loanDate', models.DateField()),
                ('returnDate', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
        migrations.AddField(
            model_name='user',
            name='booksList',
            field=models.ManyToManyField(through='todo.UserBook', to='todo.book'),
        ),
    ]
