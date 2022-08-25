import logging
import time
from typing import Generator, Optional

import requests

from Other.random_ipv4 import random_ipv4


class Requestor:
    MAX_REQUESTS_PER_MINUTE = 45

    @classmethod
    def main(cls, urls: list) -> Generator:
        for i, url in enumerate(urls):
            start_time = time.time()
            yield cls.make_request(url)
            end_time = time.time()

            duration = end_time - start_time
            logging.info(f'Request: {i + 1} finished in {duration} seconds')

            sleep_time = max(0.0, 60 / cls.MAX_REQUESTS_PER_MINUTE - duration)
            logging.info(f'Time to sleep: {sleep_time}')

            time.sleep(sleep_time)

    @staticmethod
    def make_request(url) -> Optional[dict]:
        try:
            return requests.get(url).json()
        except requests.exceptions.ConnectionError:
            logging.error(f'ConnectionError (url: {url})')
            return None


if __name__ == '__main__':
    URL = 'http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,query'
    tasks = [URL.format(ip=random_ipv4()) for _ in range(100)]
    for row in Requestor.main(tasks):
        print(row)
