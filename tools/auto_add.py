import copy
import os
import re
from typing import Dict, List, Optional, TextIO

work_dir = os.path.dirname(os.path.abspath(__file__))
dirs = os.listdir(f"{work_dir}/..")

class Param:
    def __init__(self, line: str) -> None:
        key, value = line.split("=")
        self.name = key.strip()

        self.properties = {}
        property_matches = re.compile(r"<(.+?)>\s*?\((.+?)\)").findall(value)
        if property_matches:
            for property_match in property_matches:
                self.properties[property_match[0]] = property_match[1]

    def __str__(self) -> str:
        property_str = " ".join([f'<{key}>({value})' for key, value in self.properties.items()])
        return f"{self.name} = {property_str}"

    def __repr__(self) -> str:
        return self.__str__()

class PluginMap:
    def __init__(self) -> None:
        self.map_name: Optional[str] = None
        self.map_properties = {}
        # self.params: List[Param] = []
        self.params: Dict[str, Param] = {}

    def add_line(self, line: str) -> None:
        line = line.strip()
        if "<Value>" in line:
            param = Param(line)
            self.params[param.name] = param
        elif "MapStart" in line:
            self.map_name = re.match(r"MapStart\s*<(.*)>", line).group(1)
        elif "MapEnd" in line:
            pass
        else:
            splitter = "=" if "=" in line else ":"
            key, value = line.split(splitter)
            key = key.strip()
            value = value.strip()
            self.map_properties[key] = value

    def __str__(self) -> str:
        property_str = "\n".join(
            [f"{key}: <{value}>" for key, value in self.map_properties.items()]
        )
        param_str = "\n".join([str(param) for param in self.params.values()])
        return f"""
MapStart<{self.map_name}>
{property_str}
{param_str}
MapEnd
        """

    def __repr__(self) -> str:
        return self.__str__()

class PluginConfig:
    def __init__(self) -> None:
        self.maps: List[PluginMap] = []

def load_configs(file: TextIO) -> PluginConfig:
    print(f"loading {file.name}")
    plugin_config = PluginConfig()
    plugin_map = PluginMap()
    in_config_map = False
    for line in file:
        if line.startswith("//") or line.strip() == "":
            continue
        if line.startswith("MapStart"):
            in_config_map = True
        if in_config_map:
            plugin_map.add_line(line)
        if line.startswith("MapEnd"):
            in_config_map = False
            plugin_map.add_line(line)
            print(f'adding map:\n {plugin_map}')
            plugin_config.maps.append(plugin_map)
            plugin_map = PluginMap()
    return plugin_config

def render_one_cab_config(config: PluginConfig) -> None:
    map = config.maps[0]

    map = copy.deepcopy(map)
    map.map_name = "Alt1"
    map.map_properties["PluginDisplayType"] = "Comp"
    map.params["ParamMicType"].properties["Control"] = "COMP_Ratio"
    map.params["ParamOffset"].properties["Control"] = "COMP_Attack"
    map.params["ParamDistance"].properties["Control"] = "COMP_Release"
    map.params["ParamPhaseAlign"].properties["Control"] = "COMP_Threshold"
    config.maps.append(map)

    map = copy.deepcopy(map)
    map.map_name = "Alt2"
    map.map_properties["PluginDisplayType"] = "Gate"
    map.params["ParamMicType"].properties["Control"] = "SHAPE_Gate"
    map.params["ParamOffset"].properties["Control"] = "SHAPE_GateRelease"
    map.params["ParamDistance"].properties["Control"] = "SHAPE_Sustain"
    map.params["ParamPhaseAlign"].properties["Control"] = "SHAPE_HardGate"
    config.maps.append(map)


def render_cabs():
    for path in dirs:
        if ("x12" in path) and ("Marshall" in path):
            print(path)
        else:
            continue

        file = open(f"{work_dir}/../{path}/Contents/Resources/SCMap.txt", "r+")
        config = load_configs(file)

        render_one_cab_config(config)
        print(f"new config:\n{config.maps[-1]}")
        file.write(f"\n\n{str(config.maps[-1])}\n\n{str(config.maps[-2])}\n")
        file.close()


if __name__ == "__main__":
    render_cabs()
