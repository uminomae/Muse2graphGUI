import os
import sys
import zipfile
import glob
from tkinter import messagebox
# 親ディレクトリのパスをシステムパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import options  # 親ディレクトリからインポート

def get_latest_zip(downloads_path):
	# ZIPファイルの一覧を取得し、最新のものを選択
	zip_files = glob.glob(os.path.join(downloads_path, "*.zip"))
	if not zip_files:
		messagebox.showerror("Error", "ZIPファイルが見つかりません。")
		return None
	latest_zip = max(zip_files, key=os.path.getmtime)
	return latest_zip

def unzip_file(zip_file, extract_to):
	# ZIPファイルの解凍
	try:
		with zipfile.ZipFile(zip_file, 'r') as zip_ref:
			zip_ref.extractall(extract_to)
	except zipfile.BadZipFile:
		messagebox.showerror("Error", "ZIPファイルの解凍に失敗しました。")
		return False
	return True

def find_csv(extract_to, base_name):
	# 解凍したCSVファイルを検索
	csv_file = os.path.join(extract_to, f"{base_name}.csv")
	if not os.path.exists(csv_file):
		messagebox.showerror("Error", "CSVファイルが見つかりません。")
		return None
	# 保存されたファイルのパスをコンソールに出力する。
	print("Create CSV file: ", csv_file)
	return csv_file


def process_zip_file(selected_file_path):
    zip_file = selected_file_path or get_latest_zip(os.path.expanduser("~/Downloads"))
    if not zip_file:
        messagebox.showerror("Error", "No ZIP file found.")
        return None, None, None

    base_name = os.path.splitext(os.path.basename(zip_file))[0]
    if not unzip_file(zip_file, options.EXTRACTED_DATA_DIR):
        return None, None, None

    csv_file = find_csv(options.EXTRACTED_DATA_DIR, base_name)
    if not csv_file:
        return None, None, None

    return zip_file, csv_file, base_name

def get_png_file_name(csv_file):
	# 拡張子を除いたファイル名を取得
	base_name = os.path.splitext(csv_file)[0]
	# ディレクトリが存在しない場合は作成
	if not os.path.exists(options.SAVE_DIRECTORY):
		os.makedirs(options.SAVE_DIRECTORY)
	# PNGファイルの名前を生成（拡張子.csvは含まない）
	return f"{options.SAVE_DIRECTORY}/{base_name}.png"