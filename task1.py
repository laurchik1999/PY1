from pprint import pprint

c = 16
pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(c)])
