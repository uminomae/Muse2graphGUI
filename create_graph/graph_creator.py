from tkinter import messagebox
from create_graph.config_manager import save_config
from create_graph.file_operations import process_zip_file, get_latest_zip, unzip_file, find_csv, get_png_file_name
from create_graph.process_data import process_brainwave_data
from create_graph.plot_graph import plot_graph
import sys
import os
import options
import customtkinter as ctk
# 親ディレクトリのパスをシステムパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ファイル選択処理
def handle_file_selection(selected_file_path_var):
    selected_file_path = selected_file_path_var.get()
    if not selected_file_path:
        _, csv_file, _ = process_zip_file(None)
        return csv_file 
        # return process_zip_file(None)
    else:
        # 選択されたファイルの処理
        _, csv_file, _ = process_zip_file(selected_file_path)
        if not csv_file:
            messagebox.showerror("Error", "No CSV file found in the ZIP archive.")
        return csv_file

def update_ui_after_processing(process_button, select_button, file_label, status_text="Create Graph"):
    process_button.configure(text=status_text, state=ctk.NORMAL)
    if not file_label.cget("text") or file_label.cget("text") == "No file selected":
        select_button.configure(text="Select File")
        file_label.configure(text="")

def get_graph_settings(title_entry, data_span_entry):
    """グラフ設定を取得する"""
    return (title_entry.get() or options.DEFAULT_GRAPH_TITLE,
            data_span_entry.get() or options.DEFAULT_DATA_SPAN,
            data_span_entry.get_selection())

def display_error_and_reset_ui(process_button, select_button, file_label, error_message):
    """エラーを表示し、UIをリセットする"""
    messagebox.showerror("Error", error_message)
    update_ui_after_processing(process_button, select_button, file_label)

def process_data_and_create_graph(csv_file, graph_title, data_span, selection_type, process_button, select_button, file_label):
    """データ処理とグラフ作成を行う"""
    try:
        resampled_data, actual_end_time, actual_start_time = process_brainwave_data(csv_file, int(data_span), selection_type)
        if resampled_data is None or actual_end_time is None or actual_start_time is None:
            raise ValueError("Data processing failed.")
    except Exception as e:
        display_error_and_reset_ui(process_button, select_button, file_label, f"Failed to process data: {e}")
        return False
    # グラフのプロット
    plot_graph(resampled_data, actual_start_time, actual_end_time, graph_title, get_png_file_name(os.path.basename(csv_file)))
    return True

# メインのグラフ作成機能
def create_graph(root, process_button, title_entry, data_span_entry, selected_file_path_var, file_label, select_button):
    try:
        # UIの更新: プロセス開始を示す
        process_button.configure(text="Processing...", fg_color=options.COLORS["desired_processing_color"])
        root.update_idletasks()
        # グラフの設定を取得
        graph_title, data_span, selection_type = get_graph_settings(title_entry, data_span_entry)
        # ファイル選択処理
        csv_file = handle_file_selection(selected_file_path_var)
        if not csv_file:
            display_error_and_reset_ui(process_button, select_button, file_label, "File selection failed.")
            return
        # 設定の保存
        save_config(graph_title, data_span, selection_type)
        # データ処理とグラフの作成
        if not process_data_and_create_graph(csv_file, graph_title, data_span, selection_type, process_button, select_button, file_label):
            return
    except Exception as e:
        display_error_and_reset_ui(process_button, select_button, file_label, str(e))
    update_ui_after_processing(process_button, select_button, file_label, "Create Graph")
