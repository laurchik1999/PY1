import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ",", new_line = '\n') -> list[dict]:
    data = []
    with open(filename) as f:
        headers = next(f).strip(new_line).split(delimiter)
        for line in f:
            lines = {header: li for header, li in zip(headers, line.strip(new_line).split(delimiter))}
            data.append(lines)


    return data

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


