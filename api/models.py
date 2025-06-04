import uuid
from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    last_update = models.DateTimeField(auto_now=True)
    create_on = models.DateTimeField(auto_now_add=True)

class Notes(models.Model):
    note_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    note_title = models.CharField(max_length=200)
    note_content = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
