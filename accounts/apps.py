from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals


def create_roles():
    from django.contrib.auth.models import Group, Permission
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    mod_group, _ = Group.objects.get_or_create(name='Moderator')
    perms = Permission.objects.filter(codename__in=['add_post', 'change_post', 'delete_post'])
    admin_group.permissions.set(perms)
