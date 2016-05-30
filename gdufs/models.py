# coding=utf-8
from django.db import models

# Create your models here.


class Person(models.Model):
    """
    用来存储登录学生的详细信息
    """
    name = models.CharField(max_length=10)  # 学生姓名
    ID_number = models.CharField(max_length=11)  # 学号
    password = models.CharField(max_length=20)  # 登录密码

    def __unicode__(self):
        return self.name


class Email(models.Model):
    """
    用来存储每封邮件的详细信息
    """
    mid = models.CharField(max_length=30, default='null')  # mid---每封邮件独有的标识符
    title = models.TextField()  # 邮件标题
    from_email = models.EmailField()  # 存储发件人邮箱
    from_name = models.CharField(max_length=20)  # 存储发件人姓名
    to_ID_number = models.CharField(max_length=11)  # 收件人学号
    to_name = models.CharField(max_length=20)  # 收件人姓名
    time = models.CharField(max_length=50)  # 存储邮件的发送时间
    content = models.TextField()  # 存储邮件详细内容

    def __unicode__(self):
        return self.title
