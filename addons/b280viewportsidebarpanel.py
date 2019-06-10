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
# 
# 
# 

bl_info = {
    "name": "Viewport3D Sidebar Panel ",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

class CustomSideBarPanel(bpy.types.Panel):
    """Creates a Panel in the Sidebar"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_SideBarPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom Hello'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)

#array
classes = [
    CustomSideBarPanel
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