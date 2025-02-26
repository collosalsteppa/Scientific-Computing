#function to ask the user for input
user_input = int(input("Enter an integer:"))

#function to classify number as even or odd
def classify_number(num):
    if num % 2 == 0:
      return "even"
    else:
      return "odd"

classification = classify_number(user_input)
print(f"The number [user_input] is {classification}")

#function that generates even numbers from 1 to 50
even_numbers=[]
for i in range (1,51):
    if i % 2 == 0:
        even_numbers.append(i)
        print("even vumbes from 1 to 50 :",even_numbers)
        #function to print numbers from 10 down to 1 using while loop
        countdown=10
        print("countdown from 10 to 1:")
        while countdown>0:
            print(countdown)
            countdown-=1