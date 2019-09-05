#pip install requests

import requests


def Lineconfig(command):
	url = 'https://notify-api.line.me/api/notify'
	token = 'aHLErCPp3eXBfSUzI3KRPPlk0VnXsWpiSMeVxmgkepT' ## Change to Your Token
	header = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	return requests.post(url, headers=header, data = command)

def sendtext(message):
	# send plain text to line
	command = {'message':message}
	return Lineconfig(command)


def sticker(sticker_id,package_id):
	command = {'message':" ",'stickerPackageId':package_id,'stickerId':sticker_id}
	return Lineconfig(command)


def sendimage(url):
	command = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
	return Lineconfig(command)


#sendtext('PM 2.5 : 100')
#sticker(1,1) #check sticker_id and package_id from sticker.pdf
#sendimage('http://uncle-engineer.com/loongtu.jpg') #image url
