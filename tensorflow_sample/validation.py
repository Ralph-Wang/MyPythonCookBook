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

california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")


def preprocess_features(california_housing_dataframe):
    """ Prepares input features from California housing data set.

    Args:
        california_housing_dataframe: A Pandas DataFrame expected to contain
        data from the California house data set.
    Returns:
        A DataFrame that contains the features to be used for the model,
        including synthetic features
    """
    selected_features = california_housing_dataframe[
            [
                "latitude",
                "longitude",
                "housing_median_age",
                "total_rooms",
                "total_bedrooms",
                "population",
                "households",
                "median_income"
                ]
            ]
    processed_features = selected_features.copy()

    # Create a synthetic feature.
    processed_features["rooms_per_person"] = (
            california_housing_dataframe["total_rooms"] /
            california_housing_dataframe["population"]
            )

    return processed_features

def preprocess_targets(california_housing_dataframe):
    """ Prepares target features (i.e., labels) from California housing data
    set.

    Args:
        california_housing_dataframe: A Pandas DataFrame expected to contain
        data from the California house data set.
    Returns:
        A DataFrame that contains the target feature.
    """
    output_targets = pd.DataFrame()
    # Scale the target to be in units of thousands of dollars.
    output_targets["median_house_value"] = (
            california_housing_dataframe["median_house_value"] / 1000.0
            )
    return output_targets


california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))

# training sets
training_size = 12000

training_examples = preprocess_features(california_housing_dataframe.head(training_size))

training_targets = preprocess_targets(california_housing_dataframe.head(training_size))


# validation sets
validation_size = 5000

validation_examples = preprocess_features(california_housing_dataframe.tail(validation_size))

validation_targets = preprocess_targets(california_housing_dataframe.tail(validation_size))




# print( "=" * 20, "Training Examples" )
# print( training_examples.describe() )
# print( "=" * 20, "Training Targets" )
# print( training_targets.describe() )
# print( "=" * 20, "Validation Examples" )
# print( validation_examples.describe() )
# print( "=" * 20, "Validation Targets" )
# print( validation_targets.describe() )
# print( "=" * 20 )


def draw_latitude_and_longitude():
    plt.figure(figsize=(13, 8))

    ax = plt.subplot(1, 2, 1)
    ax.set_title("Validation Data")

    ax.set_autoscaley_on(False)
    ax.set_ylim([32, 43])
    ax.set_autoscalex_on(False)
    ax.set_xlim([-126, -112])

    plt.scatter(validation_examples["longitude"],
            validation_examples["latitude"],
            cmap="coolwarm",
            c=validation_targets["median_house_value"] /
            validation_targets["median_house_value"].max())

    ax = plt.subplot(1, 2, 2)
    ax.set_title("Training Data")

    ax.set_autoscaley_on(False)
    ax.set_ylim([32, 43])
    ax.set_autoscalex_on(False)
    ax.set_xlim([-126, -112])

    plt.scatter(training_examples["longitude"],
            training_examples["latitude"],
            cmap="coolwarm",
            c=training_targets["median_house_value"] /
            training_targets["median_house_value"].max())

    plt.plot()

# draw latitude and longitude to check whether the data is available
# draw_latitude_and_longitude()
# plt.show()

def my_input_fn(features, targets, batch_size = 1, shuffle = True, num_epochs = None):
    # Convert a dataset, and configure batching/repeating
    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct pandas data into a dict of np arrays
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds = ds.shuffle(10000)

    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


def construct_feature_columns(input_features):
    """ Construct the Tensorflow Feature Columns.

    Args:
        input_features: The names of the numerical input features to use.
    Returns:
        A set of feature columns
    """
    return set([tf.feature_column.numeric_column(my_feature)
        for my_feature in input_features])

def train_model(
        learning_rate,
        steps,
        batch_size,
        training_examples,
        training_targets,
        validation_examples,
        validation_targets
        ):
    """
    """

    periods = 10
    steps_per_period = steps / periods

    # Create a linear regressor object.
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
            feature_columns = construct_feature_columns(training_examples),
            optimizer = my_optimizer
            )

    # 1. Create input functions.
    training_input_fn = lambda: my_input_fn(training_examples, training_targets, batch_size=batch_size)
    predict_training_input_fn = lambda: my_input_fn(training_examples, training_targets, num_epochs=1, batch_size=batch_size, shuffle=False)
    predict_validation_input_fn = lambda: my_input_fn(validation_examples, validation_targets, num_epochs=1, shuffle=False,batch_size=batch_size)

    # Train the model, but do so inside a loop so that we can periodically
    # assess loss metrics.
    print( "Training model..." )
    print( "RMSE (on training data)" )
    training_rmse = []
    validation_rmse = []

    for period in range(0, periods):
        linear_regressor.train(
                input_fn = training_input_fn,
                steps = steps_per_period
                )

        # 2. take a break and compute predictions.
        training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
        validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)

        training_predictions = np.array([item['predictions'][0]
            for item in training_predictions])
        validation_predictions = np.array([item['predictions'][0]
            for item in validation_predictions])

        # Compute training and validation loss.
        training_root_mean_squared_error = math.sqrt(
                metrics.mean_squared_error(training_predictions, training_targets)
                )
        validation_root_mean_squared_error = math.sqrt(
                metrics.mean_squared_error(validation_predictions, validation_targets)
                )

        # print current loss
        print( "  period %02d : %0.2f" % (period, training_root_mean_squared_error) )

        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
    print( "Model training finished." )

    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validaiton")
    plt.legend()

    return linear_regressor

linear_regressor = train_model(
        learning_rate = 0.00003,
        steps = 500,
        batch_size = 5,
        training_examples = training_examples,
        training_targets = training_targets,
        validation_examples = validation_examples,
        validation_targets = validation_targets
        )

california_housing_test_dataframe = pd.read_csv('california_housing_test.csv', sep=',')

test_examples = preprocess_features(california_housing_test_dataframe)
test_targets = preprocess_targets(california_housing_test_dataframe)
predict_test_input_fn = lambda: my_input_fn(test_examples, test_targets, num_epochs=1, batch_size=5, shuffle=False)
test_predictions = linear_regressor.predict(input_fn=predict_test_input_fn)

test_predictions = np.array([item['predictions'][0] for item in test_predictions])

# Compute loss.
test_root_mean_squared_error = math.sqrt( metrics.mean_squared_error(test_predictions, test_targets))

print( "test RMSE: %0.2f" % test_root_mean_squared_error )

# plt.show()
