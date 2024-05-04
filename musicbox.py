import tkinter as tk
from tkinter import filedialog, messagebox
import pygame.mixer

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Müzik Çalıcı")
        
        self.mixer = pygame.mixer
        self.mixer.init()
        
        self.music_list = []
        self.current_index = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Modern Müzik Çalıcı", font=("Arial", 18))
        self.label.pack(pady=10)
        
        self.play_button = tk.Button(self.root, text="Çal", command=self.play_music)
        self.play_button.pack(pady=5, padx=10, ipadx=10)
        
        self.stop_button = tk.Button(self.root, text="Durdur", command=self.stop_music)
        self.stop_button.pack(pady=5, padx=10, ipadx=10)

        self.add_music_button = tk.Button(self.root, text="Müzik Ekle", command=self.add_music)
        self.add_music_button.pack(pady=5, padx=10, ipadx=10)
        
        self.music_listbox = tk.Listbox(self.root, width=50, height=10)
        self.music_listbox.pack(pady=5)
        
        self.play_again_button = tk.Button(self.root, text="Tekrar Çal", command=self.play_again)
        self.play_again_button.pack(pady=5, padx=10, ipadx=10)

        self.play_next_button = tk.Button(self.root, text="Devam Et", command=self.play_next)
        self.play_next_button.pack(pady=5, padx=10, ipadx=10)
        
    def play_music(self):
        selected_index = self.music_listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            selected_music = self.music_list[self.current_index]
            self.mixer.music.load(selected_music)
            self.mixer.music.play()
    
    def stop_music(self):
        self.mixer.music.stop()
        
    def add_music(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 dosyaları", "*.mp3")])
        if file_paths:
            for file_path in file_paths:
                self.music_list.append(file_path)
                self.music_listbox.insert(tk.END, file_path)

    def play_again(self):
        if self.music_list:
            selected_music = self.music_list[self.current_index]
            self.mixer.music.load(selected_music)
            self.mixer.music.play()
        else:
            messagebox.showinfo("Uyarı", "Çalınacak müzik bulunamadı. Lütfen önce bir müzik ekleyin.")
    
    def play_next(self):
        if self.music_list and self.current_index < len(self.music_list) - 1:
            self.current_index += 1
            selected_music = self.music_list[self.current_index]
            self.mixer.music.load(selected_music)
            self.mixer.music.play()
        else:
            messagebox.showinfo("Uyarı", "Sonraki müzik bulunamadı veya son müzik çalınıyor.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
