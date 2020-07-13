# Tkinter-Gmail-App
It's a simple Email sender which works with any Gmail account.

## Table of contents
* [General info](#general-info)
* [Create App password](#app-password)
* [Technologies](#technologies)
* [Setup](#setup)
* [py to exe](#py-to-exe)
* [License](#license)

## General info
This project is a simple Gmail app which can be used to send email without any browser. You must need App password and enable two factor authentication inorder to send an Email. 

![Screenshot (19)](https://user-images.githubusercontent.com/67178624/87331292-5cebb800-c557-11ea-85f7-7ef57313fc35.png)

## App password
* An App Password is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. App Passwords can only be used with accounts that have 2-Step Verification turned on.

### Creating the App Password
* Go to your [Google Account](https://myaccount.google.com/).
* Select Security.
* Under "Signing in to Google," select App Passwords. You may need to sign in.
* At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
* Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
* Save the password for future use.

## Technologies
Project is created with:
* Python version: 3.8.3
* Tkinter version: 8.5
* smtplib module.
	
## Setup
### To run this project,
#### Install Tkinter
```
pip install tkinter
```
#### Install Wikipedia Api
```
pip install wikipedia
```
#### Install smtplib module
```
pip install smtplib
```
## Customization
### Customize the App according to your desire.
* As Gmail is being used by the most, I set Gmail as first preference.
* You can also change the SMTP to yahoo or any other email services.

## .py to .exe
### Convert .py file to .exe file
#### Install the pyinstaller module
* ```pip install pyinstaller```
#### Instructions
* Open your cmd and change your directory to the .py file.
* Choose an Icon. Icon must be in .ico format.
* Type ```pyinstaller -w -F -i (Your icon directory with file name) (filename.py)``` and hit enter.
* Open the directory and go to Dist folder where you can find the App.

## License
* MIT licensed. See the [License](LICENSE) file for full details. 
