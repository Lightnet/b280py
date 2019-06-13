# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# 
# https://blenderartists.org/t/blender-2-8-panel-location/1142035
# https://blender.stackexchange.com/questions/130671/creating-new-tabs-in-properties-panel
#
# https://docs.blender.org/api/blender2.8/bpy.types.SpaceProperties.html?highlight=spaceproperties#bpy.types.SpaceProperties
# 2.80\scripts\startup\bl_ui\space_properties.py
# https://blender.stackexchange.com/questions/134625/2-8-how-to-add-a-button-to-the-toolbar


bl_info = {
    "name": "Custom props dialog test",
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

class ConfirmTestOperator(bpy.types.Operator):
    bl_idname = "object.confirmtest"
    bl_label = "Hello Confirm?"

    checkme : bpy.props.BoolProperty(name="My Bool", default=False)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')
        row = layout.row()
        row.prop(self,"checkme")

    def execute(self, context):
        print(self.checkme)
        print("confirm?")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=250)

class Test_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Dialog Confirm"
    bl_idname = "OBJECT_PT_Test"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    #bl_context = "object"
    #bl_options = {'DEFAULT_CLOSED'}
    #bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        #layout = self.layout        
        self.layout.operator('object.confirmtest')

classes = (
    Test_Panel,
    ConfirmTestOperator,
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