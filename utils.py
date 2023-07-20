import requests

BASE_URL = "https://api.henrikdev.xyz/valorant/"


def get_account_by_name(name: str, tag: str) -> dict:
    url = f'{BASE_URL}v1/account/{name}/{tag}'

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        return data

    except Exception as err:
        print(f"Error fetching account: {err}")


def get_current_ranked_info(name: str, tag: str) -> dict:
    def _get_puuid(name: str, tag: str) -> str:
        url = f"{BASE_URL}v1/account/{name}/{tag}"

        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()

        except Exception as err:
            print(f"Error fetching account: {err}")

        puuid = data['data']['puuid']

        return puuid

    puuid = _get_puuid(name, tag)

    url = f"{BASE_URL}v2/by-puuid/mmr/na/{puuid}"

    try:
        r = requests.get(url)
        r.raise_for_status()

        data = r.json()

        return data

    except Exception as err:
        print(f"Error getting match info: {err}")
