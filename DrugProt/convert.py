import json

def extract_triples(data):
    triples = []
    for relation in data["relations"]:
        arg1_id = relation["arg1_id"]
        arg2_id = relation["arg2_id"]
        arg1_text = None
        arg2_text = None
        for entity in data["entities"]:
            if entity["id"] == arg1_id:
                arg1_text = " ".join(entity["text"])
            elif entity["id"] == arg2_id:
                arg2_text = " ".join(entity["text"])
        if arg1_text and arg2_text:
            triples.append(f"{arg1_text}|{relation['type']}|{arg2_text}")
    
    sentence = " ".join([" ".join(passage["text"]) for passage in data["passages"]])
    return {"triples": triples, "sentence": sentence}

# 读取 data.json 文件
with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# 提取三元组并转换格式
output_data = []
for row in json_data["rows"]:
    output_data.append(extract_triples(row["row"]))

# 将结果保存到 output.json 文件
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)