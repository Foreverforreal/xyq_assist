import json


def decode(data: bytes):
    mes = data
    [action, d] = mes.split(':')
    return (action, d)


def encode(mes):
    return bytes(mes, encoding='utf-8')
