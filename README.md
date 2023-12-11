# Muse2graph

# 機能：
- macのダウンロードディレクトリにある.zipファイルからグラフを作成します。
- 移動平均線は直近5つのデータポイントとの平均です。
<img width="900" alt="mindMonitor_2023-12-03--22-22-3" src="https://github.com/uminomae/Muse2graph/assets/101631407/ed6034ab-c33a-484f-b6a1-78859f2832ad">

# 使い方：
## 事前準備
1. ファイル群を適当な場所に保存してください。同じディレクトリにある必要があります。
	- main.pyなど
	- ※saved_plots,extracted_dataディレクトリは自動で作成されます。

## Muse2,Mind Monitor,Dropbox
1. Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。
<img width="200" alt="スクリーンショット 2023-12-06 10 29 47" src="https://github.com/uminomae/Muse2graph/assets/101631407/63cd19f5-c4ba-4cff-8430-10354c2c3462">

1. 記録を終えたら、Dropboxから計測データ(zip)をダウンロードディレクトリにダウンロードしてください。  
<img width="300" alt="スクリーンショット 2023-12-06 9 10 12" src="https://github.com/uminomae/Muse2graph/assets/101631407/dd0114c0-6a35-40c6-9cfb-84a5210bb1aa">  

## ターミナルでのbashによる操作
1. ターミナル上で、muse2analysis.shを保存したディレクトリに移動してください  
例
```bash 
	cd /Users/username/Documents/Muse2
```
1. muse2analysis.shを実行してください。グラフが作成されます。  
例　
```bash
	python3 main.py
```


参考:【Muse2（BMI）で脳波を測ってみた！ | TECH | NRI Digital】 https://www.nri-digital.jp/tech/20211228-7840/  
参考:【Mind Monitor】 https://mind-monitor.com/Chart.php