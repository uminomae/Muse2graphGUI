# Muse2graph
GUI  
<img width="342" alt="スクリーンショット 2023-12-11 19 27 34" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/c2d1e895-a9ac-4a73-a128-efe1808132bb">  
class  
<img width="1178" alt="2023-12-10_21 42 04" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/f68d454c-978a-468c-a05d-fb85d96ffdee">  

# 機能：
- macのダウンロードディレクトリにある.zipファイルからグラフを作成します。
- 移動平均線は直近5つのデータポイントとの平均です。
- 出力するデータの範囲は、取得開始時からor取得時の最後（直近）の時間で指定できます。※0orデータの範囲を超える時間数を指定すると全てを出力します
<img width="1612" alt="スクリーンショット 2023-12-11 19 28 17" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/c44eeab3-8fe9-4454-9806-b33fd4b8f2c1">  

# 使い方：
## 事前準備
1. 全てのファイルを適当な場所(例:~/Documents/Muse2)に保存してください。同じディレクトリにある必要があります。
	- ※必要なsaved_plots,extracted_data,configディレクトリは自動で作成されます。
<img width="703" alt="スクリーンショット 2023-12-12 3 57 57" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/34a140dc-542c-48dd-a84b-fea8a39bfa31">  

## Muse2,Mind Monitor,Dropbox
1. Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。  
<img width="200" alt="スクリーンショット 2023-12-06 10 29 47" src="https://github.com/uminomae/Muse2graph/assets/101631407/63cd19f5-c4ba-4cff-8430-10354c2c3462">  

1. 記録を終えたら、Dropboxから計測データ(zip)をダウンロードディレクトリにダウンロードしてください。  
<img width="300" alt="スクリーンショット 2023-12-06 9 10 12" src="https://github.com/uminomae/Muse2graph/assets/101631407/dd0114c0-6a35-40c6-9cfb-84a5210bb1aa">  

## ターミナルでのbashによる操作
1. ターミナル上でzipを解凍して作成されたディレクトリに移動してください  
1. python3 main.pyを実行してください。GUIが起動します。  
例:
```bash 
	cd ~/Documents/Muse2graphGUI-main; python3 main.py
```
<img width="342" alt="スクリーンショット 2023-12-11 19 27 34" src="https://github.com/uminomae/Muse2graphGUI/assets/101631407/c2d1e895-a9ac-4a73-a128-efe1808132bb">  

## データの保存先 ※ディレクトリは自動で作成されます
- saved_plots/ 
	- グラフ画像 (PNG)
- extracted_data/ 
	- DropBoxからダウンロードした.zipを解凍したファイル (CSV)

# 参考
参考:【Muse2（BMI）で脳波を測ってみた！ | TECH | NRI Digital】 https://www.nri-digital.jp/tech/20211228-7840/  
参考:【Mind Monitor】 https://mind-monitor.com/Chart.php  