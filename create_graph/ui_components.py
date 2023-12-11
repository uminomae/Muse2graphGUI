import customtkinter as ctk
import options
from PIL import Image
from customtkinter import CTkImage
import sys
import os
# 親ディレクトリのパスをシステムパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import options

class TitleEntry(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=options.COLORS["window_background"], **kwargs)
        self.pack(anchor='center', pady=5)
        self.graph_title_var = ctk.StringVar(value=options.DEFAULT_GRAPH_TITLE)
        self.create_widgets()
    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Graph Title: 入力or選択", text_color=options.COLORS["label_text"])
        self.title_label.pack(anchor='center', pady=2)

        self.title_entry = ctk.CTkEntry(self, fg_color=options.COLORS["entry_foreground"], text_color=options.COLORS["text"], textvariable=self.graph_title_var)
        self.title_entry.pack(anchor='center', pady=2)

        self.title_option_menu = ctk.CTkOptionMenu(self, variable=self.graph_title_var, values=options.TITLE_OPTIONS,fg_color=options.COLORS["option_menu_fg"], button_color=options.COLORS["option_menu_button"], button_hover_color=options.COLORS["option_menu_button_hover"])
        self.title_option_menu.set(self.graph_title_var.get())  # 初期値を設定
        self.title_option_menu.pack(anchor='center',  pady=5)
    def get(self):
        return self.title_entry.get()
    def get_title_var(self):
        return self.graph_title_var

class DataSpanEntry(ctk.CTkFrame):
    def __init__(self, parent, data_span_var, selection_var, **kwargs):
        super().__init__(parent, fg_color=options.COLORS["window_background"], **kwargs)
        self.pack(pady=5)
        self.data_span_var = data_span_var
        self.selection_var = selection_var
        self.create_widgets()
    def create_widgets(self):
        # ラベル
        self.data_span_label = ctk.CTkLabel(self, text="Data Span: 単位:分\n0=全てのデータポイントを取得", text_color=options.COLORS["label_text"])
        self.data_span_label.pack(anchor='center', pady=2)
        # ラジオボタン
        self.radio_recent = ctk.CTkRadioButton(self, text="Recent(最後の)", value="recent", text_color=options.COLORS["label_text"], variable=self.selection_var)
        self.radio_recent.pack(side='top', fill='x', pady=2, padx=(10, 10), anchor='w')
        self.radio_first = ctk.CTkRadioButton(self, text="First(最初の)", value="first", text_color=options.COLORS["label_text"], variable=self.selection_var)
        self.radio_first.pack(side='top', fill='x', pady=(2,5), padx=(10, 10), anchor='w')
        # データスパンの入力フィールド
        self.data_span_entry = ctk.CTkEntry(self, fg_color=options.COLORS["entry_foreground"], text_color=options.COLORS["text"], textvariable=self.data_span_var)
        self.data_span_entry.pack(anchor='center', pady=0)
    def get(self):
        return self.data_span_entry.get()
    def get_data_span_var(self):
        return self.data_span_var
    def get_selection(self):
        return self.selection_var.get()
    def set_selection(self, selection_type):
        if selection_type == "recent":
            self.radio_recent.select()
        elif selection_type == "first":
            self.radio_first.select()
    
class SelectButtonUI(ctk.CTkFrame):
    def __init__(self, parent, file_path_var, on_file_select_command, **kwargs):
        super().__init__(parent, fg_color=options.COLORS["window_background"], **kwargs)
        self.pack(pady=(20,0))
        self.file_path_var = file_path_var
        self.on_file_select_command = on_file_select_command
        self.create_widgets()
    def create_widgets(self):
        select_button_image = Image.open("img/file.png")
        select_button_image = CTkImage(select_button_image)
        self.select_button = ctk.CTkButton(self, image=select_button_image, text="Select File", fg_color=options.COLORS["select_button"], hover_color=options.COLORS["button_hover"])
        self.select_button.pack(anchor='center', pady=0)
        self.select_button.configure(command=self.on_file_select_command)

class ProcessButtonUI(ctk.CTkFrame):
    def __init__(self, parent, on_create_graph_command, **kwargs):
        super().__init__(parent, fg_color=options.COLORS["window_background"], **kwargs)
        self.on_create_graph_command = on_create_graph_command
        self.pack(pady=5)
        self.create_widgets()
    def create_widgets(self):
        process_button_image = Image.open("img/graph.png")
        process_button_image = CTkImage(process_button_image)
        self.process_button = ctk.CTkButton(self, image=process_button_image, text="Create Graph", fg_color=options.COLORS["create_button"], hover_color=options.COLORS["button_hover"])
        self.process_button.pack(anchor='center', pady=10)
        self.process_button.configure(command=self.on_create_graph_command)