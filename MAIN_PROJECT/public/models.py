from django.utils.timezone import now
from django.db import models

# Create your models here.


# Announcements from CRs and Admins
class announcements(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.title


# Weekly and sessional assignments
class assignments(models.Model):
    # subject/course the assignment belongs to
    subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    # time before the assignment should/must be submitted
    due = models.DateTimeField()
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.title


class class_tests(models.Model):
    # Class test types enum
    class CtType(models.enums.Choices):
        MCQ = "mcq"
        WRITTEN = "written"

    # subject/course the class test belongs to
    subject = models.CharField(max_length=255)
    about = models.TextField()
    # time when the class test will be held
    occurring = models.DateTimeField()
    # class text type field (can be either mcq or written)
    type = models.CharField(max_length=10, choices=CtType.choices, default=CtType.MCQ)
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.about

