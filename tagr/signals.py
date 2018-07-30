from django.dispatch import receiver
from django.core.signals import post_save
from accounts.models import UserModel
from post.models import Post


@receiver(post_save, sender=UserModel)
def ensure_profile_exists(sender, **kwargs):
	if kwargs.get('created', False):
		Post.objects.get_or_create(user=kwargs.get('instance'), question='This is a Question')