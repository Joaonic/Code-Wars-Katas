def duplicate_count(text):
    return len([1 for s in list(set(text.lower())) if text.lower().count(s) > 1])
        
        