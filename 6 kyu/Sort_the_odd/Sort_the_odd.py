def sort_array(source_array):
    if len(source_array) == 0:
        return source_array
    odds = iter(sorted(n for n in source_array if n % 2))
    return [next(odds) if n % 2 else n for n in source_array]
    # Return a sorted array.