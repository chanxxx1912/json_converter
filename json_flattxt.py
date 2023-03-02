import json
result = []
with open("sample2.json", "r") as file:
    data = json.load(file)

def traverse(item, path=""):
    if isinstance(item, dict):
        for key, value in item.items():
            
            traverse(value, f'{path}."{key}"')
    elif isinstance(item, list):
        for value in item:
            traverse(value, path)
    else:
        result.append(f'{path[1:]}."{item}",')



traverse(data)
output = "\n".join(result)

with open("result.txt", "w") as file:
    file.write(output)

