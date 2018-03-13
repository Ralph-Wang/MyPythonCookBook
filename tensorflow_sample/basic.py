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

def train_model(learning_rate, steps, batch_size, input_feature="total_rooms"):

    periods = 10
    steps_per_period = steps / periods

    # 定义输入特征
    my_feature = california_housing_dataframe[[input_feature]]

    # 把输入特征设置为特征列
    feature_columns = [tf.feature_column.numeric_column(input_feature)]

    training_input_fn = lambda: my_input_fn(my_feature, targets, batch_size=batch_size)
    # 为预测也创建一个输入函数
    # 因为对每条数据只预测一次, 所以不需要打乱数据
    prediction_input_fn = lambda: my_input_fn(my_feature, targets, num_epochs=1, batch_size=batch_size, shuffle=False)

    # 定义目标/标签
    label = "median_house_value"
    targets = california_housing_dataframe[label]

    # 梯度下降
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

    # 定义线性回归模型
    linear_regressor = tf.estimator.LinearRegressor(
            feature_columns = feature_columns,
            optimizer = my_optimizer
            )

    # Set up to plot the state of our model's line each period.
    sample = california_housing_dataframe.sample(n=300)

    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.title("Learned Line by Period")
    plt.ylabel(label)
    plt.xlabel(input_feature)
    plt.scatter(sample[input_feature], sample[label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    # 训练
    print("Training model...")
    print("RMSE (on training data):")
    root_mean_squared_errors = []
    for period in xrange(0, periods):
        _ = linear_regressor.train(
                input_fn = training_input_fn,
                steps=steps_per_period
                )


        # 调用 predict()
        predictions = linear_regressor.predict(input_fn=prediction_input_fn)

        # 用numpy 格式化数据, 方便计算
        predictions = np.array([item['predictions'][0] for item in predictions])

        # RMSE and min_max_diff
        mean_squared_error = metrics.mean_squared_error(predictions, targets)
        root_mean_squared_error = math.sqrt(mean_squared_error)
        # Add RMSE to list
        root_mean_squared_errors.append(root_mean_squared_error)

        print("Root Mean Squared Error (on training data) (period %s): %0.3f" % (period, root_mean_squared_error))
        # Root Mean Squared Error (on training data): 237.417

        # 画出回归曲线
        y_extents = np.array([0, sample[label].max()])

        weight = linear_regressor.get_variable_value('linear/linear_model/%s/weights' % input_feature)[0]
        bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

        x_extents = (y_extents - bias) / weight
        x_extents = np.maximum(np.minimum(x_extents,
                                          sample[input_feature].max()),
                                          sample[input_feature].min())
        y_extents = weight * x_extents + bias
        plt.plot(x_extents, y_extents, color=colors[period])
    print("Model training finished.")

    # Output a graph of loss metrics over period
    plt.subplot(1, 2, 2)
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(root_mean_squared_errors)

    # create a table with calibration data
    calibration_data = pd.DataFrame()
    calibration_data["predictions"] = pd.Series(predictions)
    calibration_data["targets"] = pd.Series(targets)
    display.display(calibration_data.describe())

    print("Final RMSE (on training data): %0.2f" % root_mean_squared_error)
    return calibration_data


## build a synthetic feature
california_housing_dataframe["rooms_per_person"] = california_housing_dataframe["total_rooms"] / california_housing_dataframe["population"]


## clip feature
california_housing_dataframe["rooms_per_person"] = california_housing_dataframe["rooms_per_person"].apply(lambda x: min(x, 5))


calibration_data = train_model(
        learning_rate=0.05,
        steps=500,
        batch_size=5,
        # input_feature="total_rooms"
        input_feature="rooms_per_person"
        )

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.scatter(calibration_data["predictions"], calibration_data["targets"])

plt.subplot(1, 2, 2)
_ = california_housing_dataframe["rooms_per_person"].hist()
plt.show()
