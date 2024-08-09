import tkinter as tk
from tkinter import filedialog, Label, Button, Text, Listbox, Scrollbar, messagebox, Frame
from PIL import Image, ImageTk

# Initialize lists to keep track of images and questions
uploaded_images = []
questions = []

def upload_images():
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        try:
            img = Image.open(file_path)
            img = img.resize((100, 100), Image.LANCZOS)  # Resize for thumbnail
            img_tk = ImageTk.PhotoImage(img)
            uploaded_images.append((file_path, img_tk))
            images_listbox.insert(tk.END, file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open image: {e}")

def display_image(event):
    selected_index = images_listbox.curselection()
    if selected_index:
        file_path = images_listbox.get(selected_index)
        for path, img_tk in uploaded_images:
            if path == file_path:
                image_label.configure(image=img_tk)
                image_label.image = img_tk
                preview_label.config(text=f"Image Preview: {file_path}")
                # Set current image for questions
                global current_image
                current_image = file_path

def submit_question():
    if 'current_image' not in globals():
        messagebox.showwarning("Selection Error", "Please select an image first.")
        return
    
    question = query_entry.get("1.0", tk.END).strip()
    if not question:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return
    
    questions.append((current_image, question))
    questions_listbox.insert(tk.END, f"{current_image}: {question}")
    # Placeholder for chatbot's response
    response = f"Answering your question: '{question}' about {current_image}"
    response_label.config(text=response)

def clear_questions():
    query_entry.delete("1.0", tk.END)
    response_label.config(text="")
    questions_listbox.delete(0, tk.END)

def clear_all():
    uploaded_images.clear()
    questions.clear()
    images_listbox.delete(0, tk.END)
    query_entry.delete("1.0", tk.END)
    response_label.config(text="")
    image_label.configure(image='')
    global current_image
    current_image = None

# Main GUI window
root = tk.Tk()
root.title("Image Recognition Chatbot")
root.configure(bg='white')

# Frame for image upload and display
upload_frame = Frame(root, bg='white', padx=10, pady=10)
upload_frame.pack(side=tk.TOP, fill=tk.X)

upload_label = Label(upload_frame, text="Upload Images", font=('Arial', 14, 'bold'), bg='white', fg='black')
upload_label.pack(pady=(0, 5))

upload_button = Button(upload_frame, text="Upload Images", command=upload_images, width=20, bg='black', fg='white', activebackground='gray')
upload_button.pack(pady=5)

# Frame for image preview
preview_frame = Frame(root, bg='white', padx=10, pady=10)
preview_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

preview_label = Label(preview_frame, text="Image Preview", font=('Arial', 14, 'bold'), bg='white', fg='black')
preview_label.pack(pady=(0, 5))

image_label = Label(preview_frame, bg='lightgray', relief='sunken')
image_label.pack(padx=10, pady=10)

# Frame for image list
list_frame = Frame(root, bg='white', padx=10, pady=10)
list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

list_label = Label(list_frame, text="Uploaded Images", font=('Arial', 14, 'bold'), bg='white', fg='black')
list_label.pack(pady=(0, 5))

images_listbox = Listbox(list_frame, width=50, height=15, bg='white', fg='black', borderwidth=2, relief='groove')
images_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
images_listbox.bind('<<ListboxSelect>>', display_image)

scrollbar = Scrollbar(list_frame, orient=tk.VERTICAL, command=images_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

images_listbox.config(yscrollcommand=scrollbar.set)

# Frame for question input and submission
query_frame = Frame(root, bg='white', padx=10, pady=10)
query_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

query_label = Label(query_frame, text="Ask a Question", font=('Arial', 14, 'bold'), bg='white', fg='black')
query_label.pack(pady=(0, 5))

query_entry = Text(query_frame, height=4, width=40, wrap=tk.WORD, bg='white', fg='black', borderwidth=2, relief='groove')
query_entry.pack(pady=(0, 10))

button_frame = Frame(query_frame, bg='white')
button_frame.pack(fill=tk.X)

submit_button = Button(button_frame, text="Submit Question", command=submit_question, width=20, bg='black', fg='white', activebackground='gray')
submit_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = Button(button_frame, text="Clear Questions", command=clear_questions, width=20, bg='gray', fg='white', activebackground='darkgray')
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_all_button = Button(button_frame, text="Clear All", command=clear_all, width=20, bg='gray', fg='white', activebackground='darkgray')
clear_all_button.pack(side=tk.LEFT, padx=5, pady=5)

# Frame for questions list and response
response_frame = Frame(root, bg='white', padx=10, pady=10)
response_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

response_label = Label(response_frame, text="Chatbot's Response", font=('Arial', 14, 'bold'), bg='white', fg='black')
response_label.pack(pady=10)

questions_listbox = Listbox(response_frame, width=50, height=15, bg='white', fg='black', borderwidth=2, relief='groove')
questions_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_questions = Scrollbar(response_frame, orient=tk.VERTICAL, command=questions_listbox.yview)
scrollbar_questions.pack(side=tk.RIGHT, fill=tk.Y)

questions_listbox.config(yscrollcommand=scrollbar_questions.set)

# Set initial image selection to None
current_image = None

# Start the GUI loop
root.mainloop()
