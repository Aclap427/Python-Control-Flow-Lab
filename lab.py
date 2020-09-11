# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


x = None
while x != 'quit':
  x = input('Please enter a letter from alphabet(a-z or A-Z').lower()
  if x in 'aeiouAEIOU':
    print(f"The letter {x} is a vowel!")
  else:
    print(f"The letter {x} is a consonant")


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = input('Enter a word or phrase: ')
while phrase != 'quit':
    print("The length of what you entered is :", len(phrase))
    break


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

age = int(input("Enter your dogs age in human years: "))
if age <= 2:
  print(f'your dog is {age * 10}')
elif age > 2:
  print(f'your dog is {(age -2) * 7 + 20}')


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

def triangle():
   a = int(input("Provide the length of the first side of a triangle: "))
   b = int(input("Provide the length of the second side of a triangle: "))
   c = int(input("Provide the length of the last side of a triangle: "))
   if a == b and a == c:
       print(f'A triangle with sides of {a}, {b} & {c} is an Equalateral triangle')
   elif a == b or a == b or b == c:
       print(f'A triangle with sides of {a}, {b} & {c} is an Isoceles triangle')
   else:
       print(f'A triangle with sides of {a}, {b} & {c} is a Scalene triangle')
triangle() 



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

a = 1
b = 1
for x in range(0, 51):
    if x == 0:
        print(f'term: {x} / number: 0')
    if x == 1 or x == 2:
        print(f'term: {x} / number: {b}')
    elif x > 2:
        n = a + b
        b = a
        a = n
        print(f'term: {x} / number: {n}')


# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ').capitalize()
day = int(input('Enter the day of the month (01-31): '))
if (month == 'Dec' and day >= 21) or month == 'Jan' or month == 'Feb' or (month == 'Mar' and day <= 19):
    print(f'{month}/{day} is in Winter')
elif (month == 'Mar' and day >= 20) or month == 'Apr' or month == 'May' or (month == 'Jun' and day <= 20):
    print(f'{month}/{day} is in Spring')
elif (month == 'Jun' and day >= 21) or month == 'Jul' or month == 'Aug' or (month == 'Sep' and day <= 21):
    print(f'{month}/{day} is in Summer')
elif (month == 'Sep' and day >= 22) or month == 'Oct' or month == 'Nov' or (month == 'Dec' and day <= 20):
    print(f'{month}/{day} is in Fall')