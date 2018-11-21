import module as imp
import datetime

a = 5; b = 6.2; c = 7
array = [1,4,3,2,7,9,6]
tup = (3,5,(4,3))
y = array   #aponta pra o mesmo objeto Python so passa por referencia
# valores sao computados na hora da declaracao
less = []
greater = []
pivot = 5
print a
print b
print c

z = list(array)
print z

for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)

y.append(110)
print greater
print less
print array
type(a)
type(array)

# Python is strongly-typed -> '5' + 5 is false
print(isinstance(a,int))
print "a is %s, b is %s" % (type(a),type(b))
print(a/b)

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: #not is_iterable
        return False

print(imp.f(a))
print(imp.g(a,b))

print(a is b)
print(array is y)

# list != tuple
array[1] = 'mudei'
print(array[1])
#tup[1] = 9 does not work

dt = datetime.datetime(2011,10,29,10,30,22)
print(dt.strftime("%d/%m/%Y %H:%M"))

# test = datetime.strptime('20091031', '%Y%m%d')

print(array)
print(array[::2])
print(array[::-1])
