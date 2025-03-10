import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk


class RandomFoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RANDOM FOX")  
        self.fox_image = None
        self.fox_photo = None
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.update_button = tk.Button(
            self.root,
            text="Следующая лисичка",
            command=self.update_image,
            background="orange"
        )
        self.update_button.pack()
        self.update_image()

    def get_fox_image_url(self):
        try:
            response = requests.get("https://randomfox.ca/floof/")
            response.raise_for_status()  
            return response.json()["image"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            return None

    def update_image(self):
        image_url = self.get_fox_image_url()
        if image_url:
            try:
                response = requests.get(image_url, stream=True)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                image = image.resize((500, 400), Image.LANCZOS)
                self.fox_photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=self.fox_photo)
            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomFoxApp(root)
    root.mainloop()