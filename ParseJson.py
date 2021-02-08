import json

odics='{"K1":"vall", "K2":"vall2"}'
json_result = json.loads(odics)
print(json_result["K2"])