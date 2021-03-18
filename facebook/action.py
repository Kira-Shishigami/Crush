#!
import requests


def download(items):
    return requests.get(items).content
