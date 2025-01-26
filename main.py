import pywhatkit as pyw
Number=input("enter the phone number you want to send : ")
message=input("Enter the message :")
hour_str=int(input("enter the hour :"))
min_str=int(input("Enter the min :"))
pyw.sendwhatmsg(Number,message,hour_str,min_str)