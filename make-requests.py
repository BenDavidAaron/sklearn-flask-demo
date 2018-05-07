import requests
from random import randint
from time import sleep

test_string = 'Foo'
num_tests = 5
bad_arg_num = randint(0,num_tests-1)

for i in range(num_tests):
	print("### New Request")
	x = randint(-9,19)
	y = randint(-9,19)
	if bad_arg_num == i:
		bad_arg_pos = randint(0,1)
		if bad_arg_pos == 1:
			x = test_string
		else:
			y = test_string
	print(f"  {x}\n+ {y}\n-----")
	r = requests.get('http://localhost:33507/backdoor/', params = {'x':x,'y':y})
	sleep(.5)
	sum = r.text
	print(f" {sum}\n")
	sleep(1)