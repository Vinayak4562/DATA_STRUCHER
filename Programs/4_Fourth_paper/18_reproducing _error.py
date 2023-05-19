# reproducing index error
try:
    a = [1,2,3,4]
    print(a[5])
except IndexError:
    print("IndexError: please use proper index value")

# reproducing type error
try:
    a = "vinayak"
    b = 100
    print(a+b)
except TypeError:
    print("TypeError:please give both side str or int")

# reproducing attribute error
try:
    a = "vinayak"
    b = a.append(100)
    print(b)
except AttributeError:
    print("AttributeError:string doesnt have append method")

# reproducing value error
try:
    a = int("vinayak")
    print(a)
except ValueError:
    print("ValueError:give the proper datatype or proper input")