import os, sys
import json
from enum import Enum

# get current file dir
current_dir = os.path.dirname(os.path.abspath(__file__))

json_files = []

class RowType(Enum):
    PLUGIN = "PLUGIN_START"
    PLUGIN_END = "PLUGIN_END"
    MAP = "MAP_START"
    MAP_END = "MAP_END"
    PARAMETER = "PARAMETER"
    METER = "METER"

# list ./SSX/
dirs = os.listdir(f"{current_dir}/SSX/")

print(dirs)

map_keys = ['pluginId', 'pluginName', 'mapName', 'displayName', 'displayNameShort', 'mapType', 'autoMakeup']

param_keys = ['id', 'name', 'displayName', 'mapsTo', 'value', 'minValue', 'maxValue', 'guiQuantization', 'knobMode']

csv_file = open(f"{current_dir}/ssx.csv", "w")

for dir_name in dirs:
    json_file = f"{current_dir}/SSX/{dir_name}/Contents/Resources/SCMap.json"
    config = json.loads(open(json_file).read())
    config_maps = config['maps']

    csv_file.write(f"{RowType.PLUGIN.value},{dir_name}\n")
    for config_map in config_maps:
        csv_file.write(f"{RowType.MAP.value},")
        for key in map_keys:
            if key in config_map:
                csv_file.write(f"{config_map[key]},")
            else:
                csv_file.write(",")
        csv_file.write("\n")

        parameters = config_map.get('parameters', [])
        for parameter in parameters:
            csv_file.write(f"{RowType.PARAMETER.value},")
            for key in param_keys:
                if key in parameter:
                    csv_file.write(f"{parameter[key]},")
                else:
                    csv_file.write(",")
            csv_file.write("\n")
        meters = config_map.get('meters', [])
        for meter in meters:
            csv_file.write(f"{RowType.METER.value},")
            for key in meter.keys():
                csv_file.write(f"{meter[key]},")
            csv_file.write("\n")
        csv_file.write(f"{RowType.MAP_END.value}{',-------' * 9}\n")
    csv_file.write(f"{RowType.PLUGIN_END.value}{',======='*9}\n")
