import json

with open("default.json", "r", errors="ignore") as file:
    data = json.loads(file.read())

out = {}

for i, cast in enumerate(data["result"]["casts"]):
    result = cast.get("text", "")
    out[i] = result


print(out)

with open("sample.json", "w") as outfile:
    json.dump(out, outfile, indent=4)
