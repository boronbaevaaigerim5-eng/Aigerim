# задача № 1 

def past(h, m, s):
  result = (h * 3600 + m * 60 + s) * 1000
  return result 

print(past(0, 1, 1))

# задача №2     
def invert(ist):
    return [-x for x in ist ]

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))
print(invert([]))

# задача№3
def boolean_to_string(b):
    return str(b)
print(boolean_to_string(True))
print(boolean_to_string(False))




#задача 4
def make_upper_case(s):
    return s.upper() 
print (make_upper_case("hello"), "HELLO")
 