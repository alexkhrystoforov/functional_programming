from flask import Flask, render_template,request
import requests
from xml.etree.ElementTree import fromstring, ElementTree


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    if request.method == "GET":
        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = {
            "action": "feedrecentchanges",
            'limit': 5
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.content
        tree = ElementTree(fromstring(DATA))
        changes = []

        tags = ['title', 'link']
        for node in tree.iter('item'):
            for elem in node.iter():
                if elem.tag in tags:
                    changes.append([elem.tag, elem.text])

        return render_template('index.html',  changes=changes)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
