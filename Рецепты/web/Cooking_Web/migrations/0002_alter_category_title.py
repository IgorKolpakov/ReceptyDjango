

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cooking_Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=160, unique=True),
        ),
    ]
