import os
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from .models import Project, Image


@receiver(post_delete, sender=Project)
def delete_thumbnail(sender, instance, *args, **kwargs):
    """Clean deleted project image."""
    try:
        instance.thumbnail.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Project)
def update_thumbnail(sender, instance, *args, **kwargs):
    """Delete old image when Project if updated if it applies."""
    try:
        old_image = Project.objects.get(
            id=instance.id).thumbnail.path

        try:
            new_image = instance.thumbnail.path
        except:
            new_image = None
            return False

        if old_image != new_image:
            import os
            if os.path.exists(old_image):
                os.remove(old_image)

    except:
        pass


@receiver(post_delete, sender=Image)
def delete_project_image(sender, instance, *args, **kwargs):
    """Delete project images from Image model."""
    try:
        instance.url.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Image)
def update_project_image(sender, instance, *args, **kwargs):
    """Delete old image when Project if updated if it applies."""
    try:
        old_image = Image.objects.get(
            id=instance.id).url.path

        try:
            new_image = instance.url.path
        except:
            new_image = None
            return False

        if old_image != new_image:
            import os
            if os.path.exists(old_image):
                os.remove(old_image)

    except:
        pass
