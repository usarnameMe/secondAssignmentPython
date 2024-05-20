def find_minimum(data):
    values = data.values()
    min_value = min(values)
    return min_value


if __name__ == "__main__":
    test_data = {
        "Gvanca": 26,
        "Alexandre": 32,
        "Sandro": 33,
        "Ninia": 11,
    }

    min_val = find_minimum(test_data)
    print(f"The minimum value is: {min_val}")
