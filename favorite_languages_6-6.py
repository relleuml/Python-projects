favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people_taken = ['jen', 'sarah']
people_not_taken = ['bob', 'joe']

# looping through a dictionary
for name in favorite_languages.keys():
	print(name.title())

	if name in people_taken:
		print(" Thanks " + name.title() +
		      " for responding to the poll already.")

# looping through a list
for name in people_not_taken:
	print(name.title())
	print( " Hi " + name.title() + ", please take the poll.")


# if people_taken in set(favorite_languages.keys()):
# 	print("Thanks " + favorite_languages.title().keys())

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#         language.title() + ".")
