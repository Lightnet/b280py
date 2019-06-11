# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================

bl_info = {
    "name": "3D Viewport Custom Menu",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "menu",
}

import bpy

class HelloViewPortOperator(bpy.types.Operator):
    bl_idname = "object.helloviewport_operator"
    bl_label = "Hello Operator"

    def execute(self, context):
        print("hello viewport")
        return {'FINISHED'}

class BasicViewportMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_viewportmenu"
    bl_label = "custom menu"

    def draw(self, context):
        layout = self.layout
        #layout.operator("object.select_random", text="Random")
        #layout.operator("object.helloviewport_operator", text="Random")
        layout.operator("object.helloviewport_operator")


def addmenu_callback(self, context):	
	self.layout.menu("OBJECT_MT_viewportmenu")
    #self.layout.operator("object.helloviewport_operator")

#array
classes = (
    HelloViewPortOperator,
    BasicViewportMenu
)

def register():
    #print("Hello World")
    bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback)
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()