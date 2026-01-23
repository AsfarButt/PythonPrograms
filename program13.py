# # import numpy as np


# # A = np.array([5, 10, 15, 20])

# # A = A.astype(float)

# # print(A.dtype)

# import numpy as np

# # A = np.array([5.12,8,20,3,15])
# # A[A > 10] = 10
# # A[A < 5] = 5

# # print(A)

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# # ])

# # B = A.sum(axis=1)
# # print(B)

# import numpy as np

# A = np.array([
#     [2, 4, 6],
#     [1, 3, 5],
#     [10, 20, 30]
# ])

# B = (A - A.min()) / (A.max() - A.min())

# # print(round(B,2))

# import numpy as np

# A = np.array([ [2, 4, 6], [1, 3, 5], [10, 20, 30] ])

# r = A.sum(axis=1, keepdims=True)
# B = A.r
# # B = np.round(B,2)
# # print(B)
# import numpy as np
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# c = A.sum(axis=0)
# B = A/c
# B = np.round(B,2)
# print(B)

# import numpy as np

# A = np.array([
#     [12, 5, 7],
#     [3, 18, 10],
#     [9, 2, 20]
# ], dtype = float)

# A[A<5] = np.nan


# print(np.round(np.nanmean(A),2))

# import numpy as np

# A = np.array([
#     [5, 12, 7],
#     [20, 3, 10],
#     [8, 15, 2]
# ], dtype=float)

# A[A<5] = np.nan
# print(np.nanmean(A, axis=1))

# import numpy as np

# A = np.array([
#     [4, 10, 6],
#     [8, 2, 20],
#     [1, 15, 9]
# ], dtype=float)

# A[A<5] = np.nan
# r = np.nansum(A, axis=1, keepdims=True)
# B = A/r

# print(np.round(B,2))

# import numpy as np

# A = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# B = A[A%20==0]

# print(B)
# import numpy as np

# A = np.array([
#     [5, 10, 15, 20],
#     [25, 30, 35, 40],
#     [45, 50, 55, 60]
# ])

# row_indexes = [0, 1, 2, 2]
# col_indexes = [1, 3, 0, 3]

# B = A[row_indexes, col_indexes]

# print(B)

# import numpy as np

# A = np.array([40, 10, 70, 20, 60, 30])

# B = np.argsort(A)
# print(B)
# A = A[B]

# print(A[-1:-4:-1])

# import numpy as np

# A = np.array([5, 12 ,3, 20, 8, 15])

# B = np.where(A<10, 0,1)

# print(B)

# import numpy as np

# A = np.array([4, 9, 15, 22, 7, 30])

# B = np.where(A%2==0, A,-1)

# print(B)
# import numpy as np

# A = np.array([3, 8, 15, 22, 7, 30, 11])

# B = np.where(A<10, 0, np.where(A<20, 1, 2))
# # print(B)

# import numpy as np

# A = np.array([1,2, 3,3,3,4,4,5])
# value, count = np.unique(A, return_counts=True)

# print(value, count)

# import numpy as np

# A = np.array([4, 4, 2, 8, 2, 4, 8, 8, 8])
# value, count = np.unique(A,return_counts=True)
# print(value[np.argmax(count)])
# print(count.max())

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
#     ((lambda x, y: [x[np.argmax(y)],y.max()])(lambda y:  np.unique(y,return_counts=True)))(x)
#     ,axis=1,arr=A)

# print(B)

