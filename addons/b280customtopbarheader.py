# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
#


bl_info = {
    "name": "custom topbar header right side",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "TOPBAR",
    "category": "Object",
}

import bpy
from bpy.types import Header, Menu

class HelloheadOperator(bpy.types.Operator):
    bl_idname = "object.hellohead"
    bl_label = "Top Header"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

class ACTOR_HT_header(Header):
    bl_space_type = 'TOPBAR'
    
    def draw(self, context):
        layout = self.layout
        #layout.operator("object.select_random")
        layout.operator("object.hellohead")
        pass

classes = (
    ACTOR_HT_header,
    HelloheadOperator
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