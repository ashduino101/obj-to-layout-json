#Imports
import os
import json
#Variables
outputpoints = '''
{ "m_Pos": { "x": 21.25, "y": 9.25, "z": 5.0 }, "m_Rot": { "x": -0.0, "y": -0.0, "z": -0.0, "w": 1.0 }, "m_Scale": { "x": 1.0, "y": 1.0, "z": 3.2 }, "m_Dynamic": false, "m_CollidesWithRoad": true, "m_CollidesWithNodes": false, "m_CollidesWithSplitNodes": false, "m_Flipped": false, "m_RotationDegrees": 0.0, "m_Mass": 40.0, "m_Bounciness": 0.5, "m_PinMotorStrength": 0.0, "m_PinTargetVelocity": 0.0, "m_Color": { "r": 0.16470589, "g": 0.16470589, "b": 0.16470589, "a": 1.0 }, "m_PointsLocalSpace": [ 
'''
outputend = '''
], "m_DynamicAnchorGuids": [], "m_UndoGuid": null }
'''
#Data to put before CS data
default_pre_data = ('''
 {
  "m_Version": 25,
  "m_ThemeStubKey": "Western",
  "m_BridgeJoints": [],
  "m_BridgeEdges": [],
  "m_Pistons": [],
  "m_Anchors": [
    { "m_Pos": { "x": 0.0, "y": 5.0, "z": 0.0 }, "m_IsAnchor": true, "m_IsSplit": false, "m_Guid": "de549ea0-6a2d-4886-83dc-dde75fe6cffe" },
    { "m_Pos": { "x": 12.0, "y": 5.0, "z": 0.0 }, "m_IsAnchor": true, "m_IsSplit": false, "m_Guid": "149aa130-7106-4ee1-b450-1f819e7b54df" }
  ],
  "m_HydraulicsPhases": [],
  "m_Bridge": {
    "m_Version": 9,
    "m_BridgeJoints": [],
    "m_BridgeEdges": [],
    "m_BridgeSprings": [],
    "m_Pistons": [],
    "m_HydraulicsController": { "m_Phases": [] },
    "m_Anchors": [ { "m_Pos": { "x": 0.0, "y": 5.0, "z": 0.0 }, "m_IsAnchor": true, "m_IsSplit": false, "m_Guid": "de549ea0-6a2d-4886-83dc-dde75fe6cffe" }, { "m_Pos": { "x": 12.0, "y": 5.0, "z": 0.0 }, "m_IsAnchor": true, "m_IsSplit": false, "m_Guid": "149aa130-7106-4ee1-b450-1f819e7b54df" } ]
  },
  "m_ZedAxisVehicles": [],
  "m_Vehicles": [
    { "m_Pos": { "x": -4.25, "y": 5.11 }, "m_DisplayName": "", "m_Rot": { "x": -0.0, "y": -0.0, "z": -0.0, "w": 1.0 }, "m_PrefabName": "CompactCar", "m_TargetSpeed": 5.0, "m_Mass": 14.0, "m_BrakingForceMultiplier": 2.5, "m_StrengthMethod": 0, "m_Acceleration": 5.0, "m_MaxSlope": 0.0, "m_DesiredAcceleration": 1.0, "m_ShocksMultiplier": 1.0, "m_RotationDegrees": 0.0, "m_TimeDelaySeconds": 0.0, "m_IdleOnDownhill": true, "m_Flipped": false, "m_OrderedCheckpoints": false, "m_Guid": "f9e34c1e-0cb0-4365-add8-17b30f476ef4", "m_CheckpointGuids": [], "m_UndoGuid": null }
  ],
  "m_VehicleStopTriggers": [
    { "m_Pos": { "x": 17.0, "y": 5.1 }, "m_Rot": { "x": -0.0, "y": -0.0, "z": -0.0, "w": 1.0 }, "m_Height": 1.75, "m_RotationDegrees": 0.0, "m_Flipped": false, "m_PrefabName": "VictoryFlag", "m_StopVehicleGuid": "f9e34c1e-0cb0-4365-add8-17b30f476ef4", "m_UndoGuid": null }
  ],
  "m_EventTimelines": [
    { "m_CheckpointGuid": "", "m_Stages": [ { "m_Units": [ { "m_Guid": "f9e34c1e-0cb0-4365-add8-17b30f476ef4" } ] } ] }
  ],
  "m_Checkpoints": [],
  "m_TerrainStretches": [
    { "m_Pos": { "x": 0.0, "y": 0.0, "z": 0.0 }, "m_PrefabName": "Terrain_BookEndA", "m_HeightAdded": 0.0, "m_RightEdgeWaterHeight": 3.0, "m_TerrainIslandType": 0, "m_VariantIndex": 0, "m_Flipped": false, "m_LockPosition": false, "m_UndoGuid": null },
    { "m_Pos": { "x": 12.0, "y": 0.0, "z": 0.0 }, "m_PrefabName": "Terrain_BookEndC", "m_HeightAdded": 0.0, "m_RightEdgeWaterHeight": 0.0, "m_TerrainIslandType": 0, "m_VariantIndex": 2, "m_Flipped": true, "m_LockPosition": false, "m_UndoGuid": null }
  ],
  "m_Pillars": [],
  "m_Platforms": [],
  "m_Ramps": [],
  "m_VehicleRestartPhases": [],
  "m_FlyingObjects": [],
  "m_Rocks": [],
  "m_SupportPillars": [],
  "m_WaterBlocks": [
    { "m_Pos": { "x": 5.9999995, "y": 1.5, "z": 0.0 }, "m_Width": 11.999999, "m_Height": 3.0, "m_LockPosition": false, "m_UndoGuid": null }
  ],
  "m_CustomShapes": [
  
  ''')
default_post_data = ''' ], "m_StaticPins": [ { "x": 0, "y": 0, "z": 0 }, { "x": 1, "y": 1, "z": 1 } ], "m_DynamicAnchorGuids": [], "m_UndoGuid": null }
  ],
  "m_Budget": {
    "m_CashBudget": 10000000,
    "m_RoadBudget": 100,
    "m_WoodBudget": 100,
    "m_SteelBudget": 100,
    "m_HydraulicBudget": 100,
    "m_RopeBudget": 100,
    "m_CableBudget": 100,
    "m_SpringBudget": 100,
    "m_BungieRopeBudget": 100,
    "m_AllowWood": true,
    "m_AllowSteel": true,
    "m_AllowHydraulic": true,
    "m_AllowRope": true,
    "m_AllowCable": true,
    "m_AllowSpring": true,
    "m_AllowReinforcedRoad": true
  },
  "m_Settings": {
    "m_HydraulicControllerEnabled": false,
    "m_Unbreakable": false
  },
  "m_Workshop": {
    "m_Id": "",
    "m_LeaderboardId": "",
    "m_Title": "",
    "m_Description": "",
    "m_AutoPlay": false,
    "m_Tags": []
  }
}
'''
#Find first object file
for root, dirs, files in os.walk(r'Input'):
    for file in files:
        if file.endswith('.obj'):
            objfile = os.path.join(root, file)
#Open the object model
obj = open(objfile)
#Read object
readobj = obj.read()
obj.seek(0) 
#Find line count of object
obj2 = readobj.split("\n")
linec = len(obj2)
for line in obj:
    lineprocess = line.strip()
    if lineprocess.startswith("v"):
        lineprocess = lineprocess.replace("v ", "")
        for word in lineprocess:
            coords = lineprocess.split()
        x = coords[0]
        y = coords[1]
        z = coords[2]
        outputpoints = outputpoints + '{ "x": ' + x + ', "y": ' + y + ', "z": ' + z + ' }, '
completeJSON = default_pre_data + outputpoints + default_post_data
with open("output.layout.json", "w") as outfile:
    outfile.write(completeJSON)