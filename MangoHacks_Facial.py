import serial
import json
import sys
import subprocess
import picamera
nfc_id = "a"


def nfc_id_lookup(nfc_id):
	user_table = {"3" : "cody", "4" : "kyle","1" : "jake","2" : "gabby","5" : "master"}
	#user_table = defaultdict(lambda: 0)
	return user_table[nfc_id]

def prescription(nfc_id):
	med_table = {"cody" : "3", "jake" : "1", "kyle" : "4", "gabby" : "2", "master" : "a"}
	return med_table[nfc_id]

ser = serial.Serial('/dev/ttyACM0', 9600)
ser2 = serial.Serial('/dev/ttyACM1',9600)
while True:
	
	nfc_id = ser.readline().strip()# X\r\n
        nfc_user = nfc_id_lookup(nfc_id)
        if(nfc_id != "a"):
                camera = picamera.PiCamera()
                camera.capture("capture.jpg")
                camera.close()
                print(nfc_user + '\'s card scanned')
                idk = prescription(nfc_user)
                result = {"match":"none"}
                if (nfc_user != "master"):
                        try:
                                result = json.loads(subprocess.check_output([sys.executable, "captureNrekognize.py"]))
                        except:
                                result = {'match':'none'};
                                pass 
                #muntaserus-rex's code
                #send dragonboard perscription(nfc_id)
                
                if (result['match'] != "none" or nfc_user == "master"):
                        if(result['match'] == nfc_user + '.jpg' or nfc_user == 'master'):
                                
                                print(result['match'])
                                ser2.write(idk+ "\r\n")
                                print(idk)
                        else:
                                print('WRONG USER')
                else:
                        print("No Match")
	
	

	
#def face_id_lookup(face_id)
#	def (#codys face id):
#		return "cody"
#	def (#kyles face id):
#		return "kyle"
#	def (#jakes face id):
#		return "jake"
#	def (#gabbys face id):
#		return "gabby"
#		
