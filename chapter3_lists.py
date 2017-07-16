# exercise 3-4
guest_list = ['Damon', 'Pitt', 'Deniro', 'Pacino']
current_value = 0
while current_value <= 3:
    print("Hello Mr. " + guest_list[current_value] + ", please accept my invitation to dinner.")
    current_value += 1

# exercise 3-5
print("Unfortunately, Mr. " + guest_list[0] + " can't make it to dinner.")
guest_list[0] = 'Crowe'
current_value = 0
while current_value <= 3:
    print("Hello Mr. " + guest_list[current_value] + ", please accept my invitation to dinner.")
    current_value += 1

# exercise 3-6
print("We've found a bigger dinner table.")
guest_list.insert(0, 'Nieson')
guest_list.insert(2, 'DeCaprio')
guest_list.append('Schriver')
current_value = 0
while current_value <= 6:
    print("Hello Mr. " + guest_list[current_value] + ", please accept my invitation to dinner.")
    current_value += 1

# exercise 3-7
print("Sadly, my new table won't be here in time so I can only invite 2 guests.")
current_value = 0
while current_value <=4:
	uninvited_guest = guest_list.pop(0)
	print("I'm sorry Mr. " + uninvited_guest + ", but I can't invite you to dinner.")
	current_value +=1
	print(guest_list)

current_value = 0
while current_value <=1:
	print("Hello Mr. " + guest_list[current_value] + ", you are still invited to dinner.")
	current_value +=1

# excercise 3-9
# need to cast the len() function to a string to print it
print("The number of people invited to dinner is " + str(len(guest_list)) + ".")

# both of these work to clear out the list
#del guest_list[0]
#del guest_list[0]
del guest_list[:] # guessed at this syntax
print(guest_list)

# exercise 3-8
places_to_see = ['normandy', 'berlin', 'aushwitz', 'berechtsgarden', 'caan']

print("\nOriginal order")
print(places_to_see)

print("\nTemporarily sorted order")
print(sorted(places_to_see))
print(places_to_see)

print("\nTemporarily sorted in reverse order")
print(sorted(places_to_see, reverse=True))
print(places_to_see)

print("\nPermanently sorted in reverse order")
places_to_see.reverse()
print(places_to_see)

print("\nPermanently sorted in reverse order again")
places_to_see.reverse()
print(places_to_see)

print("\nPermanently sort in alphabetical order")
places_to_see.sort()
print(places_to_see)

print("\nPermanently sort in reverse alphabetical order")
places_to_see.sort(reverse=True)
print(places_to_see)



















