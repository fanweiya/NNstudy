import numpy as np
#
# array1 = np.ndarray([1,2,3],[2,3,4])
# print(array1)
# print('number of dim:',array1.dim)
# print('shape:',array1.shape)
# print('size:',array1.size)
#
# a= np.zeros((3,4))
# b=np.linspace(1,10,6).reshape((3,5))
# c=np.arange(4)
# d=10*np.sin(c)
#
# c_dot=np.dot(a,b)
# c_dot_2=a.dot(b)
#
# e=np.random.random((2,2))
#
# print(e)

#索引
a=np.arange(3,15).reshape((3,4))
print(a)
print(a[2])
print(a[1,1:2])
for row in a:
    print(row)
for col in a.T:
    print(col)

print(a.flatten())
for item in a.flat:
    print(item)

#合并

import numpy as np

a=np.array([1,1,1])
b=np.array([2,2,2])

c=np.vstack((a,b))
d=np.hstack((a,b))

print(c)

print(d)

print(a.shape,d.shape)

print(a[np.newaxis,:])

print(a[:,np.newaxis])

c=np.array([1,1,1])[:,np.newaxis]

c=np.concatenate((a,b,b,a),axis=0)
d=np.concatenate((a,b,b,a),axis=1)

print(c)
print(d)

#分割


import numpy as np

a=np.arange(12).reshape((3,4))

print(a)

print(np.split(a,2,axis=1))


print(np.split(a,3,axis=0))

print(np.vsplit(a,3))

print(np.hsplit(a,2))


#赋值

import numpy as np

a=np.arange(4)

print(a)

b=a
c=a
d=b

a[0]=5

print(a)

print(b,c,d)

print(b is a)

d[1:3]=[22,33]
print(d,a)

e=a.copy()

print(e is a)

