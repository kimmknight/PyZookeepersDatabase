import json
animals=['Tiger','Rhino','Elephant','Octopus','Polar Bear']
animals.sort()
def print_all_animals():
	A=1
	for B in animals:C=str(A)+' '+B;print(C);A=A+1
while 1:
	print("\nZookeeper's Database\n**********************\n\n1:  Print Animals List\n2:  Add Animal\n3:  Delete Animal\n4:  Exit\n\n**********************\n");menu_selection=input('Please make a selection: ')
	if menu_selection=='1':print_all_animals()
	elif menu_selection=='2':new_animal=input('Enter new animal: ');animals.append(new_animal);animals.sort()
	elif menu_selection=='3':print_all_animals();animal_number_to_delete=input('Animal number to delete: ');animal_number_to_delete=int(animal_number_to_delete);animal_number_to_delete=animal_number_to_delete-1;del animals[animal_number_to_delete]
	elif menu_selection=='4':break