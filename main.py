import os

import mpld3
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

from evaluate import evaluate

# set to true if running in a docker container to show plots in the browser
# set to false if running locally to show plots in a native window
DOCKERIZED = True

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=10)

evaluate(model, test_images, test_labels)

prediction = model.predict(test_images)

files = os.listdir(os.getcwd())

if 'images' not in files:
    os.mkdir('images')

fig = plt.figure(figsize=(6, 6))

NUMBER_OF_IMAGES = 5
for i in range(NUMBER_OF_IMAGES):
    plt.subplot(NUMBER_OF_IMAGES, NUMBER_OF_IMAGES, i + 1)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    current_test_label_index = test_labels[i]
    current_test_label = class_names[current_test_label_index]
    current_prediction_index = np.argmax(prediction[i])
    current_wearable = class_names[current_prediction_index]
    plt.xlabel("Actual: " + current_test_label)
    plt.title("Predicted: " + current_wearable)

if DOCKERIZED:
    mpld3.show(ip='0.0.0.0', port=8080)
else:
    plt.show()
