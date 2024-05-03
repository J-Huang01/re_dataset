import xml.etree.ElementTree as ET
import json

def extract_relations(document):
    triples = []
    sentences = []
    
    for sentence in document.findall("sentence"):
        text = sentence.get("text")
        sentences.append(text)
        
        entities = {}
        for entity in sentence.findall("entity"):
            entities[entity.get("id")] = entity.get("text")
        
        for pair in sentence.findall("pair"):
            if pair.get("interaction") == "True":
                e1 = pair.get("e1")
                e2 = pair.get("e2")
                relation = pair.get("type")
                triple = f"{entities[e1]}|{relation}|{entities[e2]}"
                triples.append(triple)
    
    return {"triples": triples, "sentence": " ".join(sentences)}

# 解析XML文件
tree = ET.parse("miRNA-Test-Corpus.xml")
root = tree.getroot()

# 提取关系信息并转换格式
output_data = []
for document in root.findall("document"):
    output_data.append(extract_relations(document))

# 将结果保存到新的JSON文件
with open("miRNA_test.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)