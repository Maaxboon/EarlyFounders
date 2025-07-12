# strings
welcome_message2 = "Welcome to EarlyFounders Bootcamp" # Double quotes
welcome_message1 = 'Welcome to EarlyFounders Python Bootcamp' # Single quotes

print(welcome_message2)
print(welcome_message1)
print(type(welcome_message1))
print(type(welcome_message2))

# Multi  Line strings

multi_line_message = "We are from the African " \
"Leadership University" \
"Learning Python with Early Founders" \
"Bumbogo to the world!"

print(multi_line_message)

# Lenght of a string

name = "Maxtoshi"
length_of_name = len(name)
print(f"Maxtoshi has {length_of_name} characters.")

# Strings modification/methods
print(welcome_message1.upper())
print(welcome_message2.capitalize())

greetings_kenya = "Habari Yako"
print(greetings_kenya.replace("a", "e"))
