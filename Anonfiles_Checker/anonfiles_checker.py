import requests, time, json, datetime
import logging as l
import os
import smtplib
import ssl
from email.message import EmailMessage
import datetime

x = datetime.datetime.now()

l.basicConfig(format='%(asctime)s %(message)s', filename='LOGS/KELLOGGS.log', encoding='utf-8', level=l.INFO)


email_sender = ''
email_password = ''
email_receiver = ''
DEAD_LINKS = []

banner = '''


			   ___ _               _         
			  / __\ |__   ___  ___| | ___ __ 
			 / /  | '_ \ / _ \/ __| |/ / '__|
			/ /___| | | |  __/ (__|   <| |   
			\____/|_| |_|\___|\___|_|\_\_|   
								 


		1. Add links 				2. Check links


'''



banner_no_menu = '''


			   ___ _               _         
			  / __\ |__   ___  ___| | ___ __ 
			 / /  | '_ \ / _ \/ __| |/ / '__|
			/ /___| | | |  __/ (__|   <| |   
			\____/|_| |_|\___|\___|_|\_\_|   
								 






'''

os.system('cls')
print(banner)
CHOICE = input('')



#CHOICE MENU 
if CHOICE == '1':

	links_to_add = input("Please paste the link you want to add\n Example: \nhttps://anonfiles.com/XXXXXXXXXX/<file_name>\n")
	print("Working...")
	links_to_add = links_to_add.replace('https://anonfiles.com/', '')
	name_sep = links_to_add.split("/")
	with open("db.txt", 'a+') as f:
		for item in name_sep:
			f.write("%s " % item)
		f.write("\n")	
		f.close()
	print(name_sep)
	name_sep=name_sep.pop(0)
	print(name_sep)
	final_link = "https://api.anonfiles.com/v2/file/"+name_sep+"/info"
	print(final_link)
	with open('LINKS.txt', 'a+') as f:
		f.write(final_link + "\n")
		f.close()

elif CHOICE == '2':
	os.system("cls")
	print(banner_no_menu)
	while True:
		l.info("Link checker started\n")

		with open('LINKS.txt') as f:
			mylist = f.read().splitlines() 

		for i in mylist:
			URL = i
			r = requests.get(url=URL)
			time.sleep(1)
			data = r.json()

			if data["status"] == True:
				
				print(data["data"]["file"]["metadata"]["name"], "File still up!\n")
				l.info(data["data"]["file"]["metadata"]["name"] + " File still up!")

			elif data["status"] == False:
				word = i
				word = word.replace('https://api.anonfiles.com/v2/file/', '')
				word = word.replace('/info', '')
				with open(r'db.txt', 'r') as fp:
					
					lines = fp.readlines()
					for line in lines:
						
						if line.find(word) != -1:

							subject = '[!] - ANONFILES LINK IS DEAD'
							body = """
							Please upload this file again ASAP !
							""" + line
							
							em = EmailMessage()
							em['From'] = email_sender
							em['To'] = email_receiver
							em['Subject'] = subject
							em.set_content(body)
							
							context = ssl.create_default_context()
							
							with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
							    smtp.login(email_sender, email_password)
							    smtp.sendmail(email_sender, email_receiver, em.as_string())

				print(f"{line} " + data["error"]["message"]+"\n")
				l.info(word + i + " LINK IS DEAD")

			elif r.status() == 503:
				print("Server down...")			

		print('Last checked : ', x)
		print('Next check in 24 hours')
		time.sleep(86400)	

else:
	print("Not a possible choice, exiting...")
	quit()
