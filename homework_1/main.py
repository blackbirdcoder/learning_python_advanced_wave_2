origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]

keys_1 = ["foo", "bar"]
keys_2 = ["foobar"]
keys_3 = ["bar", "foobar"]

fixture = [
    {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
    {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
    {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
    {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
    {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
]


def filter_values(data, keys):
    results = []
    substance = []
    stocked = []
    for current_item in data:
        substance.append([value for key, value in current_item.items() if key in keys])
        for current_subject in substance:
            if (value in current_subject for value in current_item.values()) and current_subject not in stocked:
                stocked.append(current_subject)
                results.append(current_item)
    return results


if __name__ == "__main__":
    def test_filter_name():
        test_value = [
            {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
            {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        ]
        assert filter_values(fixture, ["name"]) == test_value


    def test_filter_company():
        test_value = [
            {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
            {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
            {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
            {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
            {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
        ]
        assert filter_values(fixture, ["name", "company"]) == test_value


    def test_filter_name_job():
        test_value = [
            {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
            {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
            {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
            {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
        ]
        assert filter_values(fixture, ["name", "job"]) == test_value


    if __name__ == "__main__":
        test_filter_name()
        test_filter_company()
        test_filter_name_job()
