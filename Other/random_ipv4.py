from random import randint


def random_ipv4() -> str:
    return '{}.{}.{}.{}'.format(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )
