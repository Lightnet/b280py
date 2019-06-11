# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
#
# https://docs.blender.org/api/blender2.8/bpy.types.Menu.html
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API
# https://docs.blender.org/api/blender2.8/info_quickstart.html
# https://blenderartists.org/t/editing-the-menu-bars-without-using-the-python-api/1126562/2
# 
#

bl_info = {
    "name": "Custom VIEW3D_MT_editor_menus Menu",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Menu",
}

import bpy

class custom_menu_op(bpy.types.Operator):
    bl_idname = "object.custom_menu_op"
    bl_label = "view3d custom menu"

    def execute(self, context):
        print("custom view3d menu")
        return {'FINISHED'}

class CustomMenu(bpy.types.Menu):
    bl_label = "Custom Menu"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.custom_menu_op")

def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)

classes = (
    custom_menu_op, 
    CustomMenu
)

def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_editor_menus.append(draw_item)# 

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_item)# 

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()