#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("./california_housing_train.csv", sep=",")


# 随机化数据顺序, 以防止极端排序状态
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))

# 增大 media_house_value 的单位, 以减小数值
california_housing_dataframe["median_house_value"] /= 1000.0

# print(california_housing_dataframe.describe())


# 定义输入特征: total_rooms
my_feature = california_housing_dataframe[["total_rooms"]]

# 把输入特征设置为特征列
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# 定义目标/标签
targets = california_housing_dataframe["median_house_value"]

# 梯度下降
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

# 定义线性回归模型
linear_regressor = tf.estimator.LinearRegressor(
        feature_columns = feature_columns,
        optimizer = my_optimizer
        )


# 定义一个输入函数来告诉 tensorflow 怎么获取学习数据
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    # 将 pandas 的 data 转换成 numpy arrays
    features = {key: np.array(value) for key, value in dict(features).items()}

    # 构造一个 tensorflow 的 Dataset, 并且配置 batching 和 repeating
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    # 按需随机打乱数据
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # 返回下一批次的数据
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

# 训练
_ = linear_regressor.train(
        input_fn = lambda: my_input_fn(my_feature, targets),
        steps=100
        )

# 为预测也创建一个输入函数
# 因为对每条数据只预测一次, 所以不需要打乱数据
prediction_input_fn = lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

# 调用 predict()
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# 用numpy 格式化数据, 方便计算
predictions = np.array([item['predictions'][0] for item in predictions])

# RMSE and min_max_diff
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Min. Median House Value: %0.3f" % min_house_value)
print("Max. Median House Value: %0.3f" % max_house_value)
print("Difference between Min. and Max.: %0.3f" % min_max_difference)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)
# Mean Squared Error (on training data): 56367.025
# Min. Median House Value: 14.999
# Max. Median House Value: 500.001
# Difference between Min. and Max.: 485.002
# Root Mean Squared Error (on training data): 237.417

calibration_data = pd.DataFrame()
calibration_data["predictions"] = pd.Series(predictions)
calibration_data["targets"] = pd.Series(targets)
print(calibration_data.describe())

sample = california_housing_dataframe.sample(n=300)

# 画出回归曲线
x_0 = sample["total_rooms"].min()
x_1 = sample["total_rooms"].max()

weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

y_0 = weight * x_0 + bias
y_1 = weight * x_1 + bias

plt.plot([x_0, x_1], [y_0, y_1], c='r')

plt.ylabel("median_house_value")
plt.xlabel("total_rooms")

# 标出真实测试值
plt.scatter(sample["total_rooms"], sample["median_house_value"])

plt.show()


# train_model(
#         learning_rate=0.00001,
#         steps=100,
#         batch_size=1
#         )
