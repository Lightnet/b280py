# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: WIP
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.types.UILayout.html
#
#
# 

bl_info = {
    "name": "Custom Props Panel list test 01",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy
from bpy.types import Header, Panel, UIList
from rna_prop_ui import PropertyPanel

from bpy.props import EnumProperty

bpy.types.Scene.mycustomlist = EnumProperty(
        name="My Search",
        items=(
            ('FOO', "Foo", ""),
            ('BAR', "Bar", ""),
            ('BAZ', "Baz", ""),
        ),
    )

class BtnTestOperator(bpy.types.Operator):
    bl_idname = "object.btnbartest_operator"
    bl_label = "Hello"

    bl_property = "my_search"

    my_search: EnumProperty(
        name="My Search",
        items=(
            ('FOO', "Foo", ""),
            ('BAR', "Bar", ""),
            ('BAZ', "Baz", ""),
        ),
    )

    def execute(self, context):
        print("hello")
        self.report({'INFO'}, "Selected:" + self.my_search)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'RUNNING_MODAL'}

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomTooltest_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom"
    bl_idname = "OBJECT_PT_CustomNav"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    #bl_context = "object"
    #bl_options = {'DEFAULT_CLOSED'}
    #bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        #self.layout.operator('object.property_example')
        row = layout.row()
        row.label(text="Hello World", icon='WORLD_DATA')
        row = layout.row()
        row.operator('object.btnbartest_operator',icon='WORLD_DATA')

        row = layout.row()
        row.props_enum(scene, "mycustomlist")

        row = layout.row()
        row.prop_tabs_enum(scene, "mycustomlist")

        row = layout.row()
        row.prop_menu_enum(scene, "mycustomlist")

        #row = layout.row()
        #row.prop_search(scene, "mycustomlist",scene,"mycustomlist")
        
        


classes = (
    CustomTooltest_Panel,
    BtnTestOperator
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