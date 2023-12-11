import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
import subprocess

# 日本語フォントの設定
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

def plot_average_lines(resampled_data, ax):
    """各脳波の平均値をプロットする"""
    colors = ['red', 'purple', 'blue', 'green', 'yellow']
    labels = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']
    for i, label in enumerate(labels):
        ax.plot(resampled_data['Elapsed_Minutes'], resampled_data[f'Average_{label}'], 
                label=f'Average {label}', color=colors[i], linewidth=1, alpha=0.5)

def plot_rolling_avg_lines(resampled_data, ax):
    """各脳波の移動平均をプロットする"""
    colors = ['darkred', 'indigo', 'darkblue', 'darkgreen', 'olive']
    labels = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']
    for i, label in enumerate(labels):
        ax.plot(resampled_data['Elapsed_Minutes'], resampled_data[f'Rolling_Avg_{label}'], 
                label=f'Rolling Avg {label}', color=colors[i], linewidth=2)

def configure_graph(ax, resampled_data, graph_title, valid_start_time, end_time):
    """グラフの設定を行う"""
    ax.set_title(graph_title)
    ax.set_xlabel('Time')
    ax.set_ylabel('Average Amplitude')
    ax.set_xticks(range(0, int(max(resampled_data['Elapsed_Minutes'])) + 10, 10))
    ax.set_ylim(-0.6, 1.8)
    ax.legend(loc='lower right')
    ax.text(0.01, 0.01, f"開始日時: {valid_start_time.strftime('%Y-%m-%d %H:%M:%S')}\n終了日時: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n合計時間: {round((end_time - valid_start_time).total_seconds() / 60)}分",
            transform=ax.transAxes, fontsize=9, verticalalignment='bottom')
    ax.grid(True)

def plot_graph(resampled_recent_data, valid_start_time, end_time, graph_title, png_file_name):
    # グラフのフレームと軸を作成する。ここでのグラフの大きさは幅15インチ、高さ8インチと定義する。
    fig, ax = plt.subplots(figsize=(15, 8))
    # 平均脳波のデータラインを軸にプロットするための関数を呼び出す。
    plot_average_lines(resampled_recent_data, ax)
    # 各脳波の移動平均ラインを軸にプロットするための関数を呼び出す。
    plot_rolling_avg_lines(resampled_recent_data, ax)
    # グラフのタイトル、軸のラベル、テキストボックスの配置など、グラフの視覚的な要素を設定する。
    configure_graph(ax, resampled_recent_data, graph_title, valid_start_time, end_time)
    # 作成したグラフをPNGファイルとして保存する。ファイルの保存先は変数png_file_nameで指定する。
    plt.savefig(png_file_name)
    # 保存したPNGファイルが実際に存在するか確認し、存在する場合はMacOSのコマンドを利用してファイルを開く。
    if os.path.exists(png_file_name):
        subprocess.run(['open', png_file_name])  # MacOSでファイルを開くコマンド
    # 保存されたPNGファイルのパスをコンソールに出力する。
    print("PNG file path:", png_file_name)
    # グラフのフィギュアを閉じてリソースを解放する。これはメモリの節約に役立つ。
    plt.close(fig)

