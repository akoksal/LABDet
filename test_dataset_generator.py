import json
import sys

lang = sys.argv[1]
# Read the file
with open(f"Templates/{lang}_template.json", "r") as f:
    template = json.load(f)

sent_template = template["artificial_experiments"]
examples = []
for temp in sent_template["templates"]:
    for adj in sent_template["neutral_adj"]:
        for nat_short, nat_full in template["alternatives"].items():
            if lang=="ar":
                new_sentence = temp.replace("[صفة]", adj).replace("[عرق]", nat_full)
            else:
                new_sentence = temp.replace("[NATIONALITY]", nat_full).replace("[ADJ]", adj)
                if "[a:ADJ]" in new_sentence:
                    if adj[0] in "aeiou":
                        new_sentence = new_sentence.replace("[a:ADJ]", "an "+adj)
                    else:
                        new_sentence = new_sentence.replace("[a:ADJ]", "a "+adj)

            examples.append({"sentence": new_sentence, "template":temp, "nationality":nat_short, "adj": adj})

with open(f"test/{lang}.json", "w") as f:
    json.dump(examples, f, indent=4, ensure_ascii=False)
