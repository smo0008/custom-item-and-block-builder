import os
import json

mod_id = input("Enter mod id: ")

usr = input(f"Which file(s) do you want to generate? ({mod_id}/items, {mod_id}/models/item, minecraft/items) ")

if usr == f"{mod_id}/items":
    names = input("Enter item names separated by commas: ").split(', ')
    for name in names:
        name = name.strip()
        os.makedirs(f"{mod_id}/items", exist_ok=True)
        with open(os.path.join(f"{mod_id}/items", f"{name}.json"), "w") as f:
            f.write('{\n')
            f.write('  "model": {\n')
            f.write('    "type": "minecraft:model",\n')
            f.write(f'    "model": "{mod_id}:item/{name}"\n')
            f.write('  }\n')
            f.write('}\n')
        print(f"{mod_id}/items/{name}.json")

elif usr == f"{mod_id}/models/item":
    names = input("Enter item names separated by commas: ").split(', ')
    for name in names:
        name = name.strip()
        os.makedirs(f"{mod_id}/models/item", exist_ok=True)
        with open(os.path.join(f"{mod_id}/models/item", f"{name}.json"), "w") as f:
            f.write('{\n')
            f.write('  "parent": "minecraft:item/generated",\n')
            f.write('  "textures": {\n')
            f.write(f'    "layer0": "{mod_id}:item/{name}"\n')
            f.write('  }\n')
            f.write('}\n')
        print(f"{mod_id}/models/item/{name}.json")

elif usr == "minecraft/items":
    item = input("Enter minecraft item to replace: ").strip()
    names = input("Enter new item names separated by commas: ").split(',')
    names = [n.strip() for n in names if n.strip()]  # clean names

    os.makedirs("minecraft/items", exist_ok=True)

    data = {
        "model": {
            "type": "minecraft:select",
            "property": "minecraft:custom_model_data",
            "cases": [],
            "fallback": {
                "type": "minecraft:model",
                "model": f"minecraft:item/{item}"
            }
        }
    }
    for name in names:
        case = {
            "when": name,
            "model": {
                "type": "minecraft:condition",
                "property": "minecraft:selected",
                "on_true": {
                    "type": "minecraft:model",
                    "model": f"{mod_id}:item/{name}"
                },
                "on_false": {
                    "type": "minecraft:model",
                    "model": f"minecraft:item/{item}"
                }
            }
        }
        data["model"]["cases"].append(case)

    # write to file
    path = os.path.join("minecraft/items", f"{item}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"minecraft/items/{item}.json")