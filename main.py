import json
import os
import time
import requests


def textToSpeech(text='hello man'):
    headers = {"Authorization": f"Bearer "}
    url = "https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        'providers': 'openai',
        'language': 'ru',
        'option': 'MALE',
        'openai': 'ru_alloy',
        'text': f'{text}'
    }

    resource = requests.post(url, headers=headers, json=payload)
    result = json.loads(resource.text)
    unx_time = int(time.time())


    # with open(f'{unx_time}.json', 'w') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)



def main():
    textToSpeech(text='Со столешницами для кухни и ванной из HPL-Композита вы навсегда можете забыть о проблеме формальдегида, т.к. они абсолютно экологичны и безопасны для людей и окружающей среды.')

if __name__ == '__main__':
    main()