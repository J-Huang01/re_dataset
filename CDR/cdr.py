import json

def extract_relations(data):
    triples = []
    sentence = ""
    
    for passage in data["passages"]:
        sentence += passage["text"][0] + " "
    
    for relation in data["relations"]:
        arg1_id = relation["arg1_id"]
        arg2_id = relation["arg2_id"]
        arg1_text = ""
        arg2_text = ""
        
        for entity in data["entities"]:
            if entity["id"] == arg1_id:
                arg1_text = entity["text"][0]
            elif entity["id"] == arg2_id:
                arg2_text = entity["text"][0]
        
        if arg1_text and arg2_text:
            triples.append(f"{arg1_text}|{relation['type']}|{arg2_text}")
    
    return {"triples": triples, "sentence": sentence.strip()}

# 读取JSONL数据
with open("validation.jsonl", "r") as file:
    json_lines = file.readlines()

# 提取关系信息并转换格式
output_data = []
for line in json_lines:
    document = json.loads(line)
    output_data.append(extract_relations(document))

# 将结果保存到新的JSONL文件
with open("CDR_validation.jsonl", "w", encoding="utf-8") as file:
    for item in output_data:
        file.write(json.dumps(item, ensure_ascii=False) + "\n")