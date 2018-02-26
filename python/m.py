
import LCD_1in44
import LCD_Config
import Image
import ImageDraw
import ImageFont
import ImageColor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,GPIO.PUD_UP)
def bcallback(KEY):
	print('kkk')
GPIO.add_event_detect(21,GPIO.FALLING,bcallback,200)

def main():
	LCD = LCD_1in44.LCD()
	print "**********Init LCD**********"
	Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
	LCD.LCD_Init(Lcd_ScanDir)
	image = Image.new("RGB", (LCD.LCD_Dis_Column, LCD.LCD_Dis_Page), "WHITE")
	draw = ImageDraw.Draw(image)
	#font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
	print "***draw line"
	draw.line([(0,0),(127,0)], fill = "BLUE",width = 5)
	draw.line([(127,0),(127,127)], fill = "BLUE",width = 5)
	draw.line([(127,127),(0,127)], fill = "BLUE",width = 5)
	draw.line([(0,127),(0,0)], fill = "BLUE",width = 5)
	print "***draw rectangle"
	draw.rectangle([(18,10),(110,20)],fill = "RED")
	print "***draw text"
	draw.text((33, 22), 'WaveShare ', fill = "BLUE")
	draw.text((32, 36), 'Electronic ', fill = "BLUE")
	draw.text((28, 48), '1.44inch LCD ', fill = "BLUE")
	while (True):
		time.sleep(1)
if __name__ == '__main__':
    main()
