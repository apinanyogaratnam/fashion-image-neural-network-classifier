import os
import glob
import time

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from evaluate import evaluate

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=10)

evaluate(model, test_images, test_labels, False)

prediction = model.predict(test_images)

files = os.listdir(os.getcwd())
if 'images' not in files: os.mkdir('images')

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    current_test_label_index = test_labels[i]
    current_test_label = class_names[current_test_label_index]
    current_prediction_index = np.argmax(prediction[i])
    current_wearable = class_names[current_prediction_index]
    plt.xlabel(f"Actual {current_test_label}")
    plt.title(f"Prediction {current_wearable}")

    plt.show()

    # image_name = current_test_label.replace(' ', '').lower()
    # plt.savefig(f'images/{image_name}.png', dpi=100)

print('giving the user 300 seconds to view the saves images')
time.sleep(300)
