"""
print("Hello World!")

variable = "Hello World!"
print(variable)

string_variable = "word"
print(string_variable)

int_variable = 7
print(int_variable)

float_variable = 3.14159
print(float_variable)

#print(new_variable)

word = input("Please enter a word: ")
print(word)
"""
'''
name = input("Please enter your name: ")
print("Hello " + name + "!")
age = input("Please enter your age: ")
print("You are " + age + " years old!")

#print("In one year you will be " + (age+1) + " years old!")

int_age = int(age)

print("In one year you will be " + repr(int_age+1) + " years old!")
'''
'''
print(1 == 1)
print(1 == 2)
print("1" == "1")
print("word" != "word")
print(1 == 1.0)
print(1 > 3)
print(5 <= 5)

a = 1
b = 10
print(a <= b)
c = a <= b
print(c)
'''
'''
# conditional: if p then q
# example- If it is sunny, then I will go for a run.
# Statement to translate: If the integer 20 is greater than the integer 10, then tell the user via the command line that the world makes sense.
if (20 > 10):
  print("The world makes sense!")

# Statement to translate: If the integer 20 is greater than the integer 10, then tell the user via the command line that the world makes sense. Otherwise, tell the user via the command line that chaos reigns.
if (20 > 10):
  print("The world makes sense!")
else:
  print("Chaos reigns.")

# Statement to translate: If the integer 20 is equal to the integer 10, then tell the user via the command line that the world makes sense. Else if the integer 10 is equal to the integer 10, tell the user via the command line that you made a typo. Else tell the user via the command line that chaos reigns.
if (20 == 10):
  print("The world makes sense!")
elif (10 == 10):
  print("Oops. I made a typo.")
else:
  print("Chaos reigns.")

# Is this a solution that will work?
if (20 == 10):
  print("The world makes sense!")
if (10 == 10):
  print("Oops. I made a typo.")
else:
  print("Chaos reigns.")
# Structure is not equal to above
'''
# Interactive activity
# Read in someone's name and age with input, store them as variables and print them out.

#name = input("What's your name?: ")
#age = input("How old are you?: ")
#print(name + "" + age)

# Interactive activity
# Read in a person's age (doesn't have to be yours! try a variety of numbers) from the command line. If the person can legally drive (16 or up), print a congratulatory message. Otherwise, if they are a teenager (13 or up), print how many years they have until being able to drive. If they are not a teenager, print their age.
''''
age = input("Please enter your age: ")
int_age = int(age)
if(int_age >= 16):
  print("Congrats! You can drive!")
elif(int_age >= 13):
  print(16-int_age)
else:
  print("Age: " + repr(int_age))
'''
# Final interactive activity
# Create a calculator program that takes in two floating point numbers from the command line and an operation (written as a word) from the command line and prints the result to the command line. It should handle addition (+), subtraction (-), multiplication(*), and division(/). If the operation written by the user is none of those four, print out a message telling the user that.

a = input("Please enter your first number: ")
b = input("Please enter your second number: ")
operator = input("Please enter the operator you'd like to use: ")

float_a = float(a)
float_b = float(b)

if(operator == "add"):
  print(float_a + float_b)
elif(operator == "subtract"):
  print(float_a - float_b)
elif(operator == "multiply"):
  print(float_a * float_b)
elif(operator == "divide"):
  print(float_a / float_b)
else:
  print("That is not a valid operation, please try again.")




'''
# extra stuff on operator overloading / repr() overloading
class Person():
  name = "none"
  age = 0

  def print_a():
    print('a')
  
  def print_b(self):
    print('b')

  def __repr__(self):
    return self.name

p = Person()
Person.print_a()
p.print_b()
# Person.print_b() # doesn't work

p.name = "Jeff"
p.age = 55
print(str(p))
print(repr(p))
print(p.name)
print(p.age)
'''
