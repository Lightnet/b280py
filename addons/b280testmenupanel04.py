# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# https://blender.stackexchange.com/questions/109796/how-to-populate-a-menu-using-path-menu
# https://docs.blender.org/api/blender2.8/bpy.types.Menu.html
# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui
#
# https://blender.stackexchange.com/questions/42879/create-drop-down-list-in-menu-panel
# https://blender.stackexchange.com/questions/128261/how-do-i-create-an-enumproperty-dropdown-menu-that-shows-up-in-blender-2-8

bl_info = {
    "name": "Custom menu Panel 04",
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
        layout = self.layout
        print("test button")
        #layout.menu(Object_MT_BasicMenu.bl_idname, text="Presets", icon="SCENE")

        return {'FINISHED'}

# This class has to be exactly named like that to insert an entry in the right click menu
class WM_MT_button_context(bpy.types.Menu):
    bl_idname = "WM_MT_button_context"
    bl_label = "Unused"

    def draw(self, context):
        pass

class Object_MT_BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_BasicMenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        # Built-in operators
        layout.operator("wm.hello_world")
        layout.operator("wm.hello_world")
        layout.operator("wm.hello_world")

        layout.menu(WM_MT_button_context.bl_idname)

        #layout.operator(WM_MT_button_context.bl_idname, text="menu?")
        #layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        #layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        #layout.operator("object.select_random", text="Random")

#bpy.ops.wm.call_menu(name="OBJECT_MT_BasicMenu")

def execute_operator(self, context):
    #eval('bpy.ops.' + self.primitive + '()')
    print(self.primitive)
    pass

class MyShortAddonProperties(bpy.types.PropertyGroup):
    mode_options = [
        ("mesh.primitive_plane_add", "Plane", '', 'MESH_PLANE', 0),
        ("mesh.primitive_cube_add", "Cube", '', 'MESH_CUBE', 1),
        ("mesh.primitive_circle_add", "Circle", '', 'MESH_CIRCLE', 2),
        ("mesh.primitive_uv_sphere_add", "UV Sphere", '', 'MESH_UVSPHERE', 3),
        ("mesh.primitive_ico_sphere_add", "Ico Sphere", '', 'MESH_ICOSPHERE', 4),
        ("mesh.primitive_cylinder_add", "Cylinder", '', 'MESH_CYLINDER', 5),
        ("mesh.primitive_cone_add", "Cone", '', 'MESH_CONE', 6),
        ("mesh.primitive_torus_add", "Torus", '', 'MESH_TORUS', 7)
    ]

    primitive : bpy.props.EnumProperty(
        items=mode_options,
        description="offers....",
        default="mesh.primitive_plane_add",
        update=execute_operator
    )

# https://blender.stackexchange.com/questions/23356/populating-an-enumproperty-using-a-function

def get_items():
    #closure - keep a reference to the list
    items = None
    def func(self, context):
        items = [(group.name, group.name, "") for group in bpy.data.groups]
        return items
    item2 =[
        ("mesh.primitive_plane_add", "Plane", '', 'MESH_PLANE', 0),
        ("mesh.primitive_cube_add", "Cube", '', 'MESH_CUBE', 1),
        ("mesh.primitive_circle_add", "Circle", '', 'MESH_CIRCLE', 2)
    ]
    return item2
# https://blender.stackexchange.com/questions/117822/use-prop-search-per-uilist-item
# https://blender.stackexchange.com/questions/32912/where-to-prop-search-for-vertex-groups
class Fileq_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Objectq"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Menus", icon='WORLD_DATA')
        #list = []
        layout.operator("wm.hello_world")
        #row = layout.row()
        #layout.menu(Object_MT_BasicMenu.bl_idname, text="Presets", icon="SCENE")
        #layout.menu(WM_MT_button_context.bl_idname)
        col = layout.column()
        #col.label(text="Generate objects:")
        col.prop(context.scene.my_short_addon, "primitive",text="Shape")
        
        layout.prop_menu_enum(context.object, "enum_prop",text="Group")
        #print(context.object.enum_prop)
        # prarams object | collection list
        layout.prop_search(context.object, "test",bpy.context.scene,"objects",  text="search")
        print(context.object.test)

classes = (
    Fileq_Panel,
    WM_MT_button_context,
    WM_OT_Helloworld,
    Object_MT_BasicMenu,
    MyShortAddonProperties,
)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.myfile = StringProperty()
    bpy.types.Scene.my_short_addon = bpy.props.PointerProperty(type=MyShortAddonProperties)

    #bpy.types.Object.test = bpy.props.StringProperty(name="Group")
    bpy.types.Object.enum_prop = bpy.props.EnumProperty(items=get_items())

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback)
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()