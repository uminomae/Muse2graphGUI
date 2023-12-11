#!/usr/bin/env python3

from create_graph.config_manager import load_config
from create_graph.file_selector import file_selection_process
from create_graph.graph_creator import create_graph
from create_graph.my_test import generate_and_plot_test_graph
from create_graph.ui_components import TitleEntry, DataSpanEntry, SelectButtonUI, ProcessButtonUI
import options
import sys
import customtkinter as ctk
import options

class MuseDataAnalysisApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # 親クラスのコンストラクタを呼び出す。
        self.initialize_window()
        self.load_application_settings()
        self.create_widgets()
        self.bind_key_events()

    def initialize_window(self):
        self.title("Analysis of Muse2 data")
        self.geometry(f"{options.window_width}x{options.window_height}")
        self.configure(fg_color=options.COLORS["window_background"])

    def load_application_settings(self):
        self.config = load_config()
        self.selected_file_path_var = ctk.StringVar(self, "")
        self.data_span_var = ctk.StringVar(value=options.DEFAULT_DATA_SPAN)
        self.data_selection_option_var = ctk.StringVar(value="recent")

    def create_widgets(self):
        self.create_title_entry()
        self.create_data_span_entry()
        self.create_file_selection_ui()
        self.create_process_button_ui()
    def create_title_entry(self):
        self.title_entry = TitleEntry(self)
        saved_title = self.config.get('graph_title', options.DEFAULT_GRAPH_TITLE)
        self.title_entry.get_title_var().set(saved_title)
    def create_data_span_entry(self):
        self.data_span_entry = DataSpanEntry(self, self.data_span_var, self.data_selection_option_var)
        saved_data_span = self.config.get('data_span', options.DEFAULT_DATA_SPAN)
        self.data_span_entry.get_data_span_var().set(saved_data_span)
        self.data_span_entry.set_selection(self.config.get('selection_type', 'recent'))
    def create_file_selection_ui(self):
        self.select_button_ui = SelectButtonUI(self, self.selected_file_path_var, self.on_file_select)
        self.file_label = ctk.CTkLabel(self, text="未選択の場合:ダウンロード/内の\n最新の.zipを自動選択", text_color=options.COLORS["label_text"], fg_color='transparent')
        self.file_label.pack(anchor='center', pady=(0,0))
    def create_process_button_ui(self):
        self.process_button_ui = ProcessButtonUI(self, self.on_create_graph)

    def on_key_pressed(self, event=None, option_value=''):
        """ キーが押されたときにオプションメニューの値を設定する """
        self.title_entry.title_option_menu.set(option_value)
    def bind_key_events(self):
        # """ キーイベントをバインドする """
        self.bind("<Return>", self.on_create_graph)
        self.bind('<Control-c>', lambda event: self.on_key_pressed(event, 'coding'))
        self.bind('<Control-m>', lambda event: self.on_key_pressed(event, 'meditation'))
        self.bind('<Control-d>', lambda event: self.on_key_pressed(event, 'meditation deep'))
        self.bind('<Control-s>', lambda event: self.on_key_pressed(event, 'sleeping'))
        self.bind('<Control-g>', lambda event: self.on_key_pressed(event, 'gaming(TPS)'))

    def on_close(self):
        """ アプリケーション終了時のクリーンアップ処理を行うメソッド。 """
        print("Cleaning up...")
        self.quit()  # Tkinterのイベントループを終了。
        self.destroy()  # ウィンドウを破壊。
    def on_file_select(self):
        """ ファイル選択ボタンが押された時のイベントハンドラ。 """
        file_selection_process(
            self, self.select_button_ui.select_button, self.file_label, self.selected_file_path_var)
    def on_create_graph(self, event=None):
        """ グラフ作成ボタンが押された時のイベントハンドラ。 """
        create_graph(
            self, self.process_button_ui.process_button, self.title_entry, self.data_span_entry, self.selected_file_path_var, self.file_label, self.select_button_ui.select_button)


def main():
    app = MuseDataAnalysisApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()

if __name__ == '__main__':
    # コマンドライン引数によってテストモードを切り替える
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        generate_and_plot_test_graph()
    else:
        main()

