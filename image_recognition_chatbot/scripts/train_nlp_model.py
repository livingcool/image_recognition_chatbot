from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import pandas as pd

# Load dataset (customize this if needed)
dataset = load_dataset('csv', data_files={'train': 'E:/2024/SIH Projects/image_recognition_chatbot/data/text/train.csv', 'validation': 'E:/2024/SIH Projects/image_recognition_chatbot/data/text/val.csv'})

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(dataset['train'].features['label'].names))

def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation']
)

# Train Model
trainer.train()

# Save the model
model.save_pretrained('E:/2024/SIH Projects/image_recognition_chatbot/models/nlp_model')
tokenizer.save_pretrained('E:/2024/SIH Projects/image_recognition_chatbot/models/nlp_model')
