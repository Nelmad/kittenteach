def parse_default(value, default, cls=int):
    try:
        return cls(value)
    except (ValueError, TypeError):
        return default


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance
