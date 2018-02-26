
import LCD_1in44
import LCD_Config
import Image
import ImageDraw
import ImageFont
import ImageColor
import RPi.GPIO as GPIO
import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def bcallback(KEY):
	print(KEY)
	
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,GPIO.PUD_UP)#key1
GPIO.add_event_detect(21,GPIO.FALLING,bcallback,200)
GPIO.setup(20,GPIO.IN,GPIO.PUD_UP)#key2
GPIO.add_event_detect(20,GPIO.FALLING,bcallback,200)
GPIO.setup(16,GPIO.IN,GPIO.PUD_UP)#key3
GPIO.add_event_detect(16,GPIO.FALLING,bcallback,200)
GPIO.setup(6,GPIO.IN,GPIO.PUD_UP)#joystick up
GPIO.add_event_detect(6,GPIO.FALLING,bcallback,200)
GPIO.setup(19,GPIO.IN,GPIO.PUD_UP)#joystick down
GPIO.add_event_detect(19,GPIO.FALLING,bcallback,200)
GPIO.setup(5,GPIO.IN,GPIO.PUD_UP)#joystick left
GPIO.add_event_detect(5,GPIO.FALLING,bcallback,200)
GPIO.setup(26,GPIO.IN,GPIO.PUD_UP)#joystick right
GPIO.add_event_detect(26,GPIO.FALLING,bcallback,200)
GPIO.setup(13,GPIO.IN,GPIO.PUD_UP)#joystick press
GPIO.add_event_detect(13,GPIO.FALLING,bcallback,200)

def main():
	LCD = LCD_1in44.LCD()
	print "**********Init LCD**********"
	Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
	LCD.LCD_Init(Lcd_ScanDir)
	image = Image.new("RGB", (LCD.LCD_Dis_Column, LCD.LCD_Dis_Page), "WHITE")
	draw = ImageDraw.Draw(image)
	draw.line([(0,0),(127,0)], fill = "BLUE",width = 5)
	draw.line([(127,0),(127,127)], fill = "BLUE",width = 5)
	draw.line([(127,127),(0,127)], fill = "BLUE",width = 5)
	draw.line([(0,127),(0,0)], fill = "BLUE",width = 5)
#draw.rectangle([(18,10),(110,20)],fill = "RED")
	draw.text((33, 22), 'kjhtml', fill = "BLUE")
	draw.text((0, 36), 'IPaddess:', fill = "BLUE")
	LCD.LCD_ShowImage(image,0,0)	
	draw.text((0, 50), get_host_ip(), fill = "BLUE")
	LCD.LCD_ShowImage(image,0,0)		  
#while (True):		  
if __name__ == '__main__':
    main()
