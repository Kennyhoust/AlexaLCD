import lcddriver
from time import *
from flask import Flask, url_for
app = Flask(__name__)
lcd = lcddriver.lcd()
@app.route('/')
def api_root():
	lcd.lcd_clear()

	return ''


@app.route('/lcd/<line1>/<line2>/<line3>')
def api_article(line1,line2,line3):
	lcd.lcd_clear()
	lcd.lcd_display_string(line1, 1)
	lcd.lcd_display_string(line2, 2)
	lcd.lcd_display_string(line3, 3)
	lcd.lcd_display_string("kennyhoust", 4)
	return ''

if __name__ == '__main__':
    app.run()

