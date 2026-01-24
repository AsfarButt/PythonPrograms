
# import numpy as np
# A = np.array([
#     [1, 2, 2, 3],
#     [4, 4, 4, 2],
#     [3, 3, 1, 1],
#     [2, 2, 2, 5]
# ])

# def Func1(x):
#         value,count = np.unique(x, return_counts=True)
#         a = max(count)
#         b = value[np.argmax(count)]
#         return [b, a]    

# B = np.apply_along_axis(
#     lambda x:
#     (lambda Arr: [Arr[0][np.argmax(Arr[1])],Arr[1].max()])(np.unique(x,return_counts=True))
#     ,axis=1,arr=A)

# print(B)

# import numpy as np

# A = np.array([
#     [1, 2, 2, 3],
#     [4, 4, 4, 2],
#     [3, 3, 1, 1],
#     [2, 2, 2, 5]
# ])

# B = np.apply_along_axis(
#     lambda x:
#         (lambda a: [a[0][np.argmin(a[1])],a[1].min()])(np.unique(x, return_counts=True)),
#         axis=1,arr=A
# )
# print(B)

# import numpy as np

# A = np.array([
#     [1, 2, 2, 3],
#     [4, 4, 4, 2],
#     [3, 3, 1, 1],
#     [2, 2, 2, 5]
# ])

# B = np.apply_along_axis(
#     lambda x:
#         (lambda arr: [arr[0][np.argsort(arr[1])[-1]], np.sort(arr[1])[-1], arr[0][np.argsort(arr[1])[-2]], np.sort(arr[1])[-2]])(np.unique(x,return_counts=True)),
#     axis=1,
#     arr=A
# )

# print(B)

# import numpy as np

# A = np.array([
#     [1, 2, 2, 3],
#     [4, 4, 4, 2],
#     [3, 3, 1, 1],
#     [2, 2, 2, 5]
# ])

# B = np.apply_along_axis(
#     lambda x:
#         (lambda arr2: ([arr2[0][arr2[2][-1]], arr2[1][arr2[2][-1]], arr2[0][arr2[2][-2]], arr2[1][arr2[2][-2]]]))((lambda arr: [arr[0], arr[1], np.argsort(arr[1])])(np.unique(x,return_counts=True))),
#     axis=1,
#     arr=A
# )

# print(B) 

# import numpy as np

# A = np.array([
#     [10, 50, 20, 40],
#     [ 5,  1,  9,  3],
#     [100, 60, 80, 70]
# ])

# B = np.apply_along_axis(
#     lambda x:
#         (lambda y: [y[0][y[1][-1]], y[0][y[1][-2]]])([x, np.argpartition(x,-2)]),
#         axis=1,
#         arr=A
# )
# # print(B)imp

# import numpy as np

# A = np.array([
#     [10, 50, 20, 40],
#     [ 5,  1,  9,  3],
#     [100, 60, 80, 70]
# ])

# indices =  np.argpartition(A,-2,axis=1)[:,-2:]
# print(indices)
# U_A = np.take_along_axis(A,indices,axis=1)
# print(U_A)

import numpy as np

A = np.array([
    [12, 5, 30, 8],
    [ 7, 25, 10, 3],
    [20, 15, 18, 2]
])

indices = np.argmax(A,axis=1)
print(indices)
B = np.take_along_axis(A,indices,axis=1)
print(B)
print(indices)