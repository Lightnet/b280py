# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
#
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons
# https://blenderartists.org/t/need-help-wiht-addon-for-2-8/1132021/2
# https://docs.blender.org/api/blender_python_api_2_76_release/bpy.types.Panel.html
# 
# #tool is on left where viewport3d

bl_info = {
    "name": "custom view3d toolbar",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomToolBar_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Tool Bar Panel"
    bl_idname = "OBJECT_PT_CustomToolBar"

    #work tool tab
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row = layout.row()
        row.label(text="Toolbar.", icon='WORLD_DATA')
        #row.operator("object.ht_operator")
        #print(context.mode) #edit, object

#array
classes = [
    CustomToolBar_Panel
]

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