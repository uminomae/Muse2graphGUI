window_width = 230 
window_height = 400 

DATA_WINDOW_SIZE = 6

# デフォルトのグラフタイトルとデータスパン
DEFAULT_GRAPH_TITLE = "Muse2"
DEFAULT_DATA_SPAN = "60"

TITLE_OPTIONS = ['meditation', 'meditation deep', 'sleeping', 'coding', 'gaming(TPS)']
# 抽出されたデータのディレクトリ名
EXTRACTED_DATA_DIR = "data/extracted_data"
# 保存するディレクトリのパス
SAVE_DIRECTORY = 'data/saved_plots'

REQUIRED_COLUMNS = [
    'Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10',
    'Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10',
    'Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10',
    'Beta_TP9', 'Beta_AF7', 'Beta_AF8', 'Beta_TP10',
    'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10',
    'RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10',
]

COLORS = {
	"window_background": "#f5f5dc",  # ベージュの背景色
    "background": "#333645",  # ダークな背景色
    "text": "#808080",  # テキストカラー
    "button": "#474C55",
    "button_hover": "#D291BC",  # ボタンホバー時の色（PINK）
    "entry_foreground": "#f5f5dc",  # エントリーのテキスト色（ライトグレー）
    "select_button": "#20B2AA",  # Selectボタンの色（ライトシーグリーン）
    "create_button": "#20B2AA",  # Createボタンの色（ミディアムシーグリーン）
	"label_text": "#808080",  # 
	"PINK":"#FF1493",
	"desired_processing_color":"#333645",
    "option_menu_fg":"#FF69B4",
    "option_menu_button":"#FF69B4",
    "option_menu_button_hover":"#D291BC",
}
