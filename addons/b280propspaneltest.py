# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: WIP
# 
# ===============================================
# 
# https://blenderartists.org/t/blender-2-8-panel-location/1142035
# https://blender.stackexchange.com/questions/130671/creating-new-tabs-in-properties-panel
#
# https://docs.blender.org/api/blender2.8/bpy.types.SpaceProperties.html?highlight=spaceproperties#bpy.types.SpaceProperties
# 2.80\scripts\startup\bl_ui\space_properties.py
# https://blender.stackexchange.com/questions/134625/2-8-how-to-add-a-button-to-the-toolbar
#
# https://docs.blender.org/api/blender2.8/bpy.props.html
# 
# space_properties.py
# 
# 
# 

bl_info = {
    "name": "Custom Props Tool Panel test",
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

# Assign a custom property to an existing type.
#bpy.types.Custom = bpy.props.StringProperty(name="Custom")

Custom = bpy.props.StringProperty(name="Custom")
#bpy.utils.register_class(Custom)

# Assign a collection.
class CustomSettingItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Custom", default="Unknown")
    value: bpy.props.IntProperty(name="Test Property", default=22)
bpy.utils.register_class(CustomSettingItem)

def get_float(self):
    return self["testprop"]


def set_float(self, value):
    self["testprop"] = value

bpy.types.Scene.custom = bpy.props.FloatProperty(get=get_float, set=set_float)


#bpy.types.Custom = bpy.props.CollectionProperty(type=CustomSettingItem)
#Custom = bpy.props.CollectionProperty(type=CustomSettingItem)
#print(dir(bpy.types))
#bpy.types.append(Custom)

class PROPERTIES_HT_Custom(Header):
    bl_space_type = 'PROPERTIES'

    def draw(self, _context):
        layout = self.layout
        layout.template_header()
        layout.operator("object.navbartest_operator")
        #layout.menu("FILEBROWSER_MT_view")
        #layout.template_header()

class NavTestOperator(bpy.types.Operator):
    bl_idname = "object.navbartest_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("hello viewport")
        return {'FINISHED'}

class CustomContextOperator(bpy.types.Operator):
    bl_idname = "object.customcontext_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("navbar")
        return {'FINISHED'}


class CustomButtonsPanel:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "custom"

class Custom_PT_custom_props(CustomButtonsPanel, PropertyPanel, Panel):
    _context_path = "custom"
    #_property_type = ()
    _property_type = bpy.types.Scene

    #_context_path = "custom"
    #_property_type = bpy.types.Scene

    #_property_type = bpy.types.Custom
    #_property_type = Custom


# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomNav_Panel(CustomButtonsPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = ""
    bl_idname = "OBJECT_PT_CustomNav"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'NAVIGATION_BAR'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        view = context.space_data
        layout.scale_x = 1.4
        layout.scale_y = 1.4
        # https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/UI_API
        #layout.operator('object.customcontext_operator',icon='WORLD_DATA')
        layout.operator('object.customcontext_operator',icon='HEART')

class Custom_PT_Context(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "custom"
    bl_label = ""

    bl_options = {'HIDE_HEADER'}

    #@classmethod
    #def poll(cls, context):
        #return context.scene
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')


#array
classes = [
    PROPERTIES_HT_Custom,
    CustomNav_Panel,
    NavTestOperator,
    CustomContextOperator,
    Custom_PT_Context,
    Custom_PT_custom_props
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