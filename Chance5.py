import RPi.GPIO as GPIO
import sys
import os
import random
import time
from subprocess import Popen 

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

scarymovie1 = ("/home/pi/Videos/Scary1.mp4")
scarymovie2 = ("/home/pi/Videos/Scary2.mp4")
scarymovie3 = ("/home/pi/Videos/Scary3.mp4")
scarymovie4 = ("/home/pi/Videos/Scary4.mp4")
scarymovie5 = ("/home/pi/Videos/Scary5.mp4")
scarymovie6 = ("/home/pi/Videos/Scary6.mp4")
scarymovie7 = ("/home/pi/Videos/Scary7.mp4")
scarymovie8 = ("/home/pi/Videos/Scary8.mp4")
scarymovie9 = ("/home/pi/Videos/Scary9.mp4")
scarymovie10 = ("/home/pi/Videos/Scary10.mp4")
scarymovie11 = ("/home/pi/Videos/Scary11.mp4")
scarymovie12 = ("/home/pi/Videos/Scary12.mp4")
scarymovie13 = ("/home/pi/Videos/Scary13.mp4")
scarymovie14 = ("/home/pi/Videos/Scary14.mp4")
scarymovie15 = ("/home/pi/Videos/Scary15.mp4")
scarymovie16 = ("/home/pi/Videos/Scary16.mp4")
scarymovie17 = ("/home/pi/Videos/Scary17.mp4")
scarymovie18 = ("/home/pi/Videos/Scary18.mp4")
scarymovie19 = ("/home/pi/Videos/Scary19.mp4")
scarymovie20 = ("/home/pi/Videos/Scary20.mp4")
happymovie1 = ("/home/pi/Videos/Happy1.mp4")
happymovie2 = ("/home/pi/Videos/Happy2.mp4")
happymovie3 = ("/home/pi/Videos/Happy3.mp4")
happymovie4 = ("/home/pi/Videos/Happy4.mp4")
happymovie5 = ("/home/pi/Videos/Happy5.mp4")
happymovie6 = ("/home/pi/Videos/Happy6.mp4")
happymovie7 = ("/home/pi/Videos/Happy7.mp4")
happymovie8 = ("/home/pi/Videos/Happy8.mp4")
happymovie9 = ("/home/pi/Videos/Happy9.mp4")
happymovie10 = ("/home/pi/Videos/Happy10.mp4")
happymovie11 = ("/home/pi/Videos/Happy11.mp4")
happymovie12 = ("/home/pi/Videos/Happy12.mp4")
happymovie13 = ("/home/pi/Videos/Happy13.mp4")
happymovie14 = ("/home/pi/Videos/Happy14.mp4")
screensaver = ("/home/pi/Videos/Screensaver.mp4")

input_state1 = True

quit_video = True

player = False
maxnumber = 34
random.seed()

omxc = Popen(['omxplayer', '-b', screensaver])

while True:
	#Read states of inputs
	input_state1 = GPIO.input(17)
	quit_video = GPIO.input(24)
	movienum = random.randint(1,maxnumber)

	#If GPIO(17) is shorted to ground, play scary movie
	if input_state1 == False:
            if movienum == 1:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie1])
                time.sleep(6)
            if movienum == 2:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie1])
                time.sleep(10)
            if movienum == 3:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie2])
                time.sleep(15)
            if movienum == 4:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie2])
                time.sleep(7)
            if movienum == 5:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie3])
                time.sleep(4)
            if movienum == 6:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie4])
                time.sleep(8)
            if movienum == 7:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie3])
                time.sleep(14)
            if movienum == 8:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie4])
                time.sleep(18)
            if movienum == 9:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie5])
                time.sleep(8)
            if movienum == 10:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie6])
                time.sleep(5)
            if movienum == 11:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie7])
                time.sleep(15)
            if movienum == 12:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie5])
                time.sleep(10)
            if movienum == 13:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie6])
                time.sleep(11)
            if movienum == 14:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie8])
                time.sleep(6)
            if movienum == 15:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie9])
                time.sleep(9)
            if movienum == 16:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie10])
                time.sleep(10)
            if movienum ==17:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie7])
                time.sleep(13)
            if movienum == 18:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie8])
                time.sleep(15)
            if movienum == 19:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie11])
                time.sleep(6)
            if movienum == 20:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie12])
                time.sleep(7)
            if movienum == 21:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie13])
                time.sleep(7)
            if movienum == 22:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie9])
                time.sleep(8)
            if movienum == 23:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie10])
                time.sleep(9)
            if movienum == 24:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie14])
                time.sleep(7)
            if movienum == 25:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie15])
                time.sleep(3)
            if movienum == 26:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie16])
                time.sleep(9)
            if movienum == 27:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie17])
                time.sleep(26)
            if movienum ==28:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie11])
                time.sleep(14)
            if movienum == 29:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie12])
                time.sleep(10)
            if movienum == 30:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie18])
                time.sleep(34)
            if movienum == 31:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie19])
                time.sleep(22)
            if movienum == 32:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie13])
                time.sleep(9)
            if movienum == 33:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', happymovie14])
                time.sleep(10)
            if movienum == 34:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', scarymovie20])
                time.sleep(28)
            if True:
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', screensaver])
	elif quit_video == False:
		os.system('killall omxplayer.bin')