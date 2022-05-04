#!/usr/bin/env python3

import requests
from urllib.parse import urlsplit, parse_qs
import base64
import time
import json
from datetime import datetime

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class QUIZZ:
    def __init__(self):
        self.url = "https://quizapi.io/api/v1/questions?limit=1"
        self.api_key = "5A32flK9g60cHAwgAokuP9W5lavNHIfykOjxkrfL"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'X-Api-Key': self.api_key
        }
    def get_questions(self):
        return requests.get(self.url, headers=self.headers, verify=False).json()

    def print_questions(self):
        data = self.get_questions()
        iteration = 0
        for key in data:
            print(data[iteration]['question'])
            iteration += 1

def main():
    quizz = QUIZZ()
    quizz.get_questions()
    print(quizz.print_questions())
if __name__ == '__main__':
    main()