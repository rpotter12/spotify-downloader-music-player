# Sample Python application demonstrating 
# How to create GridLayout in Kivy 

# import kivy module 
import kivy 
	
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
	
# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button 

# The GridLayout arranges children in a matrix. 
# It takes the available space and 
# divides it into columns and rows, 
# then adds widgets to the resulting “cells”. 
from kivy.uix.gridlayout import GridLayout 

# creating the App class 
class Grid_LayoutApp(App): 

	# to build the application we have to 
	# return a widget on the build() function. 
	def build(self): 

		# adding GridLayouts in App 
		# Defining number of coloumn 
		# You can use row as well depends on need 
		layout = GridLayout(cols = 2) 

		# 1st row 
		layout.add_widget(Button(text ='Hello 1')) 
		layout.add_widget(Button(text ='World 1')) 

		# 2nd row 
		layout.add_widget(Button(text ='Hello 2')) 
		layout.add_widget(Button(text ='World 2')) 

		# 3rd row 
		layout.add_widget(Button(text ='Hello 3')) 
		layout.add_widget(Button(text ='World 3')) 

		# 4th row 
		layout.add_widget(Button(text ='Hello 4')) 
		layout.add_widget(Button(text ='World 4')) 

		# returning the layout 
		return layout 

# creating object of the App class 
root = Grid_LayoutApp() 
# run the App 
root.run() 

