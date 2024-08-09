import json
import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Directory containing the JSON annotation files
annotations_dir = 'E:/2024/SIH Projects/image_recognition_chatbot/data/annotations/'

# Output CSV file paths
train_csv_path = 'E:/2024/SIH Projects/image_recognition_chatbot/data/text/train.csv'
val_csv_path = 'E:/2024/SIH Projects/image_recognition_chatbot/data/text/val.csv'

# List to store data for the CSV file
data = []

# Read each JSON file in the annotations directory
for filename in os.listdir(annotations_dir):
    if filename.endswith('.json'):
        with open(os.path.join(annotations_dir, filename), 'r') as f:
            annotations = json.load(f)
            # Extract relevant information from annotations
            for annotation in annotations['annotations']:
                # Assuming annotation contains 'caption' or 'description' and 'image_id'
                caption = annotation.get('caption', '')  # Or the relevant field name
                image_id = annotation.get('image_id', '')
                data.append({'text': caption, 'image_id': image_id})

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Split the data into training and validation sets
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

# Save the DataFrames to CSV files
train_df.to_csv(train_csv_path, index=False)
val_df.to_csv(val_csv_path, index=False)

print(f"Training CSV file created at {train_csv_path}")
print(f"Validation CSV file created at {val_csv_path}")
