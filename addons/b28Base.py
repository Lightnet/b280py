# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================

bl_info = {
    "name": "Base",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

#array
classes = ()

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