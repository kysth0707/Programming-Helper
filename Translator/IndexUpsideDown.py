# import json

# JsonValue = None
# with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Output.json", "r", encoding="utf-8") as f:
# 	JsonValue = json.loads("".join(f.readlines()))

# 	Value = 2517
# 	for i in range(2517):
# 		JsonValue['Data'][i]['Index'] = Value
# 		Value -= 1

# with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Output.json", "w", encoding="utf-8") as f:
# 	json.dump(JsonValue, f, ensure_ascii=False, indent=4)