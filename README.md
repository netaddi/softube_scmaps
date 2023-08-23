# softube_scmaps

repository to store my plugin scmap configs for softube console 1

## some remarks

### 1. single plugin multiple instances

Within one SCMap file works in a way like `MapStart<Default>` `MapStart<Alt1>` etc.
Note that each plugin needs to contain a `PluginDisplayName` field, or console 1 will start with error.

## templates

``` text
MapStart<Alt1>
PluginDisplayName:""
PluginDisplayType: <Comp>

MapEnd

MapStart<Alt2>
PluginDisplayName:""
PluginDisplayType: <EQ>

MapEnd

MapStart<Alt3>
PluginDisplayName:""
PluginDisplayType: <Gate>

MapEnd
```

## options to fill

Gate:
SHAPE_GateRelease
SHAPE_Sustain
SHAPE_HardGate
SHAPE_Punch
SHAPE_Gate

Eq:
EQ_LF_Typ
EQ_LF_Freq
EQ_LF_Gain
EQ_LMF_Freq
EQ_LMF_Gain
EQ_LMF_Q
EQ_HMF_Freq
EQ_HMF_Gain
EQ_HMF_Q
EQ_HF_Type
EQ_HF_Freq
EQ_HF_Gain

Comp:
COMP_Release
COMP_Attack
COMP_Threshold
COMP_Ratio
