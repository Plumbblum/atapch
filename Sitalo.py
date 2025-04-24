import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import time
import threading

class AcidRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("РЕГИСТРАЦИЯ")
        self.root.geometry("600x700")
        
        # Неоновые цвета
        self.neon_colors = [
            "#FF00FF",  # Неоновый розовый
            "#00FFFF",  # Неоновый голубой
            "#FF0000",  # Неоновый красный
            "#00FF00",  # Неоновый зеленый
            "#FFFF00",  # Неоновый желтый
            "#FE01B1",  # Яркий розовый
            "#0FF0FC",  # Яркий циан
            "#08F7FE",  # Электрический синий
            "#FE01B1",  # Горячий розовый
            "#3AF9EF",  # Неоновая мята
        ]
        
        # Переменные для хранения данных формы
        self.username_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()
        
        # Создание холста для психоделического фона
        self.canvas = tk.Canvas(root, width=600, height=700)
        self.canvas.pack(fill="both", expand=True)
        
        # Создание психоделического фона
        self.bg_shapes = []
        self.create_psychedelic_background()
        
        # Создание основного фрейма для формы
        self.main_frame = tk.Frame(self.canvas, bg="#111111", bd=5)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=600)
        
        # Создание и размещение элементов формы
        self.create_widgets()
        
        # Запуск анимации
        self.animate_background()
        self.animate_labels()
        
    def create_psychedelic_background(self):
        # Создание психоделического фона с разноцветными формами
        for _ in range(50):
            x = random.randint(0, 600)
            y = random.randint(0, 700)
            size = random.randint(20, 100)
            color = random.choice(self.neon_colors)
            shape_type = random.choice(["oval", "rectangle", "polygon"])
            
            if shape_type == "oval":
                shape = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
            elif shape_type == "rectangle":
                shape = self.canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline="")
            else:
                points = []
                for i in range(5):
                    angle = 2 * math.pi * i / 5
                    px = x + size/2 * math.cos(angle)
                    py = y + size/2 * math.sin(angle)
                    points.extend([px, py])
                shape = self.canvas.create_polygon(points, fill=color, outline="")
            
            self.bg_shapes.append({"shape": shape, "type": shape_type, "x": x, "y": y, "size": size})
    
    def animate_background(self):
        # Анимация фоновых элементов
        def update_background():
            while True:
                for shape_info in self.bg_shapes:
                    shape = shape_info["shape"]
                    color = random.choice(self.neon_colors)
                    self.canvas.itemconfig(shape, fill=color)
                    
                    # Случайное перемещение
                    dx = random.randint(-5, 5)
                    dy = random.randint(-5, 5)
                    self.canvas.move(shape, dx, dy)
                    
                    # Обновление координат
                    shape_info["x"] += dx
                    shape_info["y"] += dy
                    
                    # Возвращение на экран, если вышло за границы
                    x, y = shape_info["x"], shape_info["y"]
                    if x < -100 or x > 700 or y < -100 or y > 800:
                        self.canvas.moveto(shape, random.randint(0, 600), random.randint(0, 700))
                        shape_info["x"] = random.randint(0, 600)
                        shape_info["y"] = random.randint(0, 700)
                
                time.sleep(0.1)
        
        # Запуск анимации в отдельном потоке
        bg_thread = threading.Thread(target=update_background, daemon=True)
        bg_thread.start()
    
    def animate_labels(self):
        # Анимация текстовых меток
        def update_labels():
            while True:
                for label in self.animated_labels:
                    color = random.choice(self.neon_colors)
                    label.config(fg=color)
                time.sleep(0.2)
        
        # Запуск анимации в отдельном потоке
        label_thread = threading.Thread(target=update_labels, daemon=True)
        label_thread.start()
    
    def create_widgets(self):
        # Заголовок с анимированным текстом
        title_frame = tk.Frame(self.main_frame, bg="#111111")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="РЕГИСТРАЦИЯ", 
                              font=("Impact", 24, "bold"), 
                              fg=self.neon_colors[0], bg="#111111")
        title_label.pack()
        
        # Основная форма
        form_frame = tk.Frame(self.main_frame, bg="#111111")
        form_frame.pack(pady=10)
        
        # Стиль для полей ввода
        style = ttk.Style()
        style.configure("Neon.TEntry", fieldbackground="#111111", foreground="#00FFFF", 
                       bordercolor=self.neon_colors[0], borderwidth=2)
        
        # Имя пользователя
        username_frame = tk.Frame(form_frame, bg="#111111", pady=10)
        username_frame.pack(fill="x")
        
        username_label = tk.Label(username_frame, text="ТВОЙ ПСЕВДОНИМ:", 
                                 font=("Impact", 14), fg=self.neon_colors[1], bg="#111111")
        username_label.pack(anchor="w")
        
        username_entry = tk.Entry(username_frame, textvariable=self.username_var, 
                                 font=("Arial", 12), bg="#111111", fg="#00FFFF", 
                                 insertbackground="#00FFFF", width=40,
                                 highlightbackground=self.neon_colors[1],
                                 highlightcolor=self.neon_colors[1],
                                 highlightthickness=2)
        username_entry.pack(fill="x", pady=5)
        
        # Email
        email_frame = tk.Frame(form_frame, bg="#111111", pady=10)
        email_frame.pack(fill="x")
        
        email_label = tk.Label(email_frame, text="ТВОЙ ЭЛЕКТРОННЫЙ АДРЕС:", 
                              font=("Impact", 14), fg=self.neon_colors[2], bg="#111111")
        email_label.pack(anchor="w")
        
        email_entry = tk.Entry(email_frame, textvariable=self.email_var, 
                              font=("Arial", 12), bg="#111111", fg="#00FFFF", 
                              insertbackground="#00FFFF", width=40,
                              highlightbackground=self.neon_colors[2],
                              highlightcolor=self.neon_colors[2],
                              highlightthickness=2)
        email_entry.pack(fill="x", pady=5)
        
        # Пароль
        password_frame = tk.Frame(form_frame, bg="#111111", pady=10)
        password_frame.pack(fill="x")
        
        password_label = tk.Label(password_frame, text="СЕКРЕТНЫЙ КОД:", 
                                 font=("Impact", 14), fg=self.neon_colors[3], bg="#111111")
        password_label.pack(anchor="w")
        
        password_entry = tk.Entry(password_frame, textvariable=self.password_var, 
                                 font=("Arial", 12), bg="#111111", fg="#00FFFF", 
                                 insertbackground="#00FFFF", width=40, show="★",
                                 highlightbackground=self.neon_colors[3],
                                 highlightcolor=self.neon_colors[3],
                                 highlightthickness=2)
        password_entry.pack(fill="x", pady=5)
        
        # Подтверждение пароля
        confirm_frame = tk.Frame(form_frame, bg="#111111", pady=10)
        confirm_frame.pack(fill="x")
        
        confirm_label = tk.Label(confirm_frame, text="ПОВТОРИ СЕКРЕТНЫЙ КОД:", 
                                font=("Impact", 14), fg=self.neon_colors[4], bg="#111111")
        confirm_label.pack(anchor="w")
        
        confirm_entry = tk.Entry(confirm_frame, textvariable=self.confirm_password_var, 
                                font=("Arial", 12), bg="#111111", fg="#00FFFF", 
                                insertbackground="#00FFFF", width=40, show="★",
                                highlightbackground=self.neon_colors[4],
                                highlightcolor=self.neon_colors[4],
                                highlightthickness=2)
        confirm_entry.pack(fill="x", pady=5)
        
        # Кнопки с неоновым эффектом
        button_frame = tk.Frame(self.main_frame, bg="#111111")
        button_frame.pack(pady=20)
        
        # Функция для создания неоновой кнопки
        def create_neon_button(parent, text, command, color):
            frame = tk.Frame(parent, bg=color, padx=2, pady=2)
            btn = tk.Button(frame, text=text, command=command,
                           font=("Impact", 14), bg="#111111", fg=color,
                           activebackground=color, activeforeground="#111111",
                           relief=tk.FLAT, padx=20, pady=10)
            btn.pack()
            return frame
        
        # Кнопка регистрации
        register_btn_frame = create_neon_button(button_frame, "ЗАРЕГИСТРИРОВАТЬСЯ", 
                                              self.register_user, self.neon_colors[0])
        register_btn_frame.grid(row=0, column=0, padx=10)
        
        # Кнопка очистки
        clear_btn_frame = create_neon_button(button_frame, "ОЧИСТИТЬ", 
                                           self.clear_form, self.neon_colors[1])
        clear_btn_frame.grid(row=0, column=1, padx=10)
        
        # Статус
        self.status_label = tk.Label(self.main_frame, text="", 
                                    font=("Impact", 12), fg=self.neon_colors[5], bg="#111111")
        self.status_label.pack(pady=10)
        
        # Список анимированных меток
        self.animated_labels = [title_label, username_label, email_label, 
                               password_label, confirm_label, self.status_label]
    
    def register_user(self):
        # Получение данных из формы
        username = self.username_var.get()
        email = self.email_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()
        
        # Проверка заполнения всех полей
        if not (username and email and password and confirm_password):
            self.flash_message("ЗАПОЛНИ ВСЕ ПОЛЯ!!!")
            return
        
        # Проверка email (простая)
        if "@" not in email or "." not in email:
            self.flash_message("ЭТО НЕ ПОХОЖЕ НА EMAIL!!!")
            return
        
        # Проверка совпадения паролей
        if password != confirm_password:
            self.flash_message("ПАРОЛИ НЕ СОВПАДАЮТ!!!")
            return
        
        # Успешная регистрация
        self.flash_message("РЕГИСТРАЦИЯ УСПЕШНА!!!", success=True)
        self.clear_form()
    
    def flash_message(self, message, success=False):
        # Мигающее сообщение
        def flash():
            colors = self.neon_colors if success else ["#FF0000", "#FFFF00"]
            for _ in range(10):
                for color in colors:
                    self.status_label.config(text=message, fg=color)
                    time.sleep(0.1)
        
        flash_thread = threading.Thread(target=flash)
        flash_thread.daemon = True
        flash_thread.start()
    
    def clear_form(self):
        # Очистка полей формы
        self.username_var.set("")
        self.email_var.set("")
        self.password_var.set("")
        self.confirm_password_var.set("")

def main():
    root = tk.Tk()
    root.configure(bg="black")
    app = AcidRegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()