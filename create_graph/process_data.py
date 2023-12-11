import pandas as pd
import sys
import os
# 親ディレクトリのパスをシステムパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import options

def read_data(csv_file_path):
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"ファイルが見つかりません: {csv_file_path}") from e

def prepare_data(data):
    required_columns = ['TimeStamp']  # 必要な列のリスト
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"必要な列が不足しています: {missing_columns}")
        return None

    try:
        data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])
    except Exception as e:
        print("TimeStamp 列の変換に失敗しました。", e)
        return None

    data.set_index('TimeStamp', inplace=True)
    return data

def calculate_time_range(data_index, time_range_minutes, time_selection_mode):
    """ 時間範囲を計算する関数 """
    if time_range_minutes < 0:
        print("Error: 時間範囲は正の値でなければなりません。")
        return None, None
    if time_range_minutes == 0:
        return data_index.min(), data_index.max()
    if time_selection_mode == "recent":
        end_time = data_index.max()
        start_time = end_time - pd.Timedelta(minutes=time_range_minutes)
    else:
        start_time = data_index.min()
        end_time = start_time + pd.Timedelta(minutes=time_range_minutes)
    return start_time, end_time

def filter_data_by_time_range(data, start_time, end_time):
    """ 指定された時間範囲でデータをフィルタリングする """
    filtered_data = data.loc[start_time:end_time]
    if filtered_data.empty:
        print(f"選択された時間範囲 {start_time} から {end_time} にデータが存在しません。")
        return None, None, None
    
    last_index = filtered_data.last_valid_index()
    first_index = filtered_data.first_valid_index()
    return filtered_data, last_index, first_index

def calculate_averages(filtered_data):
    # 各脳波の平均値を計算する。
    for wave in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
        col_names = [f'{wave}_{loc}' for loc in ['TP9', 'AF7', 'AF8', 'TP10']]
        filtered_data[f'Average_{wave}'] = filtered_data[col_names].mean(axis=1)
    return filtered_data

def resample_and_rolling_average(data, window_size):
    """
    データをリサンプリングし、移動平均を計算する。
        window_size (int): 移動平均のウィンドウサイズ
    """
    resampled_data = data.resample('10S').mean()

    # Elapsed_Minutes の計算
    start_time = resampled_data.index.min()  # リサンプリングされたデータの最初の時刻を使用
    resampled_data['Elapsed_Minutes'] = (resampled_data.index - start_time).total_seconds() / 60

    for wave in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
        resampled_data[f'Rolling_Avg_{wave}'] = resampled_data[f'Average_{wave}'].rolling(window=window_size).mean()
    if resampled_data.empty:
        return None
    return resampled_data

def process_brainwave_data(csv_file_path, time_range, mode):
    try:
        data = read_data(csv_file_path)
    except FileNotFoundError as e:
        print(e)
        return None, None, None
    
    data = prepare_data(data)
    if data is None:
        print("データの準備に失敗しました。")
        return None, None, None

    # 時間範囲の計算
    start_time, end_time = calculate_time_range(data.index, time_range, mode)
    if start_time is None or end_time is None:
        print("時間範囲の計算に失敗しました。")
        return None, None, None
    
    # データのフィルタリング
    filtered_data, actual_end_time, actual_start_time = filter_data_by_time_range(data, start_time, end_time)
    if filtered_data is None or filtered_data.empty:
        print("時間範囲によるフィルタリングに失敗しました。")
        return None, None, None

    # 平均値を求める
    filtered_data = calculate_averages(filtered_data.select_dtypes(include=['float64', 'int64']))

    # 10秒間隔で平均化、移動平均をwindow_sizeのデータポイント数で求める
    window_size = getattr(options, 'DATA_WINDOW_SIZE', 6) # options.DATA_WINDOW_SIZEが不適切な場合にデフォルトで6
    resampled_data = resample_and_rolling_average(filtered_data, window_size)
    if resampled_data is None:
        print("データのリサンプリングと移動平均の計算に失敗しました。")
        return None, None, None

    return resampled_data, actual_end_time, actual_start_time

