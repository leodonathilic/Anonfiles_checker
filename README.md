# ANONFILES Checker

This script was made to check if your file(s) is/are still up on anonfiles.com.
Made entirely using Python 3.

It uses the Anonfiles' API and works in a very simple way.

## Setup
### Gmail setup

First you'll need to create a Gmail account (don't use your main, I am not responsible for anything happening to it).
	
Once created, go on this [link](https://myaccount.google.com/) and hop in the "Security" tab.
Enable 2FA (2 Factor Authentification), this is required since May 30th 2022 as Google removed the possibility to automate sending emails without 2FA later this date.
	
Once done, please click on this [link](https://myaccount.google.com/u/4/apppasswords) to get the password you'll use to send automated emails.
Select apps > Custom > *Choose the name you want*
	
Copy the 16 char password and paste it in the script, in the variable named __email_password = ''__ and add the email address in the __email_sender = ''__ variable.
Finally add the receiving email address in the __email_receiver = ''__ variable and you are good to go to the next part!

### Requirements

In this repository, you will find a requirements.txt file.
The easy way to install every requirements is to open a command prompt (CMD) and travel to the folder's directory.
Once done, type `pip install -r requirements.txt` in the command prompt and please wait for every module to install (should be quick).

## Usage

Hooray! You can now use Anonfiles file checker!
Just double click on the script on Windows or input `py Anonfiles_checker.py` into your command prompt.

The script will bring up two choices, 1st choice being "Add links", and the 2nd being "Check links".

### How do I add a link?

This part is super easy! Once you uploaded a file on Anonfiles, you receive a link in return. Just launch the script and type `1` to select the first option.
The script will ask you to input the link, that will then be parsed and saved in the files in the directory.
#### Quick info
<sub>The links arrive in this format `https://anonfiles.com/XXXXXXXXXX/<file_name>` and will then be saved in this format `https://api.anonfiles.com/v2/file/XXXXXXXXXX/info`. This helps when using the API. Don't worry, the script will remember the file name of the upload, since it is stored in the `db.txt` file. The API type link will however be saved in the `LINKS.txt` file.
You can only add one link at the time for now, the script is most likely being updated soon adding new features.</sub>

	
### How do I check my link(s)?

That is super easy! All you need to do is launch the script and select `2` as an option, now let the script run, it will display every working and dead links on the screen. It will also send you an email with all the dead links so you can let the script run indefinitely, it will check automatically every 24 hours. 


Thank you for using my script. If you encounter any problems or bugs, please open an issue, I'll be more than happy to help!
