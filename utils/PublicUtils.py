import os
import smtplib,time
import zipfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#发送邮件
def send_mail(receivers, file_path):
    smtp = smtplib.SMTP()
    smtpserver = 'smtp.163.com'
    user = 'XXXXXX'
    password = 'XXXXXXX'
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

#压缩文件
def zip_file(startdir):
    file_news = startdir + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()

#删除文件
def deletefiles(filepaths):
    path = os.path.dirname(os.path.abspath(__file__)) + filepaths
    if path is not None:
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            os.remove(c_path)
    print('删除成功')