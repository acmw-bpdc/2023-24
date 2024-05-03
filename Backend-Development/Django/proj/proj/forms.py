from django.http import HttpResponse 
from django.shortcuts import render
import pymongo as pm
import csv

event_recs = []

def result(request):
    roll = request.POST['roll']  
    html= '''<body style="color: #DB1792; background-color: mintcream">
          <p><p> <center><h1>The Data: <br>id:''' + roll  + '''<br> was successfully appended to the student file.</h1>
          <br><a href='../'>Main page</a></center>
          </body>'''
    return HttpResponse(html)

def writefile(s_id, s_name, s_mail, mode):
    rec = {'student id': s_id,
            'name' : s_name,
            'email id': s_mail,
            'preferred mode': mode
            }
    event_recs.append(rec)
    for k in event_recs:
        print('id: '+ k['student id'])
        print('name: '+ k['name'])
        print('email id: '+ k['email id'])
        print('mode of event preferred: '+ k['preferred mode'])
        print()


def regcsv(request):
        df = open("e.csv", 'a')
        record= []
        s_name = request.POST.get('s_name')
        s_id= request.POST.get('s_id')
    
        s_mail = request.POST.get('s_mail')
        mode = request.POST.get('online')

        
        writefile(s_id, s_name, s_mail, mode)
        
        html= '''<body style="color: #DB1792; background-color: mintcream">
          <center><h1><p><p><p><p> Thank you for your registration. The details regarding the sessions shall be mailed soon to you.</h1>
          <br><br><a href='../'>Back to Main page</a></center>
          </body>
           '''
    
        return HttpResponse(html)



