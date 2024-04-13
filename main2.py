# As you see me typing try to do the same thing throughout this video

print("Hello, it's great to meet you CJ")
print("Hello, it's great to meet you John")
print("Hello, it's great to meet you Joe")

# OR

def greet(name):
  print(f"Hello, it's great to meet you {name}")
  print("My name is TJ")

# TO INVOKE OR START THIS FUCTION TYPE THIS:
# THIS IS WHERE WE ENTER OUR ARGUMENT. WE WANT TO ADD DATA TO THE FUCTION. GOES HERE:
# VALUE OR VARIBLE GOES IN THE ARGUMENT

greet("cj")



#EX 1 (CONT.)
#2 arguments

def greet(name,age):
  print(f"Hello, it's great to meet you {name}")
  print(f"My name is John. I am {age} years old")


greet("cj", 1)


# Moving on to example # 2 
# I want you now to try to make a function. I want you to call it display_bill.  
# and make 2 aguements in this function. Let the first one be user_name 
# and the second amount_due Almost like the last example. So lets pause the video.

def display_bill(user_name, amount_due):
  print(f"Hello {user_name},")
  print(f"Thank you for your order. Your final balance is ${amount_due}")

display_bill("CJ", 100.99)


#we will talk about something new today about a return.
#return = "statment used to end a function and send a result back to the caller"


def add(num1, num2):
  z = num1 + num2
  print(z)

add(1,2)
