import os
import time
import datetime
mainFolder = "recordings/"
cameraName = "Cam1"
# address = "rtsp://admin:vijnalabs01@192.168.1.64"
address = "2"

while True:
    todayDate = time.strftime("%d-%m-%y")
    print(todayDate)
    destFolder = mainFolder + todayDate
    if not os.path.exists(destFolder):
        os.makedirs(destFolder) 
    now = datetime.datetime.now()
    current_time = now.strftime("%y-%m-%d-%H-%M-%S")
    print("Current Time =", current_time)
    fileName = destFolder + '/'+ cameraName + "-" + current_time + ".mp4"
    print(fileName)
    cmd_webCam = "ffmpeg -f v4l2 -i /dev/video0 -t 00:00:10 " + fileName
    # cmd_ipCam = "ffmpeg -i " + address +" -vcodec copy -t 00:00:10 " + fileName
    print(cmd_webCam)
    # print(cmd_ipCam)
    os.system(cmd_webCam)
    
