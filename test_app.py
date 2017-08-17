# app.py
from flask import Flask,request,jsonify
import base64

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

    ##jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    data = request.json
    #keysを取得
    keys_array = list(data.keys())
    #valuesを取得
    values_array = list(data.values())
    """
    送ってくるjsonは一つ目の要素が{画像名:base64エンコード}としたもの
    """

    #画像の保存名
    save_name = keys_array[0] + ".jpg"
    #コンバート
    convert_b64_to_file(bytes(values_array[0],"utf-8"),save_name)
    #ここにkey毎の処理を書いていく
    ###このやり方だと，image.jpgがいくつも生成されることになってしまう
    # for i in range(len(keys_array)):
    #     #まずはkeyが画像の場合
    #     if keys_array[i] == "image":
    #         save_name = keys_array[i] + ".jpg"
    #         convert_b64_to_file(bytes(values_array[i],"utf-8"),save_name)

    #utf-8に変換したいけどdict型なのでできない
    #value = bytes(value,"utf-8")
    #ファイル名はとりあえずkeyとしておく
    #filename = key + ".jpg"
    #デコード
    #convert_b64_to_file(value,filename)
    #convert_b64_to_file(value,"./test.jpg")

    return jsonify(res='success', **data)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
    # curl http://127.0.0.1:5000/post_request -X POST -H "Content-Type: application/json" -}''{"key": "value"}
