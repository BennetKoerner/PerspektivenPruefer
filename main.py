import tkinter as tk
import os
from PIL import Image, ImageTk
import hashlib
import imagehash


class ImageViewer(tk.Tk):
    def __init__(self, folder):
        super().__init__()
        self.title("Image Viewer")
        self.images = [os.path.join(folder, file) for file in os.listdir(folder) if
                       file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        self.current_index = 0

        self.label = tk.Label(self)
        self.label.pack(padx=10, pady=10)

        self.btn_previous = tk.Button(self, text="Previous", command=self.show_previous)
        self.btn_previous.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_delete = tk.Button(self, text="Delete", command=self.delete_image)
        self.btn_delete.pack(side=tk.BOTTOM, padx=5, pady=5)

        self.btn_next = tk.Button(self, text="Next", command=self.show_next)
        self.btn_next.pack(side=tk.RIGHT, padx=5, pady=5)

        self.show_image()

        self.bind("<Left>", lambda event: self.show_previous())
        self.bind("<Right>", lambda event: self.show_next())
        self.bind("<Down>", lambda event: self.delete_image())

    def show_image(self):
        if 0 <= self.current_index < len(self.images):
            image = Image.open(self.images[self.current_index])
            image = image.resize((800, 800), Image.BILINEAR)
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo

    def show_next(self):
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
            self.show_image()

    def delete_image(self):
        if 0 <= self.current_index < len(self.images):
            os.remove(self.images[self.current_index])
            del self.images[self.current_index]
            if self.current_index == len(self.images):
                self.current_index -= 1
            self.show_image()

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()


def remove_similar_images(folder):
    images = [os.path.join(folder, file) for file in os.listdir(folder) if
               file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    hash_dict = {}
    for image_path in images:
        img = Image.open(image_path)
        img_hash = imagehash.average_hash(img)
        if img_hash in hash_dict:
            os.remove(image_path)
        else:
            hash_dict[img_hash] = image_path

if __name__ == "__main__":
    folder_path = "Images"
    remove_similar_images(folder_path)
    app = ImageViewer(folder_path)
    app.mainloop()
