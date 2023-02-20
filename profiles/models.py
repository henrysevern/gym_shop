# from django.db import models
# from django.contib.auth.models import User
# Create your models here.


# class UserProfile(models.Model):

#     """
#     A user profile model for maintaining default
#     delivery information and order history
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,
#                               null=True)
#     default_address = models.CharField(max_length=200, null=True, blank=True)
#     default_city = models.CharField(max_length=200, null=True, blank=True)
#     default_county = models.CharField(max_length=200, null=True, blank=True)
#     default_postcode = models.CharField(max_length=200, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         UserProfile.objects.create(user=instance)
#     # Existing users: just save the profile
#     instance.userprofile.save()
