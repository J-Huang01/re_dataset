import json

def transform_data(data):
    output_data = []

    for item in data:
        sentence = item["sentence"]
        head = item["head"]["word"]
        head_id = item["head"]["id"]
        tail = item["tail"]["word"]
        tail_id = item["tail"]["id"]
        relation = item["relation"]

        triple = f"{head}|{relation}|{tail}"

        output_item = {
            "triples": [triple],
            "sentence": sentence
        }
        output_data.append(output_item)

    return output_data

# 读取JSON数据
with open("valid.json", "r") as file:
    json_data = json.load(file)

# 转换数据格式
output_data = transform_data(json_data)

# 将结果保存到新的JSON文件
with open("ddi_validation.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)