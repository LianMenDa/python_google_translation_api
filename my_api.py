import json
import kingdada

from flask import Flask, abort, request

app = Flask(__name__)


@app.route('/api/<string:text>', methods=['GET'])
def trans(text):
    txt = {
        'request': text,
        'response': kingdada.auto_translator(text)
    }
    return json.dumps(txt, ensure_ascii=False, indent=4)


@app.route('/api', methods=['POST'])
def post_trans():
    input_data = request.json.get('request')
    try:
        data = trans(input_data)
        return data
    except IndexError as e:
        abort(400)
        return e


if __name__ == '__main__':
    app.run()
