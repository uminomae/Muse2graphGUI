#!/usr/bin/env python3
# この.pyは、下記のようなbashで実行されたスクリプトによって前処理された引数が渡されることを前提としています
# 例　sh ./muse2analysis.sh 1 aaa 45

import pandas as pd
import sys
from process_data import process_data
from plot_graph import plot_graph
import os
from file_operations import get_png_file_name

def main():
    if len(sys.argv) < 4:
        print("Usage: python script.py <csv_file_path> <graph_title> <data_span>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    graph_title = sys.argv[2]
    data_span = int(sys.argv[3])

    try:
        data = pd.read_csv(csv_file_path)
        resampled_recent_data, end_time, valid_start_time = process_data(csv_file_path, data_span)
    except Exception as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

    if resampled_recent_data is None:
        print("No data to plot.")
        sys.exit(1)
	# PNGファイル名を取得
    png_file_name = get_png_file_name(os.path.basename(csv_file_path))

    plot_graph(resampled_recent_data, valid_start_time, end_time, graph_title, png_file_name)

if __name__ == '__main__':
    main()
