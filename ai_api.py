import requests

def get_answer(text_input):
    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
    payload = {
        "enable_google_results": True,
        "enable_memory": False,
        "input_text": text_input
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
       # "X-API-KEY":
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return response.text