import requests
import re
from bs4 import BeautifulSoup
import os
import os.path
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders

_user = "123123@qq.com"
_pwd  = "********"
_to   = "******@kindle.cn"

def htmls():
    def __init__(self):
        self.home_url = 'http://daily.zhihu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    def home_html(self):
        content = requests.get(self.home_url, headers = self.headers)
        all_href = BeautifulSoup(content.text, 'html5lib').find_all('a',class_ = 'link-button')
        for href in all_href:
            url = self.home_url + href['href']
            self.story_html(url)


def save_pdf(url,path):
    os.chdir(r'G:\python\zhihu\ribao\content')
    file_name = str(path) + '.pdf'
    if os.path.exists(file_name):
        pass
    else:
        print(file_name)
        pdfkit.from_url(url,file_name)



def send_email():
    path = r'G:\python\zhihu\ribao\content'
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        msg = MIMEMultipart()
        msg['Subject'] = 'convert'  #邮件标题
        msg['From'] = _user #显示发件人
        msg['To'] = _to #接收邮箱
        attfile = file_path
        basename = os.path.basename(file_path) 
        print(basename)
        fp = open(attfile,'rb')
        att = MIMEText(fp.read(),'base64','gbk')
        att['Content-Type'] = 'application/octer-stream'
        att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
        encoders.encode_base64(att)
        msg.attach(att)
        s = smtplib.SMTP_SSL("smtp.qq.com", 465,timeout = 30)#连接smtp邮件服务器,qq邮箱端口为465
        s.login(_user, _pwd)#登陆服务器
        s.sendmail(_user, _to, msg.as_string())#发送邮件
        s.close()