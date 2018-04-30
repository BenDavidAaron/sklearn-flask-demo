import requests
from random import randint
from time import sleep

for _ in range(10):
	print("### New Request")
	x = randint(-9,19)
	y = randint(-9,19)
	print(f"  {x}\n+ {y}\n-----")
	r = requests.get('http://localhost:33507/backdoor/', params = {'x':x,'y':y})
	sleep(.5)
	sum = r.text
	print(f" {sum}\n")
	sleep(1)