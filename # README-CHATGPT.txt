

User
create a python script that transforms the text from a picture to a text document. 

give it a GUI to select the input picture and an option to choose the output text document name & location
ChatGPT
Absolutely! You can achieve this using Python and a few libraries. One of the most common libraries for this task is pytesseract for text extraction and tkinter for the GUI. You'll also need to have Tesseract OCR installed on your system.

Here's an example script:

python
Copy code
import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from PIL import Image

def extract_text():
    input_image = filedialog.askopenfilename(title="Select Image File",
                                             filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not input_image:
        messagebox.showerror("Error", "No image selected")
        return
    
    output_text = filedialog.asksaveasfilename(title="Save Text File", defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt")])
    if not output_text:
        messagebox.showerror("Error", "No output file selected")
        return
    
    try:
        # Open the image
        img = Image.open(input_image)
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(img)
        
        # Save the extracted text to the output file
        with open(output_text, "w", encoding="utf-8") as file:
            file.write(text)
        
        messagebox.showinfo("Success", "Text extracted and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Image to Text Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=30)

button = tk.Button(frame, text="Select Image", command=extract_text)
button.pack(pady=10)

root.mainloop()
Remember, before running this script, ensure you have the required libraries installed. You can install them via pip:

bash
Copy code
pip install pillow pytesseract
Also, make sure to have Tesseract OCR installed on your system. You can download it from the official GitHub repository: https://github.com/tesseract-ocr/tesseract

This script creates a simple GUI with a button to select an image and save the extracted text to a text file. When you run the script, it'll open a window where you can choose the input image and specify the location and name for the output text file.





