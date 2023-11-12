from django.db import models
from django.contrib.auth.models import User


def profile_avatars_directory_path(instance: 'Profile', filename: str) -> str:
    return 'profiles/avatars/{pk}/{filename}'.format(
        pk=instance.profile.pk,
        filename=filename,
    )


class Avatar(models.Model):
    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'
        ordering = ['pk']

    profile = models.OneToOneField('Profile', verbose_name='avatar', on_delete=models.CASCADE)
    image = models.FileField(upload_to=profile_avatars_directory_path)

    def __str__(self):
        return f'{self.profile.user.username} avatar'

    def src(self):
        return f"/media/{self.image}"

    def alt(self):
        return f"{self.profile.user.username}_avatar"


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['pk']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False, blank=True, default='')
    fullName = models.CharField(max_length=256, null=False, blank=True, default='')
    email = models.EmailField(max_length=128, null=False, blank=True, default='')

    def __str__(self):
        return self.user.username
