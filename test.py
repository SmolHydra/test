#some random bits of code practice

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

def gen_username(fname,lname,dob):
  username = lname[0]+fname+str(dob)
  return username
print(gen_username("Rukia","Kuchiki",1857))  #rough dob, never said real age in Bleach

def insult(name,adj):
  if adj[0] in ["a","e","i","o","u"]:
    return name + " is an " + adj
  else:
    return name + " is a " + adj
name = input("Enter the name of the person you want to insult: ")
adj = input("Enter a negative adjective: ")
print(insult(name,adj))

print("idk what else to code")  #probs need to learn more
print("milady") #we like milady
print("you've attracted an audience")
