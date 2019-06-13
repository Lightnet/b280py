# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# bpy.context.scene.update()
# https://blender.stackexchange.com/questions/109796/how-to-populate-a-menu-using-path-menu
# https://docs.blender.org/api/blender2.8/bpy.types.Menu.html
# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui

bl_info = {
    "name": "Custom menu Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "PROPERTIES",
    "category": "Object"
}

import bpy
import time
import os
from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
)

class WM_OT_Helloworld(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "hello world"

    def execute(self, context):
        print("test 11")
        return {'FINISHED'}

# This class has to be exactly named like that to insert an entry in the right click menu
class WM_MT_button_context(bpy.types.Menu):
    bl_label = "Unused"

    def draw(self, context):
        pass

class Object_MT_BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_BasicMenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        # Built-in operators
        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

#bpy.ops.wm.call_menu(name="OBJECT_MT_BasicMenu")

class Fileq_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Objectq"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        #obj = context.object
        row = layout.row()
        row.label(text="Objectq", icon='WORLD_DATA')
        #row = layout.row()
        #row.label(text="Active object is: " + obj.name)
        #row = layout.row()
        #row.prop(obj, "name")

        #row = layout.row()
        #row.prop(context.scene,"myfile")
        #list = []
        layout.operator("wm.hello_world")
        #row = layout.row()
        layout.menu(Object_MT_BasicMenu.bl_idname, text="Presets", icon="SCENE")

classes = (
    Fileq_Panel,
    WM_MT_button_context,
    WM_OT_Helloworld,
    Object_MT_BasicMenu,
)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.myfile = StringProperty()

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback)
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()