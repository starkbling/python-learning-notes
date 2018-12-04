__author__ = "Alex Li"
import random
from random import randint
checkcode=''
for i in range(5):
    current=random.randrange(0,5)
    if current > i:
         a = random.randint(97, 122)
         b = random.randint(65, 90)
         tmp=chr(random.choice([a,b]))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)