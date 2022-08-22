import re

IPv4_REGEX = '(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'


def valid_IPv4(address: str) -> bool:
    return re.fullmatch(IPv4_REGEX, address) is not None


if __name__ == '__main__':
    assert valid_IPv4('') is False
    assert valid_IPv4('127.0.0.1') is True
    assert valid_IPv4('0.0.0.0') is True
    assert valid_IPv4('255.255.255.255') is True
    assert valid_IPv4('10.20.30.40') is True
    assert valid_IPv4('10.256.30.40') is False
    assert valid_IPv4('10.20.030.40') is False
    assert valid_IPv4('127.0.1') is False
    assert valid_IPv4('127.0.0.0.1') is False
    assert valid_IPv4('..255.255') is False
    assert valid_IPv4('127.0.0.1\n') is False
    assert valid_IPv4('\n127.0.0.1') is False
    assert valid_IPv4(' 127.0.0.1') is False
    assert valid_IPv4('127.0.0.1 ') is False
    assert valid_IPv4(' 127.0.0.1 ') is False
