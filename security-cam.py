import os
from picamera import PiCamera
from gpiozero import MotionSensor
from sendemail import send_email
from load_creds import load_creds
from email.message import EmailMessage

import datetime as dt
import multiprocessing
from time import sleep

path = os.path.dirname(os.path.realpath(__file__))+"/recordings/"
creds = load_creds()

#email notifcation specifics
def msg_specifics(msg):
    msg['subject'] = "Motion has been detected"
    msg.set_content("Urgent! See attached video.")
    msg['to'] = creds[2]
    return msg

#camera setup
camera = PiCamera()
camera.vflip = True

#Motion sensor setup
pir = MotionSensor(17)

sleep(5)

def startup():
    start_msg = EmailMessage()
    start_msg['subject'] = "System Notification"
    start_msg.set_content("Motion Detection system now online. Be alert for future notifications alerting you of motion.")
    start_msg['to'] = "b.hen02@icloud.com"

    file_name = record(10)

    start_msg = attach(start_msg,file_name)

    sent = False
    while not sent:
        try:
            send_email(start_msg)
            sent = True
        except:
            pass

def convert_file(file_name):
    print("Converting file...")
    os.system("MP4Box -add "+file_name+".h264 "+file_name+".mp4")
    os.remove(file_name+".h264")
    print("File converted.")

def record(t):
    print("Recording...")
    file_name = path+dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    camera.start_recording(file_name+".h264")
    elapsed=0
    while elapsed < t:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(1)
        elapsed+=1
    camera.stop_recording()
    convert_file(file_name)
    return file_name

def attach(msg,file_name):
    with open(file_name+".mp4",'rb') as f:
        data = f.read()
        msg.add_attachment(data,maintype="application",subtype="mp4",filename=f.name)
    return msg

def notify(file_name):
    msg = msg_specifics(EmailMessage())
    msg = attach(msg,file_name)

    email_process = multiprocessing.Process(target=send,args=[msg,])
    try:
        email_process.start()
    except:
        pass

def send(msg):
    print("Sending Email Notification...")
    send_email(msg)
    print("Email Sent.")

    msg.get_payload()[0]._payload = None

startup()

while True:
    print("Waiting for motion...")
    pir.wait_for_motion()
    print("Motion Detected")
    file_name = record(30)
    notify(file_name)