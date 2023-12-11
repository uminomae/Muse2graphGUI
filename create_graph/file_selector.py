from tkinter import filedialog
import os

def open_file_dialog():
    """ファイル選択ダイアログを開き、選択されたファイルのパスを返す"""
    return filedialog.askopenfilename(
        initialdir=os.path.expanduser("~/Downloads"),
        title="Select file",
        filetypes=(("ZIP files", "*.zip"), ("all files", "*.*"))
    )

def abbreviate_filename(filename, max_length=20):
    """ファイル名を省略形にする関数"""
    if len(filename) > max_length:
        return f"{filename[:5]}...{filename[-15:]}"
    return filename

def update_ui_after_selection(file_label, selected_file_path_var, file_path, select_button):
    """ファイル選択後のUIを更新する"""
    if file_path:
        abbreviated_path = abbreviate_filename(os.path.basename(file_path))
        selected_file_path_var.set(file_path)
        file_label.configure(text=abbreviated_path)
        select_button.configure(text="File Selected")
    else:
        selected_file_path_var.set("")
        file_label.configure(text="No file selected")
        select_button.configure(text="Select File")

def file_selection_process(file_label, selected_file_path_var, select_button):
    """ファイル選択プロセスを管理する関数"""
    file_path = open_file_dialog()
    update_ui_after_selection(file_label, selected_file_path_var, file_path, select_button)
