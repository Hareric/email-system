# coding=utf-8
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
"""
Author = Eric_Chan
Create_Time = 2016/02/29
登录数据库中已存在的用户
模拟登录邮箱系统,更新数据库中的邮件内容
input:广外邮箱的帐号和密码
return:收件箱中的详细内容
"""
import urllib
import urllib2
import re


class Email_gdufs_twice:
    header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6)'
                            ' Gecko/20091201 Firefox/3.5.6'}
    user_accounts = ''  # 记录用户帐号(学号)
    user_name = ''  # 记录用户姓名
    user = ''  # 记录用户帐号
    pwd = ''  # 记录用户密码
    cookie = None
    sid = None
    mailBaseUrl = 'http://gdufs.edu.cn/'

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def login(self):
        """
        登录学校邮箱
        :return:
        """
        user = self.user
        pwd = self.pwd
        header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6)'
                                ' Gecko/20091201 Firefox/3.5.6'}
        post_data = urllib.urlencode({  # urllib 的 urlencode 方法将字典编码
                                        'user': user,
                                        'password': pwd,
                                        'locale': 'zh_CN',
                                        'face': '',
                                        'action:login': '',
                                        })
        # 注意版本不同，登录URL也不同
        req = urllib2.Request(  # 创建一个Request的实例,用来发出请求
                                url='http://gdufs.edu.cn/coremail/index.jsp',
                                data=post_data,
                                headers=header
                                )
        res = urllib2.urlopen(req)  # response 获得服务器的响应
        res_read = res.read()
        # print 'response \n', res_read, '\n------------------------------------------------------------------'

        pattern_sid = re.compile('.jsp\?sid=([^"]+)')  # 匹配返回结果是否有sid,若有则表明登录成功
        search_result = pattern_sid.search(res_read)  # re.search(pat,string) 等同于 pat.search(string)
        sid = search_result.group(1)

        pattern_user_name = re.compile('<span class="account">(.*)</span> &lt;\d+@gdufs\.edu\.cn&gt')  # 获得用户的姓名
        user_name = re.findall(pattern_user_name, res_read)
        if search_result:
            self.sid = sid
            self.user_name = user_name[0]
            print 'Login Successful.....'
            print "sid:", self.sid, "\nuser_name:", self.user_name
        else:
            print 'Login failed....'



