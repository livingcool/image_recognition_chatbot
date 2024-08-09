import os
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

# Load the pre-trained MobileNetV2 model with ImageNet weights
model = MobileNetV2(weights='imagenet')

def process_image(image_path, question):
    """
    Processes the image and provides an answer based on the question.
    
    :param image_path: Path to the image file.
    :param question: The question related to the image.
    :return: A string response based on the image and question.
    """
    # Use the model to get predictions
    image_label = get_image_label(image_path)
    
    # Generate a response based on the label and the question
    if image_label:
        return f"Answering your question: '{question}' about the image, which seems to contain: {image_label}."
    else:
        return "Sorry, I can't recognize the image or answer the question."

def get_image_label(image_path):
    """
    Retrieves or generates a label for the image.
    
    :param image_path: Path to the image file.
    :return: A label or description for the image.
    """
    try:
        # Load and preprocess the image
        image = Image.open(image_path).resize((224, 224))
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        # Predict using the pre-trained model
        predictions = model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Generate a string of detected objects with confidence levels
        objects_detected = ", ".join([f"{pred[1]} ({round(pred[2]*100, 2)}%)" for pred in decoded_predictions])
        return objects_detected

    except Exception as e:
        return f"Error processing the image: {e}"
