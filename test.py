print("Hello world")
def greet(name):
  print("Hello",name)
greet("Rukia")

def multiply(num1,num2):
  return num1*num2
num1 = int(input("Enter a integer: "))
num2 = int(input("Enter another integer: "))
result = multiply(num1,num2)
print(f"{num1} x {num2} = {result}")

def gen_pw(fname,lname,dob,punc):
  pw = lname[0]+fname+str(dob)+punc
  return pw
print(gen_pw("Rukia","Kuchiki",1857,"?"))
