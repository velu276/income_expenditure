# Generated by Django 3.1.5 on 2021-03-15 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenditureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenditure_type', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_source', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('source_account', models.BigIntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('granted_by', models.CharField(max_length=100)),
                ('receipt', models.ImageField(upload_to='iemodule/income_receipts')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomesource', to='IncomeExpenditure.incomesource')),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('granted_to', models.CharField(max_length=100)),
                ('expenditure_receipt', models.ImageField(upload_to='iemodule/expenditure_receipts')),
                ('spent_on', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expendituretype', to='IncomeExpenditure.expendituretype')),
            ],
        ),
    ]
