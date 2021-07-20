from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Test(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #add widgets

        #image widget
        self.window.add_widget(Image(source="python2.png"))

        #label widget
        self.question = Label(
                        text="Jak nazywa się ten język programowania?",
                        font_size = 18,
                        color='#00FFCE')
        self.window.add_widget(self.question)
        self.answer = TextInput(
                      multiline=False,
                      padding_y = (20,20),
                      size_hint = (1, 0.5)
                      )
        self.window.add_widget(self.answer)
        self.button = Button(
                      text = "SPRAWDŹ",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#3337ff'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

        #callback function

    def callback(self, event):
        
        if self.answer.text == 'Python' or self.answer.text == 'python':
                self.question.text = "Masz rację! Jest to " + self.answer.text + "!"

        else:
                self.question.text = "Spróbuj jeszcze raz! Niestety nie jest to " + self.answer.text + "!"


if __name__ == "__main__":
    Test().run()
