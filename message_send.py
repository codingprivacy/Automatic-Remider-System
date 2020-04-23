from twilio.rest import Client
import messages
import requests
import json
import datetime
import gspread                              #google spreadsheet api
from oauth2client.service_account import ServiceAccountCredentials






def send_message(number,mail,name,pass_no,parent_email,rector_contact,message,sheet):


    #using twillio
    # #print("came here")
    # number2="+"+str(number)
    #
    # client = Client(messages.account_sid, messages.auth_token)
    # message = client.messages.create(
    #     to=number2,                                     # "+919876543210"
    #     from_="+14157920130",
    #     body=messages.message)
    # print("message successfully sent to,:",name)
    #

    student=requests.get("http://api.msg91.com/api/sendhttp.php?sender=MSGIND&route=4&mobiles=+91"+str(number)+"&authkey=192990AkDQ3bDBv5a59de99&country=91&message="+message)
    rector=requests.get("http://api.msg91.com/api/sendhttp.php?sender=MSGIND&route=4&mobiles=+91"+str(rector_contact)+"&authkey=192990AkDQ3bDBv5a59de99&country=91&message="+(messages.rector_sms%(name,pass_no)))
    print(messages.rector_sms%(name,pass_no))

    row=[name,number,message,datetime.datetime.now().time()]
    sheet.append_row(row)

    #print(r.content)



