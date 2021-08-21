import csv
import json
import sys
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def remove_special_chars(word):
    if isinstance(word, str):
        temp = word.replace("\r\n", "")
        result = ""
        for char in temp:
            if char.isalnum() or char in '" ,"`.!?»':
                result += char
        return result
    return str(word)


def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)
        for index, rows in enumerate(csvReader):
            map(remove_special_chars, rows)
            data.append(rows)
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))



if __name__ == "__main__":
    csvFilePath = r'./data/data.csv'
    jsonFilePath = r'./data/data.json'
    make_json(csvFilePath, jsonFilePath)
