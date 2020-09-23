# Generated by Django 3.1.1 on 2020-09-04 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areasCurso',
            fields=[
                ('id_area_curso', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre_area_curso', models.CharField(max_length=100)),
                ('descripcion_area_curso', models.TextField(max_length=600)),
                ('id_curso', models.IntegerField()),
                ('nombre_icono', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'areas_de_curso',
                'ordering': ['id_curso'],
            },
        ),
    ]