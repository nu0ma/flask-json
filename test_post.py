import urllib.request, json
import base64

def convert_b64(file_path):
    """
    b64にエンコード
    """
    return base64.encodestring(open(file_path, 'rb').read()).decode("utf-8")

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/post_request"
    image = "test.jpg"
    method = "POST"
    headers = {"Content-Type" : "application/json"}
    value = convert_b64(image)
    # PythonオブジェクトをJSONに変換する
    obj = {"imagetest" : value}
    json_data = json.dumps(obj).encode("utf-8")
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
