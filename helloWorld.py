print ("hello World")
'''
#print('Yay! Printing.')
#print("I'd much rather you 'not'.")
#print('I "said" do not touch this.')

print ( "counting is fun")
print ("hens", 25 + 30 / 6)
print ("Is it greater?", 5 > -2)

#variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers,
      "in each car.")

#strings
my_name = 'Lillian'
my_age = 24 /3 # not a lie
my_height = 67 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'

print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall.")
print(f"She's {my_weight} pounds heavy.")
#print("Actually that's not too heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print("Its fleece was white as {}.".format('snow'))
print("." * 10)  # what'd that do?

formatter = "{} and a {} and a {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "a",
    "b",
    "c",
    "d"
))
'''
x = input("something: ")
#print((int)x + 4) #how do i take int input????
