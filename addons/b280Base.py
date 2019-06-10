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
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy

#array
classes = ()
"""
classes = (
    MyAddonPreferences,
    MyPropertyGroup,
    ADDON_OT_some_operator,
    ADDON_OT_some_other_operator,
    ADDON_PT_some_panel
)
register, unregister = bpy.utils.register_classes_factory(classes)
"""

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