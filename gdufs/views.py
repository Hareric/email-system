# coding=utf-8
from django.shortcuts import render
from forms import GdufsForm
from process.login_email_gdufs import Email_gdufs
from .models import Person, Email


def home(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = GdufsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ID_number = cd['ID_number']
            pwd = cd['password']
            print "获得用户输入学号和密码"
            print ID_number
            print pwd
            try:
                print "查询数据库中是否存在该用户..."
                User = Person.objects.get(ID_number=ID_number)
                print "用户查询成功,数据库中存在该用户"
                name = User.name
                print name
                emails = Email.objects.all().filter(to_ID_number=ID_number).order_by('-time')
                print "成功获得数据库中的邮件内容"

            except:
                print "查询失败,创建新用户"
                email_instance = Email_gdufs(user=ID_number, pwd=pwd)
                emails = email_instance.get_emails()
                name = email_instance.user_name
                Person.objects.create(name=name, ID_number=ID_number, password=pwd)  # save the user's data in database
                for email in emails:  # save the email's data in database
                    Email.objects.create(to_ID_number=ID_number, to_name=name, title=email['title'],
                                         content=email['content'], time=email['time'], from_email=email['from_email'],
                                         from_name=email['from_name'], mid=email['mid'])

            return render(request, 'index.html', {'emails': emails,
                                                  'name': name})
    else:
        form = GdufsForm()
    return render(request, 'index.html', {'form': form})
