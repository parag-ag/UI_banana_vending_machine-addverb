import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore, QtGui, uic,QtTest
from PyQt4.QtGui import *
import subprocess
from time import sleep

output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
resolution = output.split()[0].split(b'x')

a = QApplication(sys.argv)
global x 					#width of screen
global y					#height of screen
global textbox
global cur_stage
cur_stage = 0

class UI:
	def __init__(self):
		self.x = int(resolution[0])				#width of screen
		self.y = int(resolution[1])				#height of screen

		self.w1 = QWidget()
		self.w1.setWindowTitle("Enter coin")
		self.w1.resize(self.x, self.y)

		self.w2 = QWidget()
		self.w2.setWindowTitle("")
		self.w2.resize(self.x, self.y)
		textbox = QLabel(self.w2)
		
		self.w3 = QWidget()
		self.w3.setWindowTitle("")
		self.w3.resize(self.x, self.y)
		
		self.w4 = QWidget()
		self.w4.setWindowTitle("")
		self.w4.resize(self.x, self.y)
		
		self.w5 = QWidget()
		self.w5.setWindowTitle("")
		self.w5.resize(self.x, self.y)
		
		self.w6 = QWidget()
		self.w6.setWindowTitle("")
		self.w6.resize(self.x, self.y)

	def amt_screen(self,stage,text=''):
		if stage=='1':
			#window w1
			self.label_w1 = QLabel(self.w1)
			self.movie = QMovie("g3.gif")
			self.movie.setScaledSize(QtCore.QSize(self.x,self.y))
			self.label_w1.setMovie(self.movie)
			self.movie.start()
			try:
				self.w5.close()
			except:
				print("")
			try:
				self.w4.close()
			except:
				print("")
			self.w1.show()
	
		elif stage=='2':
			if cur_stage==0:
				textbox.clear()
				font = QtGui.QFont()
				font.setPointSize(100)
				font.setBold(True)
				font.setItalic(True)
				font.setWeight(75)
			
				textbox.move(x/3, y/3)
				textbox.setText("You entered \n\tRs. "+text)
				textbox.setFont(font)
			else:
				try:
					w1.close()
				except:
					print("")
				try:
					w2.close()
				except:
					print("")
				#window w2
				label_w2=QLabel(w2)
				image = QPixmap("ret_money.jpg")
				image2=image.scaled(x,y)
				label_w2.setPixmap(image2)
				font = QtGui.QFont()
				font.setPointSize(100)
				font.setBold(True)
				font.setItalic(True)
				font.setWeight(75)
				
				textbox.move(x/3, y/3)
				textbox.setText("You entered \n\tRs. "+text)
				textbox.setFont(font)
				w2.show()
	
		elif stage=='3':
			#window w3
			label_w3=QLabel(w3)
			image_w3 = QPixmap("")
			image2_w3=image_w3.scaled(x,y)
			label_w3.setPixmap(image2_w3)
			btn_w3_1=QPushButton("Continue",w3)
			btn_w3_1.move(x/2,y/2)
			try:
				w2.close()
			except:
				print("")
			w3.show()
	
		elif stage=='4':
			#window w4
			label_w4 = QLabel(w4)
			movie = QMovie("g2.gif")
			movie.setScaledSize(QtCore.QSize(x,y))
			label_w4.setMovie(movie)
			movie.start()
			try:
				w3.close()
			except:
				print("")
			w4.show()
			print('a')
			QtTest.QTest.qWait(2000)
			print('b')
			w4.close()
			#amt_screen(1,text)	
	
		elif stage=='5':
			#window w5
			label_w5=QLabel(w5)
			image_w5 = QPixmap("ret_money.jpg")
			image2_w5=image_w5.scaled(x,y)
			label_w5.setPixmap(image2_w5)
			try:
				w6.close()
			except:
				w2.close()
			w5.show()
			QtTest.QTest.qWait(3000)
			w5.close()
	
		elif stage=='6':
			#window w6
			label_w6=QLabel(w6)
			image_w6 = QPixmap("weong.png")
			image2_w6=image_w6.scaled(x,y)
			label_w6.setPixmap(image2_w6)
			#btn_w6_1=QPushButton("Cancel",w6)
			#btn_w6_1.move(x/2,y/2)
			try:
				w1.close()
			except:
				print("")
			w6.show()
		a.exec_()
obj = UI()

obj.amt_screen(1,1)

sys.exit()
