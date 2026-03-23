import requests
import urllib3

# отключаем предупреждение SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url, verify=False)
        data = response.json()

        print("\n💬 Цитата:")
        print(data["content"])
        print("—", data["author"])

    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    get_quote()