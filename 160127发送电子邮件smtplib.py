#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-27 21:31:17

import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'test@ramwin.com'  
receiver = 'ramwin@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.mxhichina.com'  
username = 'test@ramwin.com'  
password = 'Zettage321'  
  
msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.mxhichina.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

