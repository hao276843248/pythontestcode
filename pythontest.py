# init
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
# 维数 2维
print(array.ndim)
# 行列数（2,3）
print(array.shape)
# 元素个数
print(array.size)
# 生成0站位的array
a = np.zeros((3, 4))
# 生成 【star ， stop 个数】 的array 线段内的点
a = np.linspace(1, 20, 21)
b = np.zeros(4)
c = np.arange(4)
# np 加法运算
print(b + c)  # [0. 1. 2. 3.]
# np 加法运算
print(b - c)  # [ 0. -1. -2. -3.]
# np 加法运算
print(b * c)  # [0. 0. 0. 0.]
# np 除
print(c / b)  # [nan inf inf inf]
print("&" * 29)
# 求值
A = np.arange(12).reshape((4, 3))
print(A)
# 每一位是前几位的和。[1,2,3]=[1,3,6] axis  0 纵向。1横向
print(A.cumsum(0))
print(np.cumsum(A, 0))
# [[ 0  1  2]
# [ 3  5  7]
# [ 9 12 15]
# [18 22 26]]

# 5.5 求平均值 3种方式
print(A.mean())
print(np.average(A))
print(np.mean(A))
# 取得值为最大值序列
print(A.max())  # 11
# 纵向求最大值 1横向求最大值
print(np.max(A, 0))  # [ 9 10 11]
print(np.max(A, 1))  # [ 2  5  8 11]
# 取得值为最小值序列
print(A.min())  # 最小序列 0

# 三角函数
print(np.sin(A))  # 每个值的sin值
# [[ 0.          0.84147098  0.90929743]
# [ 0.14112001 -0.7568025  -0.95892427]
# [-0.2794155   0.6569866   0.98935825]
# [ 0.41211849 -0.54402111 -0.99999021]]
print(np.cos(a))
print(np.tan(a))
print("%%%%%%%%" * 29)
a = np.random.random((3, 4))
# 序列排序 序列 axis 总是 0 纵向 1横向排序 默认为-1
print(np.argsort(a, axis=None))
# [[0 2 0 0]
#  [2 0 1 1]
#  [1 1 2 2]]
print(np.sort(a, axis=1))
# [[0.14169547 0.32314967 0.44123913 0.51404863]
#  [0.21702596 0.49495577 0.61901096 0.65376785]
#  [0.15591303 0.58022679 0.60854734 0.83725538]]

# 最大最小值替换，最大值替换6，最小值替换1
print(np.clip(a, 1, 6))
a.clip(1, 6)
# 行列变化
print(np.transpose(a))
print(a.T)
# reshape 重置 行列
a = np.arange(3, 15).reshape((3, 4))
# 索引取值
print(a)
print(a[1][2])
print(a[:, 2])
print("*" * 19)
for row in a:
    print(row)
print("*" * 19)
for row in a.T:
    print(row)
print("*" * 19)
print(a.flatten())
print("*" * 19)
for i in a.flat:
    print(i)
# 合并
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
# 上下合并 变多维数组
C = np.vstack((A, B))
print(C)
# 左右合并变单维
D = np.hstack((A, B))
print(D)
# 增加纬度。 【1,1,1】 =[[1],[1],[1]]
print(A[np.newaxis, :])
# 自定义横向纵向合并，0 纵向 1横向
c = np.concatenate((A, B, A, B), axis=1)
print(c)
print("$" * 19)
# 分割
A = np.arange(12).reshape((3, 4))
A = np.arange(12)
print(A)

print("$" * 19)
# 相等分割，0 纵向， 1横向
print(np.split(A, 2, axis=1))
print(A.vsplit(2, 1))
# 不等分割
print(np.array_split(A, 3, axis=0))
# 横向分割 3组 【【】，【】，【】】 = 【【】】，【【】】，【【】】
print(np.vsplit(A, 3))
