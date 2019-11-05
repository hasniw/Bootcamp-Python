cookbook = {
	"sandwich": {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	},
	"cake": {
		"ingredients": ["flour", "sugar", "eggs", "dessert"],
		"meal": "lunch",
		"prep_time": 60
	},
	"salad": {
		"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "lunch",
		"prep_time": 15
	}
}

def print_recipe(name):
	for values in cookbook[name]:
		if values == "ingredients":
			for items in cookbook[name][values]:
				print(items)
			else:
				print(cookbook[name][values])

#Print keys of the dictionary
print("Print just keys")
for keys in cookbook:
	print(keys)

#Print values of the dictionnary
print("Print all values")
for keys in cookbook:
	for values in cookbook[keys]:
		print(values)
#Print all the items
print("<-------------------->")
for keys in cookbook:
	for values in cookbook[keys]:
		if values == "ingredients":
			for items in cookbook[keys][values]:
				print(items)
		else:
			print(cookbook[keys][values])

def delete_recipe(name):

def add_new_recipe(name):

def print_all
