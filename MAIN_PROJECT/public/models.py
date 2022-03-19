from django.utils.timezone import now
from django.db import models

# Create your models here.


# Announcements from CRs and Admins
class announcements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True) 
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.title



# Weekly and sessional assignments
class assignments(models.Model):
    # subject/course the assignment belongs to
    subject = models.CharField(max_length=200)
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
    subject = models.CharField(max_length=200)
    about = models.TextField()
    # time when the class test will be held
    occurring = models.DateTimeField()
    # class text type field (can be either mcq or written)
    type = models.CharField(max_length=10, choices=CtType.choices, default=CtType.MCQ)
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.about


class helpwewant(models.Model):
    student_id = models.CharField(max_length=7)
    question = models.TextField(max_length=500) 
    answered_by = models.TextField(max_length=15, blank=True)
    asnwer = models.TextField(max_length=500, blank=True)


    def __str__(self) -> str:
        return self.question

    



# class Demo(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.name 