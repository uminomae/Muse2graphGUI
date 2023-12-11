from tkinter import filedialog
import os

def file_selection_process(root, select_button, file_label, selected_file_path_var):
    def start_progress_bar():
        """プログレスバーを開始するヘルパー関数"""
        select_button.configure(text="Processing...")

    def stop_progress_bar():
        """プログレスバーを停止し、非表示にするヘルパー関数"""

    def abbreviate_filename(filename, max_length=20):
        if len(filename) > max_length:
            return f"{filename[:5]}...{filename[-15:]}"
        return filename

    def update_ui_after_selection(file_path):
        """ファイル選択後のUI更新を行うヘルパー関数"""
        if file_path:
            abbreviated_path = abbreviate_filename(os.path.basename(file_path))
            selected_file_path_var.set(file_path)
            file_label.configure(text=abbreviated_path)
            # file_label.configure(text=os.path.basename(file_path))
            select_button.configure(text="File Selected")
        else:
            selected_file_path_var.set("")
            file_label.configure(text="No file selected")
            select_button.configure(text="Select File")

    def open_file_dialog():
        """ファイル選択ダイアログを開き、選択されたファイルに応じてUIを更新する"""
        file_path = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~/Downloads"),
            title="Select file",
            filetypes=(("ZIP files", "*.zip"), ("all files", "*.*"))
        )
        update_ui_after_selection(file_path)

    # プログレスバーを開始し、ファイル選択ダイアログを開く
    start_progress_bar()
    root.after(100, open_file_dialog)
    root.after_idle(stop_progress_bar)  # ダイアログが閉じられた後にプログレスバーを停止
