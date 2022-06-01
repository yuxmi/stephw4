# stephw4

課題内容:
1. Wikipediaのグラフを使ってなにか面白いことをしてみよう
必須："Google"から"渋谷"までをたどる方法をDFSとBFSで探す
追加：ダイクストラ法

準備：
wikipedia_data.zip をダウンロードして解凍し、以下のようなディレクトリ構成にしてください。

step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── .gitignore
├── README.md
├── wikipedia_sample.cc
├── wikipedia_sample.py
└── WikipediaSample.java

グラフデータ
data/ に含まれるファイルで、実際に使うものは以下の2つです。

pages.txt：各ページのidとタイトルのリスト
links.txt：各リンクのリンク元とリンク先のリスト
以下の3つはテスト用の小さなグラフを表すデータです。

pages_small.txt
links_small.txt
graph_small.png

There are three files within the "main" folder: DFS, BFS, Dijkstra's algorithmn, all labelled respectively.
Thank you!

メインの中にDFS、BFS、ダイクストラ法、と入っています。小さいファイルの頂点は全部ちゃんと走りました。
レビューよろしくお願いします＾＾
