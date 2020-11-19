from django.db import models
#
# class Parent(models):
#     local_parent = models.CharField(max_length=255,null=False)
#     out_door_parent = models.CharField(max_length=255,null=False)
#     # Option for the parent
#     address = models.CharField(max_length=255,null=False)
#     email_address = models.CharField(max_length=255, null=False)
#     phone_number = models.CharField(max_length=255,null=False)
#
# class Subject(models):
#     name = models.CharField(max_length=255)
#     registered_date = models.DateTimeField()
#

class Speaker(models):
    name = models.CharField(max_length=255)

class Category(models):
    name = models.CharField(max_length=255)

class Event(models):
    title = models.CharField(max_length=255)
    featured = models.BooleanField(max_length=255)
    image = models.ImageField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


