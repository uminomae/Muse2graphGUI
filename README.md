# Muse2graph
## 概要
Muse2とMind Monitorアプリを使って取得したデータからグラフを出力するプログラムです。  

【Muse (headband) - Wikipedia】 https://en.wikipedia.org/wiki/Muse_(headband)  
【Mind Monitor】 https://mind-monitor.com/

### GUI  
<img width="342" alt="スクリーンショット 2023-12-12 6 19 07" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/a3de6cfc-e8e1-485b-a957-c3555febe7ef">  

### class  
<img width="1178" alt="2023-12-10_21 42 04" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/f68d454c-978a-468c-a05d-fb85d96ffdee">  

# 機能：
- macのダウンロードディレクトリにある.zipファイルからグラフを作成します。
- 移動平均線は直近5つのデータポイントとの平均です。
- 出力するデータの範囲は、取得開始時からor取得時の最後（直近）の時間で指定できます。※0orデータの範囲を超える時間数を指定すると全てを出力します
<img width="1612" alt="スクリーンショット 2023-12-11 19 28 17" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/c44eeab3-8fe9-4454-9806-b33fd4b8f2c1">  


# 事前準備  
1. 全てのファイルを適当な場所(例:~/Documents/Muse2)に保存してください。同じディレクトリにある必要があります。
	- ※必要なsaved_plots,extracted_data,configディレクトリは自動で作成されます。
<img width="703" alt="スクリーンショット 2023-12-12 3 57 57" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/34a140dc-542c-48dd-a84b-fea8a39bfa31">  

# 使い方：  
## Muse2,Mind Monitor,Dropbox  
1. Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。  
<img width="200" alt="スクリーンショット 2023-12-06 10 29 47" src="https://github.com/uminomae/Muse2graph/assets/101631407/63cd19f5-c4ba-4cff-8430-10354c2c3462">  
1. 記録を終えたら、Dropboxから計測データ(zip)を標準のダウンロードディレクトリにダウンロードしてください。  
<img width="300" alt="スクリーンショット 2023-12-06 9 10 12" src="https://github.com/uminomae/Muse2graph/assets/101631407/dd0114c0-6a35-40c6-9cfb-84a5210bb1aa">  

## ターミナルでのbashによる操作
1. ターミナル上でcloneした(zipをDLした場合、解凍して作成された)ディレクトリに移動してください  
1. python3 main.pyを実行してください。GUIが起動します。  
	- 前回の設定と同じであれば起動後Returnキーを押すだけでグラフが出力され自動でCSVとPNGが保存されます。  

	- データの保存先 
	※ディレクトリは自動で作成されます  
		- saved_plots/ 
			- グラフ画像 (PNG)
		- extracted_data/ 
			- DropBoxからダウンロードした.zipを解凍したファイル (CSV)

例:  
```bash 
	cd ~/Documents/Muse2graphGUI-main; python3 main.py
```

## GUI操作  
<img width="342" alt="スクリーンショット 2023-12-12 6 19 07" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/a3de6cfc-e8e1-485b-a957-c3555febe7ef">  

- Graph Title
	- グラフ画像の上部に文字を表示します。
		- 自由に入力可能です。
		- メニューから選択することもできます。
			- oprions.pyを編集することで選択肢を増やすことができます。TITLE_OPTIONS  
		- ショートカットキーはcontrol+'m'などで設定しています。
			- ショートカットキーも編集可能です。 KEY_BINDINGS
- Data Span
	- Recent
		- データの終了時点から直近の指定した時間分のデータを元にグラフを出力します。
	- First
		- データの開始時点から指定した時間分のデータを元にグラフを出力します。
- Select File
	- データを自由に選択できます。
	- 未選択の場合、~/Downloadディレクトリから最新の.zipファイルを探してグラフを出力します。
- Create Graph
	- .zipを解凍し、CSVファイルを保存し、グラフを保存し、ウィンドウに画像を出力します。
	- Returnキーでも動作します。  

# スクリプトエディタでアプリとして保存する場合  
https://support.apple.com/ja-jp/guide/script-editor/scpedt1072/2.11/mac/14.0  
```
 tell application "Terminal"
	do script "cd ~/Documents/Muse2; python3 main.py"
end tell
```
<img width="539" alt="スクリーンショット 2023-12-12 6 41 22" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/4ca4d278-f099-42db-bf86-de1fba1432dc">  

Dockにエイリアスを登録することでターミナル操作をせずに起動できます  
<img width="168" alt="スクリーンショット 2023-12-12 6 38 11" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/7b86582c-c975-428c-9d52-56debd491a57">  

# 参考
参考:【Muse2（BMI）で脳波を測ってみた！ | TECH | NRI Digital】 https://www.nri-digital.jp/tech/20211228-7840/  
