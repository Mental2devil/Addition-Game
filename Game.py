import random
n1 = random.randint(0,9)
n2 = random.randint(0,9)
a = int(input("What is" + str(n1) +  "+" + str(n2) + "?" ))
print(n1, "+",n2, "=",a, "is", n1+n2 == a)
