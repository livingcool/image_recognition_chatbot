import tensorflow as tf

# Load your model
model = tf.keras.models.load_model("path_to_your_model.h5")

# Convert and save as TFLite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

model_path = "C:/Users/Ganesh/Path/To/Your/Model/model.tflite"
with open(model_path, "wb") as f:
    f.write(tflite_model)
