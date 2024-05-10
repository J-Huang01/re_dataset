import json

def extract_relations(data):
    triples = []
    sentences = []
    
    for passage in data["passages"]:
        sentences.append(passage["text"][0])
    
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
    
    return {"triples": triples, "sentence": " ".join(sentences)}
    
with open("test.json", "r") as file:
    json_data = json.load(file)

output_data = []
for row in json_data["rows"]:
    output_data.append(extract_relations(row["row"]))

with open("bioinfer_test.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)