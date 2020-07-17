def unique_in_order(iterable):
    pre_item = None
    result = []
    for item in iterable:
        if item != pre_item:
            result.append(item)
            pre_item = item
    return result