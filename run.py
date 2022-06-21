# -*- coding:utf-8 -*-
import os,time
import unittest
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils import HTMLTestRunnerCN3
from case.test_case_yaml import Test_test

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))




def zip_file(startdir):
    file_news = startdir + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()
    return file_news

def send_mail(receivers, file_path):
    smtp = smtplib.SMTP()
    smtpserver = 'smtp.163.com'
    user = 'XXXXXX'
    password = 'XXXXXXXXX'
    subject = '接口自动化测试报告——' + time.strftime('%Y_%m_%d_%H_%M_%S')
    #添加附件，#创建一个带附件的实例
    message = MIMEMultipart()
    #邮件正文内容
    message.attach(MIMEText('这个是接口测试用例执行结果。请查收', 'plain', 'utf-8'))
    message['To'] = receivers
    message['subject'] =subject
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename='+file_path.split('/')[-1]
    message.attach(att1)
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(user,receivers,message.as_string())
    smtp.quit()



print('-----start-----')
if __name__ == '__main__':
    htmlFile = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '/report/result.html'
    print(htmlFile)
    fp = open(htmlFile, 'wb')
    test = unittest.TestLoader().loadTestsFromTestCase(Test_test)
    runner = HTMLTestRunnerCN3.HTMLTestReportCN(stream=fp, verbosity=2, title=u'接口测试', tester='lph')
    runner.run(test)

    file_new_name = zip_file('./report/result.html')
    send_mail('XXXXXXXX','./report/result.html.zip', 'result.zip')