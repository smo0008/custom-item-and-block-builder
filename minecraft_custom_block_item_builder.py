import os
import json

mod_id = input("Enter mod id: ")

usr = input(f"Which file(s) do you want to generate? ({mod_id}/items, {mod_id}/models/block, both) ")

def add_item_json(names):
    for name in names:
        name = name.strip()
        os.makedirs(f"{mod_id}/items", exist_ok=True)
        with open(os.path.join(f"{mod_id}/items", f"{name}.json"), "w") as f:
            f.write('{\n')
            f.write('  "model": {\n')
            f.write('    "type": "minecraft:model",\n')
            f.write(f'    "model": "{mod_id}:block/{name}"\n')
            f.write('  }\n')
            f.write('}\n')
        print(f"{mod_id}/items/{name}.json")

def add_item_model_json(names):
    for name in names:
        name = name.strip()
        os.makedirs(f"{mod_id}/models/block", exist_ok=True)
        with open(os.path.join(f"{mod_id}/models/block", f"{name}.json"), "w") as f:
            f.write('{\n')
            f.write('  "parent": "minecraft:block/cube_all",\n')
            f.write('  "textures": {\n')
            f.write(f'    "all": "{mod_id}:block/{name}"\n')
            f.write('  }\n')
            f.write('}\n')
        print(f"{mod_id}/models/item/{name}.json")

if usr in [f"{mod_id}/items", f"{mod_id}/models/item", "both"]:
    names = input("Enter item names separated by commas: ").split(', ')

if usr == f"{mod_id}/items":
    add_item_json(names)

elif usr == f"{mod_id}/models/item":
    add_item_model_json(names)

elif usr == "both":
    add_item_json(names)
    add_item_model_json(names)
