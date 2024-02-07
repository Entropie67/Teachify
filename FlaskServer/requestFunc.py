import requests
from operationFunc import getContent, createCombinedList

## build function for each type of utility 

openai_api_key = "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"  # Replace with your OpenAI API key
url = "https://api.openai.com/v1/chat/completions"

def simpleRequest():
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "capital of France ?"}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(getContent(result))
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
# Generate summary ( input : string, output : array )
def summaryRequest(input):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"I have to learn about {input} Give me 5 keypoints to learn about {input} Only answer in interpretable code: an array. Only an array."}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(result)
        return getContent(result, True)
    else:
        print(f"Error: {response.status_code}, {response.text}")
# Generate lesson ( input : array & globalTheme, output : array )
def lessonpart(globalTheme, inputarray):
    finalResultArray = []
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
    }
    
    for keypoint in inputarray :
        data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"What's the importance of {keypoint} regarding : {globalTheme}. I want you to developp what it is and why it's important. Write that in paragraph format"}],
        "temperature": 0.7
        }
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print(result)
            finalResultArray.append(getContent(result, False))
        else:
            print(f"Error: {response.status_code}, {response.text}")
    return finalResultArray
# Generate exercise ( input : string, output : array)
        
# OHHH I HAVE TO GENERATE A COURSE ABOUT : Paris
