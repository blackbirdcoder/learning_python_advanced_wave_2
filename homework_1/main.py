origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]

keys_1 = ["foo", "bar"]
keys_2 = ["foobar"]
keys_3 = ["bar", "foobar"]


def filter_values(data, keys):
    temp, results = [], []
    for current_item in data:
        for current_key in keys:
            current_value = current_item.get(current_key)
            if current_value not in temp:
                temp.append(current_value)
                results.append(current_item)
            break
    return results


if __name__ == "__main__":
    print(filter_values(origin, keys_1))
    print(filter_values(origin, keys_2))
    print(filter_values(origin, keys_2))
