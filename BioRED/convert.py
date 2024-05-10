import json

def extract_relations(data):
    triples = []
    sentence = ""
    
    for passage in data["passages"]:
        sentence += passage["text"] + " "
        
        entities = {}
        for annotation in passage["annotations"]:
            entity_id = annotation["infons"]["identifier"]
            entity_text = annotation["text"]
            entity_type = annotation["infons"]["type"]
            entities[entity_id] = (entity_text, entity_type)
    
    for relation in data["relations"]:
        entity1_id = relation["infons"]["entity1"]
        entity2_id = relation["infons"]["entity2"]
        relation_type = relation["infons"]["type"]
        
        entity1_text, _ = entities.get(entity1_id, ("", ""))
        entity2_text, _ = entities.get(entity2_id, ("", ""))
        
        if entity1_text and entity2_text:
            triple = f"{entity1_text}|{relation_type}|{entity2_text}"
            triples.append(triple)
    
    return {"triples": triples, "sentence": sentence.strip()}

with open("BioRED/Dev.BioC.JSON", "r") as file:
    json_data = json.load(file)

output_data = []
for document in json_data["documents"]:
    output_data.append(extract_relations(document))

with open("biored_valid.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)