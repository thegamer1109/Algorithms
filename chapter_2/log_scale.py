def log_scale(data, base):
    import math

    result = []
    for i in data:
        result.append(math.log(i, base))

    return result