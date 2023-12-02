import os, sys
import json



# get current file dir
current_dir = os.path.dirname(os.path.abspath(__file__))
work_dir = f"{current_dir}/../"
print(work_dir)

# find all json files under current dir
json_files = []
for root, dirs, files in os.walk(work_dir):
    if '.ssx' not in root:
        print(f"skip {root}")
        continue
    for file in files:
        if file.endswith(".json"):
            json_files.append(os.path.join(root, file))


map_keyset = set()
key_value_set = {}
type_param_set = {}

# parse json files
for json_file in json_files:
    print(f'parsing "{json_file}" ...')
    conf_maps = json.loads(open(json_file).read())['maps']
    for conf_map in conf_maps:
        name = conf_map.get('mapName', 'unknown')
        conf_type = conf_map.get('mapType', 'unknown')
        print(f"mapName: {name}, mapType: {conf_type}")
        parameters = conf_map.get('parameters', [])
        for param in parameters:
            map_type = param.get('mapsTo', None)
            print(f" -- mapType: {map_type}")
            if map_type is None:
                continue
            if conf_type not in type_param_set:
                type_param_set[conf_type] = set()
            type_param_set[conf_type].add(map_type)

        for key in conf_map.keys():
            map_keyset.add(key)
            value = conf_map[key]
            if isinstance(value, list):
                continue
            if key not in key_value_set:
                key_value_set[key] = set()
            key_value_set[key].add(conf_map[key])


print(map_keyset)

# print key value set
for key in key_value_set.keys():
    print(f"{key}: {key_value_set[key]}")

print('-------------------------------------')
for type in type_param_set.keys():
    print(f"{type}: {json.dumps(list(type_param_set[type]), indent=4)}")
