import json
import sys

lang = sys.argv[1]
# Read the file
with open(f"Templates/{lang}_template.json", "r") as f:
    template = json.load(f)

sent_templates = template["sentiment_templates"]
examples = []
for sent_template in sent_templates:
    for temp in sent_template["templates"]:
        for adj in sent_template["pos_adj"]+sent_template["neg_adj"]:
            for noun in sent_template["noun"]:
                if lang=="ar":
                    new_sentence = temp.replace("[صفة]", adj).replace("[اسم]", noun)
                else:
                    new_sentence = temp.replace("[NOUN]", noun).replace("[ADJ]", adj)
                    if "[a:ADJ]" in new_sentence:
                        if adj[0] in "aeiou":
                            new_sentence = new_sentence.replace("[a:ADJ]", "an "+adj)
                        else:
                            new_sentence = new_sentence.replace("[a:ADJ]", "a "+adj)

                examples.append({"sentence": new_sentence, "sentiment": "positive" if adj in sent_template["pos_adj"] else "negative", "template": temp, "noun": noun, "adj": adj})


# Find the examples with largest difference

with open(f"train/{lang}.json", "w") as f:
    json.dump(examples, f, indent=4, ensure_ascii=False)
