#coding=utf-8
import smtplib,traceback
from email.mime.text import MIMEText
msg_from='1379875051@qq.com'                        #发送方邮箱
passwd=''                                   #填入发送方邮箱的授权码
msg_to='1379875051@qq.com'                     #收件人邮箱
                            
subject="python邮件测试"                                     #主
content="这是我使用python smtplib及email模块发送的邮件"#正文
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except :
    traceback.print_exc()
    print ("发送失败")
finally:
    s.quit()
