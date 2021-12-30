from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0026_vminterface_bridge'),
        ('extras', '0066_customfield_name_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='configcontext',
            name='cluster_types',
            field=models.ManyToManyField(blank=True, related_name='_extras_configcontext_cluster_types_+', to='virtualization.ClusterType'),
        ),
    ]