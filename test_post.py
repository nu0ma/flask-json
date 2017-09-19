import urllib.request, json
import base64

def convert_b64(file_path):
    """
    b64にエンコード
    """
    return base64.encodestring(open(file_path, 'rb').read()).decode("utf-8")

if __name__ == '__main__':
    #送信先
    url = "http://0.0.0.0:5000/post_request"
    #画像ファイル
    image = "test.jpg"
    #画像の名前
    json_key = "image0000"
    
    method = "POST"
    headers = {"Content-Type" : "application/json"}
    #エンコードしたもの
   
    value = convert_b64(image)
    #json_key:名前
    #value:中身
    
    # PythonオブジェクトをJSONに変換する
    obj = {json_key : value}
    #json_data:認識結果などのjsonを入れてもOK
    json_data = json.dumps(obj).encode("utf-8")
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
