# vos3000-tool
vos3000平台主叫号码应答率，呼叫次数监控以及主叫替换的网页平台

安装步骤

将安装包下载到vos服务器

1.在vos3000库中创建主叫号码表，建表语句在sql.txt

2.编辑crontab 任务
  
  */1 * * * * /root/auto_get_vos_caller.py

3.启动app.py,访问1234端口

<img width="1865" height="916" alt="image" src="https://github.com/user-attachments/assets/4bc0b9f4-b21b-42ba-9cc1-b6c1a45c74b4" />
<img width="1847" height="362" alt="image" src="https://github.com/user-attachments/assets/17320514-90cd-40e7-8d67-aba4675254b4" />




