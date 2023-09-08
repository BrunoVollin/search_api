def clean_data(data):
    return [item.replace('\n', '').strip() for item in data]
