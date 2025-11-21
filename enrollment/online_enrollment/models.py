from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"


class Subjects(models.Model):
    no_of_units = models.IntegerField()
    department = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.no_of_units} {self.department} {self.sub_title} {self.sub_code} {self.time}"


class Course(models.Model):
    course_id = models.IntegerField()
    course_subject= models.CharField(max_length=100)
    units = models.IntegerField()
    description = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_id} {self.course_subject} {self.units} {self.description} {self.department}"

class Grades(models.Model):
    Grade_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    course_taken = models.CharField(max_length=100)
    grade = models.IntegerField()
    remark = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Grade_id} {self.student_name} {self.course_taken} {self.grade} {self.remark}"

class Notification(models.Model):
    notification_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.notification_id} {self.student_name} {self.message} {self.date_sent} {self.status}"

class Attendance(models.Model):
    attendance_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attendance_id} {self.student_name} {self.subject} {self.date} {self.status}"


