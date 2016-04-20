#----------------------------------------------------------------------------
# Written by: roflollies
# Date started: 18/04/2016
# Version Date: 
# Description: Simple program that calculates damages in Wargame: Red Dragon
#----------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk

#Initialise tkinter
class WargameCalcApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# Make different 'windows' for each section of the program.
		# will probably add other functionality via different 'windows' later on
		# (Literally just referencing sentdex's tutorial I'll get what's going on one day)

		self.frames = {}

		for i in (StartPage, Heat_Calc, KE_Calc):
			frame = i(container, self)
			self.frames[i] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


# initialise the start page frame
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page")
		label.pack(pady=10, padx=10)

		# make buttons whoooooo
		Heat_Button = ttk.Button(self, text="HEAT Damage Calculator", 
			command = lambda: controller.show_frame(Heat_Calc))
		Heat_Button.pack()
		KE_Button = ttk.Button(self, text="KE Damage Calculator",
			command = lambda: controller.show_frame(KE_Calc))
		KE_Button.pack()

class Heat_Calc(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="HEAT Damage")
		label.pack(pady=10, padx=10)

		#calculate stuff here
		def calculate_HEAT(heat, armour):
			heat_damage_entry.delete(0, last=len(heat_damage_entry.get())+1)
			heat = int(heat)
			armour = int(armour)
			if armour == 1:
				damage = heat
				damage = str(damage)
				heat_damage_entry.insert(0, damage)
				return
			elif armour == 0:
				damage = heat*2
				damage = str(damage)
				heat_damage_entry.insert(0, damage)
				return
			elif (heat - armour) >= 10:
				damage = 6 + ((heat - 10) - armour)
				damage = str(damage)
				heat_damage_entry.insert(0, damage)
				return
			elif (heat - armour) <= 10 and (heat - armour) >= 1:
				damage = ((heat-armour)/2) + 1
				damage = str(damage)
				heat_damage_entry.insert(0, damage)
				return
			else:
				damage = 1
				heat_damage_entry.insert(0, damage)
				return
			
		heat_label=tk.Label(self, text="Enter AP power")
		heat_label.pack(pady=1, padx=10)
		heat_entry=tk.Entry(self)
		heat_entry.pack(pady=1, padx=10)

		armour_label=tk.Label(self, text="Enter target armour")
		armour_label.pack(pady=1, padx=10)
		armour_entry=tk.Entry(self)
		armour_entry.pack(pady=1, padx=10)

		heat_damage_label=tk.Label(self, text="Damage")
		heat_damage_label.pack(pady=1, padx=10)
		heat_damage_entry=tk.Entry(self)
		heat_damage_entry.pack(pady=5)

		calc_button = ttk.Button(self, text="Calculate!", 
			command = lambda: calculate_HEAT(heat_entry.get(), armour_entry.get()))
		calc_button.pack(pady=5)

		KE_Button = ttk.Button(self, text="KE Damage Calculator",
			command = lambda: controller.show_frame(KE_Calc))
		KE_Button.pack(pady=1)

		return_button = ttk.Button(self, text="Go Back",
			command = lambda: controller.show_frame(StartPage))
		return_button.pack()

class KE_Calc(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="KE Damage")
		label.pack(pady=10, padx=10)

		#calculate stuff here
		def calculate_KE_range(ap,gun_range,actual_range):
			gun_range = int(gun_range)
			actual_range = int(actual_range)
			ap = int(ap)
			if gun_range > actual_range:
				difference = (actual_range - gun_range)/175
				actual_ap = ap + difference
				return actual_ap
			elif actual_range > gun_range:
				return 0
			else:
				return ap

		def calculate_KE(ap,armour):
			damage_entry.delete(0, last=len(damage_entry.get())+1)
			ap = int(ap)
			armour = int(armour)
			if armour == 0:
				damage = ap*2
				damage = str(damage)
				damage_entry.insert(0, damage)
				return
			elif ap < armour:
				damage = 'inefficient'
				damage = damage_entry.insert(0, damage)
				return
			else:
				damage = (ap-armour)/2 + 1
				damage = damage_entry.insert(0, damage)
				return

		ap_label=tk.Label(self, text="Enter AP power")
		ap_label.pack(pady=1, padx=10)
		ap_entry=tk.Entry(self)
		ap_entry.pack(pady=1, padx=10)

		armour_label=tk.Label(self, text="Enter target armour")
		armour_label.pack(pady=1, padx=10)
		armour_entry=tk.Entry(self)
		armour_entry.pack(pady=1, padx=10)

		gun_range_label=tk.Label(self, text="Enter weapon range")
		gun_range_label.pack(pady=1, padx=10)
		gun_range_entry=tk.Entry(self)
		gun_range_entry.pack(pady=1, padx=10)

		range_label=tk.Label(self, text="Enter target range")
		range_label.pack(pady=1, padx=10)
		range_entry=tk.Entry(self)
		range_entry.pack(pady=1, padx=10)

		damage_label=tk.Label(self, text="Damage")
		damage_label.pack(pady=1, padx=10)
		damage_entry=tk.Entry(self)
		damage_entry.pack(pady=5)

		calc_button = ttk.Button(self, text="Calculate!", 
			command = lambda: calculate_KE(calculate_KE_range(ap_entry.get(), 
				gun_range_entry.get(), range_entry.get()), armour_entry.get()))
		calc_button.pack(pady=5)

		Heat_Button = ttk.Button(self, text="HEAT Damage Calculator", 
			command = lambda: controller.show_frame(Heat_Calc))
		Heat_Button.pack(pady=1)

		return_button = ttk.Button(self, text="Go Back",
			command = lambda: controller.show_frame(StartPage))
		return_button.pack()


app = WargameCalcApp()
app.mainloop()