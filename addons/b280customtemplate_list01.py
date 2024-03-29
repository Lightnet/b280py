# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: WIP
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.types.UILayout.html
# https://docs.blender.org/api/blender2.8/bpy.props.html
# https://blender.stackexchange.com/questions/19686/remove-from-collectionproperty
# https://blender.stackexchange.com/questions/23623/collectionproperty-change-items-index?rq=1

# ListItem
# 2.80\scripts\startup\bl_ui\properties_scene.py
# col.template_list("UI_UL_list", "keying_sets", scene, "keying_sets", scene.keying_sets, "active_index", rows=1)
# 
bl_info = {
    "name": "Custom Template List 01",
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
# https://blenderartists.org/t/creating-a-random-string/504679
import random,time

from bpy.props import EnumProperty, CollectionProperty, IntProperty, StringProperty, BoolProperty

def random_id(length = 8):
    """ Generates a random alphanumeric id string.
    """
    tlength = int(length / 2)
    rlength = int(length / 2) + int(length % 2)

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = ""
    for i in range(0, rlength):
        text += random.choice(chars)
    text += str(hex(int(time.time())))[2:][-tlength:].rjust(tlength, '0')[::-1]
    return text

class ExamplePropsGroup(bpy.types.PropertyGroup):
    boolean : BoolProperty(default=False)
    name : StringProperty() #default for name display in list
    bexport : BoolProperty(default=False, name="Export", options={"HIDDEN"},
                           description = "This will be ignore when exported")
    bselect : BoolProperty(default=False, name="Select", options={"HIDDEN"},
                           description = "This will be ignore when exported")
    otype : StringProperty(name="Type",description = "This will be ignore when exported")

class BtnCAddOperator(bpy.types.Operator):
    bl_idname = "object.btncadd_operator"
    bl_label = "Add"

    def execute(self, context):
        #print("hello")
        #self.report({'INFO'}, "Selected:" + self.my_search)
        scene = context.scene
        print(scene.examplecollection_list)

        my_item = bpy.data.scenes[0].examplecollection_list.add()
        my_item.name = random_id()

        for my_item in bpy.data.scenes[0].examplecollection_list:
            print(my_item.name)

        return {'FINISHED'}

class BtnCRemoveOperator(bpy.types.Operator):
    bl_idname = "object.btncremove_operator"
    bl_label = "Remove"

    def execute(self, context):
        #print("hello")
        #self.report({'INFO'}, "Selected:" + self.my_search)
        scene = context.scene
        print(scene.examplecollection_list)
        scene.examplecollection_list.remove(scene.examplecollection_list_idx)
        print(scene.examplecollection_list_idx)
        return {'FINISHED'}

class BtnCClearOperator(bpy.types.Operator):
    bl_idname = "object.btncclear_operator"
    bl_label = "Clear"

    def execute(self, context):
        #print("hello")
        #self.report({'INFO'}, "Selected:" + self.my_search)
        scene = context.scene
        scene.examplecollection_list.clear()
        return {'FINISHED'}

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomTemplateList_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom"
    bl_idname = "OBJECT_PT_CustomTemplateList"

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
        row.label(text="Collection Group List!", icon='WORLD_DATA')
        row = layout.row()
        #row.operator('object.btnbartest_operator',icon='WORLD_DATA')
        row.operator('object.btncadd_operator')
        row.operator('object.btncremove_operator')
        row.operator('object.btncclear_operator')

        row = layout.row()
        row.template_list("UI_UL_list", "examplecollection_list", context.scene, "examplecollection_list",
                                 context.scene, "examplecollection_list_idx", rows=5)

        bfounditem = False
        for i in range(len(scene.examplecollection_list)):
            if i == scene.examplecollection_list_idx:
                bfounditem = True
                break
            
        if bfounditem == True:
            item = scene.examplecollection_list[scene.examplecollection_list_idx]
            if item != None:
                row = layout.row()
                row.prop(item, "name")
                row.prop(item, "bexport")
                row.prop(item, "bselect")
                row.prop(item, "otype")
        row = layout.row()
        row.prop(scene, "examplecollection_list")

classes = (
    CustomTemplateList_Panel,
    BtnCAddOperator,
    BtnCRemoveOperator,
    BtnCClearOperator,
)

def register():
    #print("Hello World")

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.utils.register_class(ExamplePropsGroup)
    bpy.types.Scene.examplecollection_list = CollectionProperty(type=ExamplePropsGroup)
    bpy.types.Scene.examplecollection_list_idx = IntProperty()

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.utils.unregister_class(ExamplePropsGroup)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()