import streamlit as st
import random
import math
import time
import threading

class AcidRegistrationForm:
    def init(self):
        self.neon_colors = [
            "#FF00FF", "#00FFFF", "#FF0000", "#00FF00", "#FFFF00",
            "#FE01B1", "#0FF0FC", "#08F7FE", "#FE01B1", "#3AF9EF",
        ]
        self.bg_shapes = []
        self.username_var = ""
        self.email_var = ""
        self.password_var = ""
        self.confirm_password_var = ""
        self.status_message = ""

    def create_psychedelic_background(self):
        st.session_state.bg_shapes = []  # Initialize in session state
        for _ in range(50):
            x = random.randint(0, 600)
            y = random.randint(0, 700)
            size = random.randint(20, 100)
            color = random.choice(self.neon_colors)
            shape_type = random.choice(["oval", "rectangle", "polygon"])
            st.session_state.bg_shapes.append({"type": shape_type, "x": x, "y": y, "size": size, "color": color})

    def draw_background(self):
        # Since Streamlit redraws, just use the stored shapes
        if 'bg_shapes' in st.session_state:
            for shape_info in st.session_state.bg_shapes:
                if shape_info["type"] == "oval":
                    st.write(f'<div style="position: absolute; left: {shape_info["x"]}px; top: {shape_info["y"]}px; width: {shape_info["size"]}px; height: {shape_info["size"]}px; background-color: {shape_info["color"]}; border-radius: 50%;"></div>', unsafe_allow_html=True)
                elif shape_info["type"] == "rectangle":
                    st.write(f'<div style="position: absolute; left: {shape_info["x"]}px; top: {shape_info["y"]}px; width: {shape_info["size"]}px; height: {shape_info["size"]}px; background-color: {shape_info["color"]};"></div>', unsafe_allow_html=True)
                else:  # polygon
                    points = []
                    for i in range(5):
                        angle = 2 * math.pi * i / 5
                        px = shape_info["x"] + shape_info["size"] / 2 * math.cos(angle)
                        py = shape_info["y"] + shape_info["size"] / 2 * math.sin(angle)
                        points.append(f"{px},{py}")
                    points_str = " ".join(points)
                    st.write(f'<div style="position: absolute; left: {shape_info["x"]}px; top: {shape_info["y"]}px;"><svg height="{shape_info["size"]}" width="{shape_info["size"]}"><polygon points="{points_str}" style="fill:{shape_info["color"]};stroke:purple;stroke-width:0;fill-rule:nonzero;"></polygon></svg></div>', unsafe_allow_html=True)

    def animate_background(self):
        if 'bg_shapes' not in st.session_state:
            return  # Ensure bg_shapes is initialized

        for shape_info in st.session_state.bg_shapes:
            shape_info["color"] = random.choice(self.neon_colors)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            shape_info["x"] += dx
            shape_info["y"] += dy

            if shape_info["x"] < -100 or shape_info["x"] > 700 or shape_info["y"] < -100 or shape_info["y"] > 800:
                shape_info["x"] = random.randint(0, 600)
                shape_info["y"] = random.randint(0, 700)
        time.sleep(0.1)
        st.rerun()  # Force Streamlit to redraw

    def animate_labels(self):
        if 'animated_labels' not in st.session_state:
            return

        for label in st.session_state.animated_labels:
            label["color"] = random.choice(self.neon_colors)
        time.sleep(0.2)
        st.rerun()

    def create_widgets(self):
        if 'animated_labels' not in st.session_state:
            st.session_state.animated_labels = []

        st.markdown(f'<h1 style="font-family: Impact; color: {self.neon_colors[0]};">РЕГИСТРАЦИЯ</h1>', unsafe_allow_html=True)
        st.session_state.animated_labels.append({"label": "title", "color": self.neon_colors[0]})
self.username_var = st.text_input("ТВОЙ ПСЕВДОНИМ:", value="",  
                                        )
        st.session_state.animated_labels.append({"label": "username", "color": self.neon_colors[1]})

        self.email_var = st.text_input("ТВОЙ ЭЛЕКТРОННЫЙ АДРЕС:", value="", 
                                     )
        st.session_state.animated_labels.append({"label": "email", "color": self.neon_colors[2]})

        self.password_var = st.text_input("СЕКРЕТНЫЙ КОД:", value="", type="password", 
                                        )
        st.session_state.animated_labels.append({"label": "password", "color": self.neon_colors[3]})

        self.confirm_password_var = st.text_input("ПОВТОРИ СЕКРЕТНЫЙ КОД:", value="", type="password",
                                                )
        st.session_state.animated_labels.append({"label": "confirm", "color": self.neon_colors[4]})

        col1, col2 = st.columns(2)
        with col1:
            if st.button("ЗАРЕГИСТРИРОВАТЬСЯ"):
                self.register_user()
        with col2:
            if st.button("ОЧИСТИТЬ"):
                self.clear_form()

        st.markdown(f'<p style="font-family: Impact; color: {self.neon_colors[5]};">{self.status_message}</p>', unsafe_allow_html=True)
        st.session_state.animated_labels.append({"label": "status", "color": self.neon_colors[5]})

    def register_user(self):
        username = self.username_var
        email = self.email_var
        password = self.password_var
        confirm_password = self.confirm_password_var

        if not (username and email and password and confirm_password):
            self.flash_message("ЗАПОЛНИ ВСЕ ПОЛЯ!!!")
            return

        if "@" not in email or "." not in email:
            self.flash_message("ЭТО НЕ ПОХОЖЕ НА EMAIL!!!")
            return

        if password != confirm_password:
            self.flash_message("ПАРОЛИ НЕ СОВПАДАЮТ!!!")
            return

        self.flash_message("РЕГИСТРАЦИЯ УСПЕШНА!!!", success=True)
        self.clear_form()

    def flash_message(self, message, success=False):
        colors = self.neon_colors if success else ["#FF0000", "#FFFF00"]
        for _ in range(10):
            for color in colors:
                self.status_message = message
                st.rerun()  # Force update
                time.sleep(0.1)

    def clear_form(self):
        self.username_var = ""
        self.email_var = ""
        self.password_var = ""
        self.confirm_password_var = ""
        self.status_message = ""
        st.rerun()

def main():
    st.set_page_config(page_title="РЕГИСТРАЦИЯ", page_icon=":tada:", layout="wide")
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    form = AcidRegistrationForm()
    if 'bg_shapes' not in st.session_state:
        form.create_psychedelic_background()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        form.create_widgets()

    form.draw_background()  # Draw the background
    
    # Run animations in separate threads (Streamlit's rerun will handle updates)
    threading.Thread(target=form.animate_background, daemon=True).start()
    threading.Thread(target=form.animate_labels, daemon=True).start()

if name == "main":
    main()
