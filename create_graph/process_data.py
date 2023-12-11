import pandas as pd
import os

def read_data(csv_file_path):
    # CSVファイルを読み込む関数
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {csv_file_path}")
        return None

def filter_recent_data(data, data_span, selection_type):
# def filter_recent_data(data, data_span):
    # 与えられたデータから、最近のデータを特定の時間範囲でフィルタリングする。
    # TimeStamp列を必要とする。
    if 'TimeStamp' in data.columns:
        data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])
        data.set_index('TimeStamp', inplace=True)
    else:
        print("Error: 'TimeStamp' column not found in the data.")
        return None, None, None

    # data_spanが0の場合は全データを返す
    if data_span == 0:
        return data, data.index.max(), data.index.min()
    
    if selection_type == "recent":
        # 最新のデータから過去に遡ってデータを取得
        end_time = data.index.max()
        start_time = end_time - pd.Timedelta(minutes=data_span)
    else:  # "first"の場合
        # データの開始から特定の時間範囲のデータを取得
        start_time = data.index.min()
        end_time = start_time + pd.Timedelta(minutes=data_span)


    recent_data = data.loc[start_time:end_time]

    return recent_data, end_time, start_time

def check_required_columns(recent_data, required_columns):
    # データに必要な列が含まれているかどうかをチェックする。
    missing_columns = [col for col in required_columns if col not in recent_data.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return False
    return True

def calculate_averages(recent_data):
    # 各脳波の平均値を計算する。
    for wave in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
        col_names = [f'{wave}_{loc}' for loc in ['TP9', 'AF7', 'AF8', 'TP10']]
        recent_data[f'Average_{wave}'] = recent_data[col_names].mean(axis=1)
    return recent_data

def resample_and_rolling_average(data, window_size=6):
    """
    データをリサンプリングし、移動平均を計算する。
    Args:
        data (DataFrame): 処理するデータ
        window_size (int): 移動平均のウィンドウサイズ
    Returns:
        Tuple[DataFrame, datetime]: リサンプリングされたデータ、有効な開始時刻
    """
    resampled_data = data.resample('10S').mean()
    valid_start_time = resampled_data.first_valid_index()
    if valid_start_time is None:
        print("No valid start time found.")
        return None, None
    resampled_data['Elapsed_Minutes'] = (resampled_data.index - valid_start_time).total_seconds() / 60
    for wave in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
        resampled_data[f'Rolling_Avg_{wave}'] = resampled_data[f'Average_{wave}'].rolling(window=window_size).mean()
    return resampled_data, valid_start_time

def process_data(csv_file_path, data_span, selection_type):
# def process_data(csv_file_path, data_span):
    # CSVファイルを読み込み、データを処理するメイン関数。
    data = read_data(csv_file_path)
    if data is None:
        return None, None, None
    
    recent_data, end_time, start_time = filter_recent_data(data, data_span, selection_type)
    # recent_data, end_time, start_time = filter_recent_data(data, data_span)

    required_columns = [
    'Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10',
    'Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10',
    'Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10',
    'Beta_TP9', 'Beta_AF7', 'Beta_AF8', 'Beta_TP10',
    'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10',
    'RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10',
    ]
    if not check_required_columns(recent_data, required_columns):
        return None, None, None
    recent_data = calculate_averages(recent_data.select_dtypes(include=['float64', 'int64']))
    resampled_recent_data, valid_start_time = resample_and_rolling_average(recent_data)
    if resampled_recent_data is None:
        return None, None, None
    return resampled_recent_data, end_time, valid_start_time
