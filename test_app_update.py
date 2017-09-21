
from flask import Flask,request,jsonify
import base64
import re

"""
それぞれのディレクトリの用途
/image : base64エンコードされた画像をデコードしてローカルに保存する．
/chat : 発話と尤度がペアになったjsonを取得する．
"""
count = 0

#server
app = Flask(__name__)

def convert_b64_to_file(b64,outfile_path):
    """
    b64をデコードしてファイルに書き込む
    """
    s = base64.decodestring(b64)
    with open(outfile_path,"wb") as f :
        f.write(s)

@app.route("/")
def index():
    return "send me json "

#base64でエンコードされたjsonファイルをデコード
@app.route('/post_request', methods=['POST'])
def post_request():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している
    #jsonを取得
    data = request.json
    #keysを取得
    keys_array = list(data.keys())
    #valuesを取得
    values_array = list(data.values())
    """
    送ってくるjsonはの形式{画像名:base64エンコード}としたもの
    """
    #if imagetest + count in keys_array
    m = re.match(r"imagetest+",keys_array[-1])
    # print(m)
    if m  :
        #画像の保存名
        save_name = keys_array[-1] + ".jpg"
        #コンバート
        convert_b64_to_file(bytes(values_array[-1],"utf-8"),save_name)

        #print(keys_array)
        return jsonify(res='success', **data)

    else:
        print(keys_array[-1],values_array[-1])
        return jsonify(res='success', **data)


##発話の認識結果のjsonを保存する
@app.route('/chat', methods=['POST'])
def post_request_chat():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    data = request.json
    #keysを取得
    keys_array = list(data.keys())
    #valuesを取得
    values_array = list(data.values())
    """
    送ってくるjsonはN_bestで作ったやつ
    """
    #発話収納辞書（キーに発話，値に尤度）
    sentence_dict = {}
    #とりあえず会話文とスコアをprintしてみる
    #values_array
    for i in range(len(keys_array)):
        #print(values_array[i]["sentence"],values_array[i]["score"])
        #発話と尤度を辞書型で格納
        sentence_dict[values_array[i]["sentence"]] = values_array[i]["score"]
    print(sentence_dict)
    #このsentence_dictを山本さんのプログラムにぶち込みたいけど，
    #pointingとかの情報もここに送ってくる必要がある．

    return jsonify(res='success', **data)

if __name__ == "__main__":
    app.debug = True
    app.run("163.225.223.72")
    # curl http://0.0.0.0/post_request -X POST -H "Content-Type: application/json" -}''{"key": "value"}
