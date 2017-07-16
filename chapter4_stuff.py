# chapter 4 stuff - 5/29/16
#numbers = list(range(1,21))
#print(numbers)

#values = list(range(1,1000001))
#print(min(values))
#print(max(values))
#print(sum(values))

#odds = list(range(1,21,2))
#for odd in odds:
#	print(odd)

#multiples_of_3 = list(range(3,31,3))
#for mo3 in multiples_of_3:
#	print(mo3)

#cubes = []
#for value in range(1,11):
#	cube = value**3
#	cubes.append(cube)
#	print(cube)

# using a list comprehension
#cubes = [value**3 for value in range(1,11)]
#print(cubes)
# 4-10 - Slices
#print("The first three items in the list are: " + str(cubes[:3]) + ".")
#print("Three items from the middle of the list are: " + str(cubes[3:6]) + "." )
#print("The last three items in the list are: " + str(cubes[-3:]) + ".")

# 4-11
#my_pizzas = ['sausage', 'peperoni', 'cheese']
#print(my_pizzas)
#friend_pizzas = my_pizzas[:]
#print(friend_pizzas)

#my_pizzas.append('veggie')
#friend_pizzas.append('supreme')
#print("My favorite pizzas are: ")
#for mp in my_pizzas:
#	print(mp)
#print("My friend's favorite pizzas are: ")
#for mfp in friend_pizzas:
#	print(mfp)

# 4-13
buffet_foods = ('potatoes', 'pork', 'corn', 'chicken', 'salad')
for bf in buffet_foods:
	print(bf)
# creates an error
#buffet_foods[0] = ('macaroni')
buffet_foods = ('macaroni', 'fish', 'corn', 'chicken', 'salad')
for bf in buffet_foods:
	print(bf)












