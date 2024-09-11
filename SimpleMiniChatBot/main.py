import google.generativeai as genai
import tkinter as tk

class ChatBotGUI:
    def __init__(self, root, API):
        self.api = API
        self.master = root
        self.master.title('chatbot')
        self.label = tk.Label(root, text='Chat Dialog')
        self.label.pack()
        self.text_dialog = tk.Text(root)
        self.text_dialog.pack()
        self.label = tk.Label(root, text= 'your Message: ')
        self.label.pack()
        self.entry_msg = tk.Entry(root)
        self.entry_msg.pack()
        self.button_send = tk.Button(root, text='Send your Message', command=self.handle_button)
        self.button_send.pack()

    def handle_button(self):
        msg = self.entry_msg.get()
        self.text_dialog.insert('end', 'you: ' + msg + '\n')
        self.text_dialog.insert('end', 'Bot: ' + self.reply(msg) + '\n')
        self.entry_msg.delete(0, tk.END)

    def reply(self, msg):
        genai.configure(api_key=self.api)
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        response = chat.send_message(msg)
        return response.text

GOOGLE_API_KEY=input('API KEY를 입력하세요 : ')
root = tk.Tk()
app = ChatBotGUI(root, GOOGLE_API_KEY)
root.mainloop()

