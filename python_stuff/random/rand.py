import random

test_int = random.randint(1,10)

test_rnd = random.random()

print('int = ',test_int)
print('random = ', test_rnd)

alist = ['адын',2,'three','четыре',5,6,7]

print('from list = ',random.choice(alist))

atuple = ('i','love','python',5,7,-1)

print('from tuple = ',random.choice(atuple))

astring = 'String is a sequence too, by the way'

print('from string = ',random.choice(astring))