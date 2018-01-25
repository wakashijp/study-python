import json
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])

'''
1行目：jsonというPython標準ライブラリから全てのコードをインポートする。
2行目：urllibという標準ライブラリからurlopen関数だけをインポートする。
3行目：url変数にYouTubeのURLを代入する。
4行目：指定されたURLのウェブサーバーに接続し、特定のウェブサービスを要求する。
5行目：応答データを受取り、contents変数に代入する。
6行目：contentsをJSON形式の文字列にデコードし、結果をtext変数に代入する。
7行目：textをdata、即ちPythonのデータ構造に変換する。
8行目：動画についての情報を一度にひとつずつvideo変数に取り出す。
9行目：print関数を使って動画のタイトルだけを表示する。
'''