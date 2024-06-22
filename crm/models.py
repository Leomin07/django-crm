from django.db import models

from core.enum.enum import CommonStatus


class Todo(models.Model):
    title = models.TextField(
        max_length=255,
    )
    note = models.TextField(max_length=255, blank=True, null=True)
    status = models.BooleanField(
        default=CommonStatus.ACTIVE,
    )
    is_completed = models.BooleanField(default=CommonStatus.INACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["id"]),
            models.Index(fields=["is_completed"]),
        ]
