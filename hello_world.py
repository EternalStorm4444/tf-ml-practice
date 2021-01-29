#imports tensorflow v2 with some extra swag
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
print('Importing tensorflow... ' + tf.__version__)

import numpy as np
from tensorflow import keras

#layer - one neuron
neuron = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
    ]
)
print("built")

#mean squared error and stochastic gradient descent
neuron.compile(optimizer='sgd', loss='mean_squared_error')

#feed it data numpy array
#y=3x+1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
print("data loaded")

#train
neuron.fit(xs, ys, epochs=50)

print(neuron.predict([13.0]))
