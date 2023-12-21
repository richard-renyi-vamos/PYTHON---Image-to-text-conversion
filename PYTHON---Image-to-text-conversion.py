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
