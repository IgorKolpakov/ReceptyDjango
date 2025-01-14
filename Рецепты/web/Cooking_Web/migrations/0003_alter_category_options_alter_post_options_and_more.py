

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cooking_Web', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=160, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Cooking_Web.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='Скоро здесь будет статья..', verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_post',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Фото-карточка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_post',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='watched',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Коментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cooking_Web.post', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии ',
            },
        ),
    ]
