
from flask import Flask, request, render_template, jsonify
import requests, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("VT_API_KEY")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# URL Scan route
@app.route('/scan/url', methods=['POST'])
def scan_url():
    url = request.form['url']
    vt_response = requests.post(
        'https://www.virustotal.com/api/v3/urls',
        headers={'x-apikey': API_KEY},
        data={'url': url}
    )
    analysis_id = vt_response.json()['data']['id']
    analysis = requests.get(
        f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',
        headers={'x-apikey': API_KEY}
    )
    result = analysis.json()
    stats = result['data']['attributes']['stats']
    return render_template('result.html', stats=stats, link=url)

# File Scan route
@app.route('/scan/file', methods=['POST'])
def scan_file():
    file = request.files['file']
    vt_response = requests.post(
        'https://www.virustotal.com/api/v3/files',
        headers={'x-apikey': API_KEY},
        files={'file': (file.filename, file.stream)}
    )
    analysis_id = vt_response.json()['data']['id']
    analysis = requests.get(
        f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',
        headers={'x-apikey': API_KEY}
    )
    result = analysis.json()
    stats = result['data']['attributes']['stats']
    return render_template('result.html', stats=stats, link="Uploaded File")
