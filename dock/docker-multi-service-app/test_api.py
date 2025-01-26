import requests

def test_backend():
    url = "http://localhost:3000/api"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    test_backend()
