from flask import Flask, render_template, request
import requests
import base64

Application = Flask(__name__)

@api_key = 'AIzaSyAVG-nor2RDqJHlKtyBxo-JDsulm_Qk774'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    
    url = f'https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}'
    payload = {
        'input': {
            'text': text
        },
        'voice': {
            'languageCode': 'en-US',
            'ssmlGender': 'NEUTRAL'
        },
        'audioConfig': {
            'audioEncoding': 'MP3'
        }
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        # Handle successful response
        audio_content = response.content
        # Base64 encode the audio content for HTML audio playback
        encoded_audio = base64.b64encode(audio_content).decode('utf-8')
        return f'<audio controls><source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mp3"></audio>'
    else:
        # Handle error response
        return 'Error:', response.status_code, response.text

if __name__ == '__main__':
    app.run(debug=True)



