import urllib.request, json
import base64

def convert_b64(file_path):
    """
    b64にエンコード
    """
    return base64.encodestring(open(file_path, 'rb').read()).decode("utf-8")

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/chat"
    image = "test.jpg"
    method = "POST"
    headers = {"Content-Type" : "application/json"}
    value = convert_b64(image)
    # PythonオブジェクトをJSONに変換する
    #obj = {"image0" : value}
    obj = {
    "sentence1": {
        "sentence": "おはよう。",
        "score": "-1491.054321"
    },
    "sentence2": {
        "sentence": "おはよう！",
        "score": "-1493.834961"
    },
    "sentence3": {
        "sentence": "おはよう",
        "score": "-1501.910034"
    },
    "sentence4": {
        "sentence": "おはよう！",
        "score": "-1504.246948"
    },
    "sentence5": {
        "sentence": "おはよう？",
        "score": "-1506.228516"
    },
    "sentence6": {
        "sentence": "オハイオ。",
        "score": "-1507.084839"
    },
    "sentence7": {
        "sentence": "を配布。",
        "score": "-1509.117432"
    },
    "sentence8": {
        "sentence": "はい。",
        "score": "-1510.448364"
    },
    "sentence9": {
        "sentence": "お早う。",
        "score": "-1510.746216"
    },
    "sentence10": {
        "sentence": "おはよう。",
        "score": "-1512.481201"
    }
    }

    json_data = json.dumps(obj).encode("utf-8")
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
