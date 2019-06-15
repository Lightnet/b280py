# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://blender.stackexchange.com/questions/102871/how-to-check-a-json-file-dynamically-with-blender?rq=1
# https://blender.stackexchange.com/questions/102644/dynamic-generated-json-file-read
#
#
#
# https://www.w3schools.com/python/python_json.asp

bl_info = {
    "name": "Custom read/write Json",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy
import json

from bpy.props import (
    #BoolProperty,
    #EnumProperty,
    StringProperty,
)

class createjson_Operator(bpy.types.Operator):
    bl_idname = "object.createjson_operator"
    bl_label = "Create json"
    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        )

    filepath : StringProperty(
        name=".json",
        description="Filepath used for exporting the file",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    def execute(self, context):


        # a Python object (dict):
        x = {
        "name": "John",
        "type": "object"
        }

        # convert into JSON:
        y = json.dumps(x)
        # the result is a JSON string:
        print(y)

        return {'FINISHED'}
# https://www.w3schools.com/python/python_json.asp
class readjson_Operator(bpy.types.Operator):
    bl_idname = "object.readjson_operator"
    bl_label = "Read json"
    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        )

    filepath : StringProperty(
        name=".json",
        description="Filepath used for exporting the file",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    def execute(self, context):
        
        x =  '{ "name":"John", "age":30, "city":"New York"}'
        # parse x:
        y = json.loads(x)
        # the result is a Python dictionary:
        print(y["age"])
        

        return {'FINISHED'}

class Objectjson_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Object Json Panel"
    bl_idname = "OBJECT_PT_Objectjson"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.operator("object.readjson_operator")
        col.operator("object.createjson_operator")

#array
classes = (
    Objectjson_Panel,
    readjson_Operator,
    createjson_Operator
)


def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()