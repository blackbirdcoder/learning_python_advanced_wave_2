origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]

keys_1 = ["foo", "bar"]
keys_2 = ["foobar"]
keys_3 = ["bar", "foobar"]


def filter_values(data, keys):
    results = []
    substance = []
    stocked = []
    for current_item in data:
        substance += [value for key, value in current_item.items() if key in keys if value not in substance]
        for current_subject in substance:
            if current_subject in current_item.values() and current_subject not in stocked:
                stocked += substance
                results.append(current_item)
    return results


if __name__ == "__main__":
    print(filter_values(origin, keys_1))
    print(filter_values(origin, keys_2))
    print(filter_values(origin, keys_2))
