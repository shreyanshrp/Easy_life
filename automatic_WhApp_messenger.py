#Automatic Message sender for whatsapp program in python , by shreyanshrp(github.com/shreyanshrp)
import pywhatkit
hr=int(input("Enter the hour when you want to send the message(24hr format): "))
min=int(input("Enter the minute when you want to sen the message: "))
mob=input("Enter mobile number with + and country code (without spaces): ")
message=input("Enter the message you want to send: ")
pywhatkit.sendwhatmsg(mob, message, hr, min)

