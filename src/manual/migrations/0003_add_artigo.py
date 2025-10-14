from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0002_alter_comando_comando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('arquivo', models.FileField(upload_to='artigos/')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artigos', to='manual.secao')),
            ],
        ),
    ]
