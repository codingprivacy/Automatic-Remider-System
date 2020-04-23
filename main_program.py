#Flow of the program
#while loop --> scheduling for 7 am --> function 'update_database; --> function 'thread_row'
# --> scheduling for 8 am --> function 'check_date_match' --> if condition match --> .py file 'message_send' to send message and mail

import _thread    #threading
from datetime import datetime,timedelta    #checking date time of the system
import json
import schedule   #scheduling
import gspread                              #google spreadsheet api
from oauth2client.service_account import ServiceAccountCredentials    #authentiction
import message_send                     #python file for further mailing and messaging
import messages


def thread_row(sheet,db_row,json_data,file):   #this thread is going to work continously for each student unless the task gets over
    print("into thread_row")

    def check_date_match(db_row):
            scope = ['https://spreadsheets.google.com/feeds']
            creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_key2.json', scope)      #opening frro logs sheet
            client = gspread.authorize(creds)
            sheet = client.open('FRRO_LOGS').sheet1
            for i in range(1,5):         # for frro 1 to frro 4 ; checking if the todays date matches with any

                    day_1=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=1)     #timedelta adds days to the given date  ... Hence we save all the notifications date in variable
                    day_2=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=2)
                    day_3=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=3)
                    day_10=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=10)
                    day_11=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=11)
                    day_12=datetime.strptime(db_row['frro %d'%(i)+'(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=12)
                    #print("into loop2")
                    if(i==1):
                        if(str(datetime.now().date())==str(day_1.date()) or  str(datetime.now().date())==str(day_2) or  str(datetime.now().date())==str(day_3)):      #column 12
                                print("condition satisfied for day 1,2,3 frro 1")

                                _thread.start_new_thread(message_send.send_message,(db_row['contact number'],db_row['email'],db_row['name of student'],db_row['passport no'],db_row['parent email'],db_row['rector contact'],db_row['parent email'],messages.student_sms_1frro123,sheet))

                        if(str(datetime.now().date())==str(day_12) or  str(datetime.now().date())==str(day_10) or  str(datetime.now().date())==str(day_11)):
                                print("condition satisfied for day 10,11,12 frro 1")
                                _thread.start_new_thread(message_send.send_message,(db_row['contact number'],db_row['email'],db_row['name of student'],db_row['passport no'],db_row['parent email'],db_row['rector contact'],messages.student_sms_1frro101112,sheet))
                    if(i==2 or i==3 or i==4):
                        if(str(datetime.now().date())==str(day_1.date()) or  str(datetime.now().date())==str(day_2) or  str(datetime.now().date())==str(day_3 or str(datetime.now().date())==str(day_12) or  str(datetime.now().date())==str(day_10) or  str(datetime.now().date())==str(day_11))):
                            print("condition satisfied for frro2 or frro3 or frro4")
                            if(db_row["frro%d incampus"%(i)]=='yes'):
                                _thread.start_new_thread(message_send.send_message,(db_row['contact number'],db_row['email'],db_row['name of student'],db_row['passport no'],db_row['parent email'],db_row['rector contact'],messages.student_sms_otherfrro_incampus,sheet))
                            if(db_row["frro%d incampus"%(i)]=='no'):
                                _thread.start_new_thread(message_send.send_message,(db_row['contact number'],db_row['email'],db_row['name of student'],db_row['passport no'],db_row['parent email'],db_row['rector contact'],messages.student_sms_otherfrro_outcampus,sheet))


        # if(db_row['single_visa']==0):    # if the visa is not for the whole course and needs renewel in between
        #
        #     day_1=datetime.strptime(db_row['visa issue date'],'%Y-%m-%d')+timedelta(days=1)
    #print(datetime.now().date())
    #print(datetime.strptime(db_row['frro 4(rc/rp)_start'],'%Y-%m-%d')+timedelta(days=14))

    def check_condition(db_row,json_data):
        if(  datetime.now() < (datetime.strptime(db_row['frro 4(rc/rp)_start'],'%Y-%m-%d'))+timedelta(days=14)   ):
            check_date_match(db_row)

        else:
            del json_data[ db_row['name of student'] ]     #the task of the student is completed hence to remove the name from the json file
            f=open('data.json','w')
            f.write(json.dumps(json_data))
            schedule.clear('daily_routine')
            return schedule.CancelJob

    schedule.every().day.at("11:33").do(lambda:check_condition(db_row,json_data)).tag('daily_routine','friend')          #checking the date every date at 9:00

def update_database():    #taking data from the sheets at regular intervals 7:00 am
    print("update_database")
    try:
        print("into try function")
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('FRRO-Reminder-API.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('FRRO_PU').sheet1
        db=sheet.get_all_records()       #taking all the records
        print(db)
        file=open('data.json','r')
        json_data=json.load(file)
        file.close()

        for i in range(0,len(db)):      #for all the records .. making a thread of each row i.e. for each person.
            print("into loop1")
            if(db[i]['name of student'] not in json_data.keys()):     #checking if the name present in data.json
                json_data[  db[i]['name of student']  ]="started"    #if name not present ; then add the name and start the thread of it
                f=open('data.json','w')
                f.write(json.dumps(json_data))
                f.close()
                print("database updated")
                _thread.start_new_thread(thread_row,(sheet,db[i],json_data,file))  #thread created for each student

    except:
        schedule.every(1).minute.do(update_database)
schedule.every().day.at("16:46").do(update_database)    #checks every day and updates the datebase

while True:

    schedule.run_pending()











