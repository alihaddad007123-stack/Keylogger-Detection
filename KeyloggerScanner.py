import re
import os 
from datetime import datetime

def log_writer(text):#كل ما نكتشف كلمة مشبوهة → نرسلها للـ console ونكتبها بالتقرير
    print(text)
    report.write(text+"\n")
report=open("keylogger_report.txt","w",encoding="utf-8")
suspicious_keywords = ["keylogger", "logger", "password", "hook", "capture"]
allowed_extension =[".txt",".log",".ps1",".sh",".conf"]
path=input("Enter folder path:")
keyword_counter={}
file_counter={}
for root ,dirs,files in os.walk(path):
    for file in files:
        full_path=os.path.join(root,file)#نحن بدنا نجمع مسارين مع بعض
        try:
            if not any(file.lower().endswith(ext) for ext in allowed_extension):
                continue
            with open(full_path, "r", errors="ignore") as f: 
                 content=f.read()
        except:
            continue
        for keyword in suspicious_keywords:
            if keyword in content:
               log_writer(f"suspicious keyword : {keyword} found in {full_path}")
               keyword_counter[keyword]=keyword_counter.get(keyword,0)+1
               file_counter[full_path]=file_counter.get(full_path,0)+1
log_writer("\n *******************ANALYAIS*****************")
for keyword , content in keyword_counter.items():
    log_writer(f"keyword '{keyword}' found {content} times")
if file_counter:
    top_file=max(file_counter,key=file_counter.get)
    log_writer(f"\n🔥 Top Suspicious File: {top_file} ({file_counter[top_file]} keywords found)")
report.close()
appdata = os.getenv('APPDATA') #os.getenv يعيد قيمة متغير بيئة النظام
home = os.path.expanduser('~')#يعيد مجلد المستخدم على أي جهاز.
folders_to_scan=[appdata,home]
print(folders_to_scan)
