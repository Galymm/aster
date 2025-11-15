# from django.db.models.signals import post_migrate
# from django.contrib.auth.models import Group, Permission
# from django.dispatch import receiver
# from django.apps import apps
#
# @receiver(post_migrate)
# def create_default_groups(sender, **kwargs):
#     if sender.label != 'cards':
#         return
#
#     editor_group, _ = Group.objects.get_or_create(name='Editor')
#     reader_group, _ = Group.objects.get_or_create(name='Reader')
#
#     Card = apps.get_model('cards', 'Card')
#     Category = apps.get_model('cards', 'Category')
#
#     # Все разрешения для карточек и категорий → редактор
#     editor_permissions = Permission.objects.filter(
#         content_type__app_label='cards',
#         content_type__model__in ['card', 'category']
#     )
#
#     editor_group.permissions.set(editor_permissions)
#
#     # Читателю пока ничего не даём (только читать, без действий)
#     reader_group.permissions.clear()
