def main(choice):
	choice = int(choice)
	if choice == 1:
		heat = int(input("Please input the AP damage: "))
		armour = int(input("Please input the armour of the target: "))
		calculate_HEAT(heat,armour)
		print("Hit the target for " + str(calculate_HEAT(heat,armour)) + " damage.")
	elif choice == 2:
		ap = int(input("Please input the AP damage: "))
		gun_range = int(input("Please input the effective range of the weapon: "))
		actual_range = int(input("Please input the actual range of the target: "))
		armour = int(input("Please input the armour of the target: "))
		print("Hit the target for " + str(calculate_KE(calculate_KE_range(ap,gun_range,actual_range),armour)) + " damage.")
		return None

def calculate_HEAT(heat,armour):
	if armour <= heat:
		damage = 1
		return damage
	elif armour == 1:
		damage = heat
		return damage
	elif armour == 0:
		damage = heat*2
		return damage
	elif (armour-10) >= heat:
		damage = 6 + ((armour-10) - heat)
		return damage

def calculate_KE_range(ap,gun_range,actual_range):
	if gun_range < actual_range:
		difference = (actual_range - gun_range)/175
		actual_ap = ap + difference
		return actual_ap
	else:
		return ap

def calculate_KE(ap,armour):
	if armour == 0:
		damage = ap*2
		return damage
	damage = (ap-armour)/2 + 1
	if damage <= 0:
		damage = 'Inefficient!'
	return damage

while True:
	print("1. HEAT damage")
	print("2. KE damage")
	choice = input("What would you like to calculate? ")
	main(choice)
	choice = input("Would you like to make another calculation? Y/N? ")
	if choice == 'y' or choice == 'Y':
		pass
	else:
		break

