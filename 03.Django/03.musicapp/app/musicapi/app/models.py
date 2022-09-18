import requests
from requests.exceptions import ConnectionError, HTTPError
from typing import Final, Union, Optional
from django.core.cache import cache


SAMPLE_API_ROOT: Final[str] = "http://sample:9000/v1/"


class Category:
    def __init__(self) -> None:
        self.url: str = SAMPLE_API_ROOT + "categories?"
        self.get_categories()

    def get_categories(self) -> None:
        cache_key: str = 'categories'
        categories: dict[str, list[str]] = cache.get(cache_key, None) 
        if categories is None:
            categories = self.cache_categories(cache_key)

        self.genre: list[str] = categories['genre']
        self.role: list[str] = categories['role']
        self.instrument: list[str] = categories['instrument']
        self.key: list[str] = categories['key']
        self.time_signature: list[str] = categories['time_signature']

    def cache_categories(self, cache_key: str) -> dict[str, list[str]]:
        types: list[str] = ['genre', 'role', 'instrument', 'key', 'time_signature']
        categories: dict[str, list[str]] = {
            'genre': [],
            'role': [],
            'instrument': [],
            'key': [],
            'time_signature': []
        }
        for type in types:
            try:
                response: requests.Response = requests.get(url=self.url, params={'type': type})
            except ConnectionError:
                raise ConnectionError('Could not connect to sample api server')
            if response.status_code != 200:
                raise HTTPError('Request failed due to {} error from sample api server'.format(response.status_code))

            items: list[dict[str, str]] = response.json()['items']
            for item in items:
                categories[type].append(item['name'])
        cache.set(cache_key, categories, 60*60)
        return categories


class Samples:
    def __init__(self, params: dict[str, Union[list[str], int]], instruments: list[str]) -> None:
        self.url: str = SAMPLE_API_ROOT + "samples?"
        self.total: int = 0
        self.items: list[dict[str, object]] = []
        self.get_samples(params, instruments)

    def get_samples(self, params: dict[str, Union[list[str], int]], instruments: list[str]) -> None:
        try:
            response: requests.Response = requests.get(url=self.url, params=params)
        except ConnectionError:
            raise ConnectionError('Could not connect to sample api server')
        if response.status_code in (422, 500):
            raise HTTPError('Request failed due to {} error from sample api server'.format(response.status_code))
        elif response.status_code == 404:
            return
        
        raw_items = response.json()['items']    
        while response.json()['has_next'] == True:
            params['page'] += 1
            response = requests.get(url=self.url, params=params)
            raw_items += response.json()['items']

        self.items = [item for item in raw_items if item['instrument'] in instruments]
        self.total = len(self.items)

