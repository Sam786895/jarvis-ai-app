from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        label = Label(text="Hello, I am Jarvis AI", font_size=24)
        btn = Button(text="Click Me", size_hint=(1, 0.3))

        def on_press(instance):
            label.text = "Jarvis is working..."

        btn.bind(on_press=on_press)

        layout.add_widget(label)
        layout.add_widget(btn)

        return layout

if __name__ == "__main__":
    JarvisApp().run()
