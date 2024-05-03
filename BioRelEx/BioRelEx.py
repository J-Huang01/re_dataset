import json

def extract_triplets(data):
    triplets = []
    for interaction in data["interactions"]:
        if interaction["label"] == 1:
            head_idx, tail_idx = interaction["participants"]
            head = None
            tail = None
            for entity in data["entities"]:
                if entity["is_mentioned"]:
                    if data["entities"].index(entity) == head_idx:
                        head = list(entity["names"].keys())[0]
                    elif data["entities"].index(entity) == tail_idx:
                        tail = list(entity["names"].keys())[0]
            if head and tail:
                triplets.append(f"{head}|{interaction['type']}|{tail}")
    return {"triples": triplets, "sentence": data["text"]}

# 读取 JSON 文件
with open("1.0alpha7.dev.json", "r") as file:
    json_data = json.load(file)

# 提取三元组并转换格式
output_data = []
for item in json_data:
    output_data.append(extract_triplets(item))

# 将生成的三元组数据保存到新的 JSON 文件
with open("BioRelEx_test.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)