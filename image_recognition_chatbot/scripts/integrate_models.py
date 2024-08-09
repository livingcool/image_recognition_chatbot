import tensorflow as tf
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
from PIL import Image
import os

# Load models
image_model = tf.keras.models.load_model('E:/2024/SIH Projects/image_recognition_chatbot/models/image_recognition_model.h5')
tokenizer = BertTokenizer.from_pretrained('E:/2024/SIH Projects/image_recognition_chatbot/models/nlp_model')
nlp_model = BertForSequenceClassification.from_pretrained('E:/2024/SIH Projects/image_recognition_chatbot/models/nlp_model')

def recognize_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    predictions = image_model.predict(image_array)
    return predictions

def generate_response(query):
    inputs = tokenizer(query, return_tensors="pt")
    outputs = nlp_model(**inputs)
    logits = outputs.logits
    predicted_class = np.argmax(logits.detach().numpy())
    return predicted_class

# Example usage
image_path = 'path_to_image.jpg'
query = 'What is in this image?'
predicted_object = recognize_image(image_path)
response = generate_response(query)
print(f'Predicted Object: {predicted_object}')
print(f'Response: {response}')
