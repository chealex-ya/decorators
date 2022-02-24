import time
from inspect import signature
import inspect


def sum(a, b):
	print(a + b)
	print(a)
	print(b)


sum(2,5)

def get_arguments():
	sum(2, 5)


arguments = []

sig = signature(sum)

for param in sig.parameters.values():
	if (param.kind == param.POSITIONAL_OR_KEYWORD and param.default is param.empty):
		arguments.append(param)

for i in arguments:
	print(i)

print(inspect.getfullargspec(sum))