#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:24:27 2019

@author: cuijiajun
"""
# regex
import re
# open the file 
f = open ('address_information.csv')
# convert the string to list 
for line in f :
    line = line.rstrip()
    line = re.split (r',',line)
# extract login, address and subject
    login = line[0]
    address = line[1]
    subject = line[2]
# choose the legal address    
    if re.findall(r'(\S+@\d+\w+)',address):
# send emails        
        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header
        
        mail_host="smtp.zju.edu.cn"  #server
        mail_user="3180110107@zju.edu.cn"    #username
        mail_pass="129118Cz"   #password
# sender and receivers        
        sender = '3180110107@zju.edu.cn'
        receivers = [address]
 # the bodytext of emails       
        text = open ('body.txt')
        body = text.read()
 # match the user name        
        body = re.sub (r'User',login,body)
# parameters        
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = Header("cjj", 'utf-8')   # 发送者
        message['To'] =  Header("address", 'utf-8')        # 接收者
        message['Subject'] = Header(subject, 'utf-8') 
# sent and output        
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host,25)   # 25 为 SMTP 端口号
        
            smtpObj.login('3180110107','129118Cz')  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ('Email sent successfully')
        except smtplib.SMTPException:
            print ("Error:Unable to send email")
       
    
        
        
