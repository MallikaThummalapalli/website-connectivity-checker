import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is Online ✅")
        else:
            print(f"{url} returned status code: {response.status_code} ❌")
    except requests.ConnectionError:
        print(f"{url} is Offline ❌")
    except requests.Timeout:
        print(f"{url} timed out ⏱️")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    website = input("Enter website URL (with https://): ")
    check_website(website)
