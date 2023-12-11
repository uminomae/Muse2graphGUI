from tkinter import messagebox
import sys
import tkinter as tk
from create_graph.config_manager import save_config
from create_graph.file_operations import process_zip_file
from create_graph.process_data import process_data
from create_graph.plot_graph import plot_graph
import os
from create_graph.file_operations import get_latest_zip, unzip_file, find_csv, get_png_file_name
# 親ディレクトリのパスをシステムパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import options
import customtkinter as ctk


def select_file_or_dl_latest(selected_file_path_var):
    selected_file_path = selected_file_path_var.get()
    if not selected_file_path:
        print("No file path provided. Trying to select the latest ZIP file.")
        latest_zip = get_latest_zip(os.path.expanduser("~/Downloads"))
        if not latest_zip:
            print("Error: No ZIP file found in the Downloads folder.")
            return None, None

        if not unzip_file(latest_zip, options.EXTRACTED_DATA_DIR):
            print("Error: Failed to unzip the ZIP file.")
            return None, None

        csv_file = find_csv(options.EXTRACTED_DATA_DIR, os.path.splitext(os.path.basename(latest_zip))[0])
        if not csv_file:
            print("Error: CSV file not found after extraction.")
            return None, None
        return latest_zip, csv_file

    zip_file, csv_file, base_name = process_zip_file(selected_file_path)
    if not csv_file:
        print("Error: No CSV file found in the ZIP archive.")
        return None, None
    return zip_file, csv_file

def create_graph(root, process_button, title_entry, data_span_entry, selected_file_path_var, file_label, select_button):
    process_button.configure(text="Processing...", fg_color=options.COLORS["desired_processing_color"])
    root.update_idletasks()

    graph_title = title_entry.get() or options.DEFAULT_GRAPH_TITLE
    data_span = data_span_entry.get() or options.DEFAULT_DATA_SPAN
    selection_type = data_span_entry.get_selection()  # ここで選択オプションを取得

    zip_file, csv_file = select_file_or_dl_latest(selected_file_path_var)
    if not csv_file:
        process_button.configure(text="Create Graph", state=ctk.NORMAL)
        return

    save_config(graph_title, data_span, selection_type)
    png_file_name = get_png_file_name(os.path.basename(csv_file))

    try:
        data_span = int(data_span)
        resampled_recent_data, end_time, valid_start_time = process_data(csv_file, data_span, selection_type)
        if resampled_recent_data is None or end_time is None or valid_start_time is None:
            raise ValueError("Data processing failed, received None.")
    except Exception as e:
        print(f"Error during data processing: {e}")
        messagebox.showerror("Error", f"Failed to process data: {e}")
        process_button.configure(text="Create Graph", state=ctk.NORMAL)
        return

    plot_graph(resampled_recent_data, valid_start_time, end_time, graph_title, png_file_name)
    process_button.configure(text="Create Graph", fg_color=options.COLORS["create_button"], state=ctk.NORMAL)

    if not file_label.cget("text") or file_label.cget("text") == "No file selected":
        select_button.configure(text="Select File")
        file_label.configure(text="")
