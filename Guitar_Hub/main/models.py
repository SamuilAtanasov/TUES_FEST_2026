from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # NEW: parent message (null for top-level posts)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username}: {self.text[:30]}"

    class Meta:
        permissions = [
            ("can_moderate", "Can moderate forum messages"),
        ]
