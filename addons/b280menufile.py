# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================

bl_info = {
    "name": "Custom Menu File Submenu",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "File",
    "category": "Menu",
}

import bpy

#display button
class custom_submenu_op(bpy.types.Operator):
    bl_idname = "object.custom_submenu_op"
    bl_label = "sub menu"

    def execute(self, context):
        print("Hello World sub")
        return {'FINISHED'}

#display menu with sub menu
class CustomMenu(bpy.types.Menu):
    bl_label = "custom file submenu"
    bl_idname = "OBJECT_MT_custom_file_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.custom_submenu_op")
        print("hello submenu file")

#display either button menu or menu with submenu
def draw_item_submenu(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)
    #layout.operator("object.custom_submenu_op")


classes = (CustomMenu, 
    custom_submenu_op
    )

def register():
    #print("Hello World")
    bpy.types.TOPBAR_MT_file.append(draw_item_submenu)# File Menu Top Left

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    bpy.types.TOPBAR_MT_file.remove(draw_item_submenu)

    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()