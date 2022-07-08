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
    for current_item in data:
        for current_key in keys:
            value_item = current_item.get(current_key)
            if len(results) == 0:
                results.append(current_item)
            else:
                for current_result in results:
                    value_result = current_result.get(current_key)
                    if value_result != value_item:
                        results.append(current_item)
                    break
    return results


if __name__ == "__main__":
    print(filter_values(origin, keys_1))
    # {'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}, {'foo': 'F', 'bar': 'BAR', 'foobar': 'fb'}]
    print("--------------")
    print(filter_values(origin, keys_2))
    # [{'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}]
    print("--------------")
    print(filter_values(origin, keys_3))
    # [{'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}]
    print("--------------")
