# Generated by Django 4.1.4 on 2022-12-20 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField(verbose_name='ID уровня школы')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='Последняя правка')),
                ('text', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Формулировка')),
                ('number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер')),
                ('tabler', models.IntegerField(blank=True, null=True, verbose_name='Шапка/Альтернатива')),
                ('min_range', models.IntegerField(blank=True, null=True, verbose_name='Минимум')),
                ('max_range', models.IntegerField(blank=True, null=True, verbose_name='Максимум')),
                ('min_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название минимума')),
                ('max_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название максимума')),
                ('related_question', models.CharField(blank=True, max_length=11, null=True, verbose_name='связанный вопрос')),
            ],
            options={
                'verbose_name': 'Альтернатива',
                'verbose_name_plural': 'Альтернативы',
                'db_table': 'alternative',
            },
        ),
        migrations.CreateModel(
            name='PartTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField(verbose_name='ID уровня школы')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='Последняя правка')),
                ('target_n_quest', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Сколько вопросов показывать')),
                ('method_of_sel', models.IntegerField(choices=[(1, 'По порядку'), (2, 'Случайным образом')], default=1, verbose_name='Как выбрать нужное кол-во вопросов')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст части')),
                ('number', models.IntegerField(default=0, verbose_name='Номер части')),
                ('name', models.CharField(max_length=100, verbose_name='Название части')),
            ],
            options={
                'verbose_name': 'Часть теста',
                'verbose_name_plural': 'Части теста',
                'db_table': 'part_test',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название типа вопроса')),
                ('function', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название типа вопроса')),
            ],
            options={
                'verbose_name': 'Тип вопроса',
                'verbose_name_plural': 'Типы вопроса',
                'db_table': 'type_questions',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField(verbose_name='ID уровня школы')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='Последняя правка')),
                ('name', models.CharField(max_length=100, verbose_name='Название методики')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание методики')),
                ('type_test', models.SmallIntegerField(choices=[(1, 'Опрос учащегося'), (2, 'Опрос педагогов')], default=1, verbose_name='Тип опроса')),
                ('anonymus', models.SmallIntegerField(choices=[(0, 'Не анонимный'), (1, 'Анонимный'), (2, 'Конфиденциальный')], default=0, verbose_name='Анонимность')),
                ('added_by_ou', models.BooleanField(default=True, verbose_name='Добавлено ОУ')),
                ('variant', models.ManyToManyField(to='polls.test', verbose_name='Вариант')),
            ],
            options={
                'verbose_name': 'Психологический тест',
                'verbose_name_plural': 'Психологические тесты',
                'db_table': 'test',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField(verbose_name='ID уровня школы')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='Последняя правка')),
                ('method', models.IntegerField(blank=True, null=True, verbose_name='Бывший фореигн на тест')),
                ('min_ball', models.IntegerField(default=0, verbose_name='Минимальный балл')),
                ('max_ball', models.IntegerField(default=0, verbose_name='Максимальный балл')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Формулировка вопроса')),
                ('number', models.CharField(max_length=11, verbose_name='Номер вопроса (как в спецификации)')),
                ('is_table', models.BooleanField(default=False, verbose_name='В виде таблицы?')),
                ('on_graph', models.BooleanField(default=False, verbose_name='Учитывать при построения графика?')),
                ('manually', models.BooleanField(default=False, verbose_name='Оценивать вручную?')),
                ('required', models.BooleanField(default=False, verbose_name='Обязательный для заполнения?')),
                ('related_question', models.CharField(blank=True, max_length=11, null=True, verbose_name='связанный вопрос')),
                ('part_test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.parttest', verbose_name='Часть теста')),
                ('type_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.questiontype', verbose_name='Тип вопроса')),
            ],
            options={
                'verbose_name': 'Ворпос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'question',
            },
        ),
        migrations.AddField(
            model_name='parttest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='ASIOU_PSY_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField(verbose_name='ИД уровня школы')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='Последняя правка')),
                ('value', models.CharField(blank=True, max_length=6000, null=True, verbose_name='Ответ')),
                ('open_ans', models.CharField(blank=True, max_length=6000, null=True, verbose_name='Ответ на открытый вопрос')),
                ('available_to_upload', models.BooleanField(blank=True, default=False, verbose_name='Разрешить выгрузку в ЦОиККО')),
                ('alternative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.alternative', verbose_name='Альтарнатива')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
                'db_table': 'asiou_psy_answer',
            },
        ),
        migrations.AddField(
            model_name='alternative',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Вопрос'),
        ),
    ]