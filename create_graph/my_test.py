# test.py

import pandas as pd
import numpy as np
import zipfile
import os
from datetime import datetime, timedelta
from create_graph.plot_graph import plot_graph

# テストデータの生成
def create_test_data(num_points=120):
    # 時間（Elapsed_Minutes）と各種脳波データのシミュレーション
    data = {
        'Elapsed_Minutes': range(num_points),
        'Average_Delta': np.random.rand(num_points),
        'Average_Theta': np.random.rand(num_points),
        'Average_Alpha': np.random.rand(num_points),
        'Average_Beta': np.random.rand(num_points),
        'Average_Gamma': np.random.rand(num_points),
    }
    # 移動平均の追加（窓サイズ6で計算）
    for wave in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
        data[f'Rolling_Avg_{wave}'] = pd.Series(data[f'Average_{wave}']).rolling(window=6).mean()
    return pd.DataFrame(data)

def generate_and_plot_test_graph():
    test_data = create_test_data()

    # CSVファイルとして保存
    csv_file_path = 'test_data.csv'
    test_data.to_csv(csv_file_path, index=False)

    # ZIPファイルに圧縮
    zip_file_path = 'test_data.zip'
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(csv_file_path, os.path.basename(csv_file_path))

    # ZIPファイルを解凍
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        zipf.extractall('.')

    # テストデータの読み込み
    resampled_recent_data = pd.read_csv(csv_file_path)

    # グラフのプロット
    valid_start_time = datetime.now() - timedelta(hours=2)
    end_time = datetime.now()
    graph_title = "Test Graph"
    png_file_name = "test_graph.png"
    plot_graph(resampled_recent_data, valid_start_time, end_time, graph_title, png_file_name)

    # テスト用ファイルの削除
    os.remove(csv_file_path)
    os.remove(zip_file_path)
    # os.remove(png_file_name)
