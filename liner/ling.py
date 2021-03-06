import numpy as np
data = [[83.0, 234.289, 235.6, 159.0, 107.608, 1947., 60.323],
        [88.5, 259.426, 232.5, 145.6, 108.632, 1948., 61.122],
        [88.2, 258.054, 368.2, 161.6, 109.773, 1949., 60.171],
        [89.5, 284.599, 335.1, 165.0, 110.929, 1950., 61.187],
        [96.2, 328.975, 209.9, 309.9, 112.075, 1951., 63.221],
        [98.1, 346.999, 193.2, 359.4, 113.27, 1952., 63.639],
        [99.0, 365.385, 187., 354.7, 115.094, 1953., 64.989],
        [100.0, 363.112, 357.8, 335.0, 116.219, 1954., 63.761],
        [101.2, 397.469, 290.4, 304.8, 117.388, 1955., 66.019],
        [104.6, 419.18, 282.2, 285.7, 118.734, 1956., 67.857],
        [108.4, 442.769, 293.6, 279.8, 120.445, 1957., 68.169],
        [110.8, 444.546, 468.1, 263.7, 121.95, 1958., 66.513],
        [112.6, 482.704, 381.3, 255.2, 123.366, 1959., 68.655],
        [114.2, 502.601, 393.1, 251.4, 125.368, 1960., 69.564],
        [115.7, 518.173, 480.6, 257.2, 127.852, 1961., 69.331],
        [116.9, 554.894, 400.7, 282.7, 130.081, 1962., 70.551]]
data = np.array(data)
x_data = data[:, 1:]
y_data = data[:, 0, np.newaxis]

X_data = np.concatenate((np.ones((16, 1)), x_data), axis = 1)
# print(np.ones((16, 1)))
# print(X_data)
# print(X_data.shape)


def calc_weights(X_data, y_data, lam=0.4087):
    """
    标准方程法求weights
    算法: weights = (X的转置矩阵 * X矩阵 + lam * I单位矩阵)的逆矩阵 * X的转置矩阵 * Y矩阵
    :param x_data: 特征数据
    :param y_data: 标签数据
    """

    x_mat = np.mat(X_data)
    y_mat = np.mat(y_data)
    xT_x = x_mat.T * x_mat
    lam_xT_x = xT_x + lam * np.eye(x_mat.shape[1])
    if np.linalg.det(lam_xT_x) == 0:
        print("不可逆矩阵，不能使用标准方程法求解")
        return
    weights = lam_xT_x.I * x_mat.T * y_mat
    return weights

lam = calc_weights(X_data, y_data)

print(np.mat(lam))
# print(y_data)
print(X_data.shape)
print(np.mat(lam.shape))
print(np.mat(X_data) * np.mat(lam))