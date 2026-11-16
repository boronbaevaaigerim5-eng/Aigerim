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
def no_space(x):
    return "". join(x.split())

print("Fixed Tests")
print('Basic Test Cases')

#задача 5
def get_volume_of_cuboid(length, width, height):
    return length * width * height 

print(get_volume_of_cuboid(6.3, 2, 5), 63)
print(get_volume_of_cuboid(1, 2, 2), 4)


#задача 6
def remove_exclamation_marks(s):
     return s.replace("!","")

print("Fixed Tests")
print('Basic Test Cases')

#7
def simple_multiplication(number) :
    return number *8 if number % 2 ==0 else number *9

print (simple_multiplication(8), 64)
print(simple_multiplication(4), 32) 

# 8
def paperwork(n, m):
    if n<0 or m<0 :
        return 0 
    return n * m

print (paperwork(5,5), 25, "Failed at Paperwork(5,5)")

#9

def number_to_string(num : int) -> str:
    return str (num)

print (number_to_string(67), '67')
print (number_to_string(79585), '79585')

#10
def cockroach_speed(s):
    return int (s* 100000//3600)

print (cockroach_speed(1.08),30)
#11
def repeat_str(repeat, string):
  return string * repeat

# 12
def get_volume_of_cuboid(length, width, height):
    return (length * width * height )

print (get_volume_of_cuboid(1, 2, 2))
print (get_volume_of_cuboid(6.3, 2, 5), 63)

