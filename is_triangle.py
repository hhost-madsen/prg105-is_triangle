a = int(raw_input("What is the length of side A?"))
b = int(raw_input("What is the length of side B?"))
c = int(raw_input("What is the length of side C?"))

def is_triangle(a, b, c):

    if a > (b + c):
       print "No"

    elif b > (a + c):
        print "No"

    elif c > (a + b):
        print "No"

    else:
       print "Yes"

is_triangle(a, b, c)
