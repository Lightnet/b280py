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
# https://docs.blender.org/api/blender_python_api_2_76_release/bpy.types.Panel.html
# https://docs.blender.org/api/blender2.8/bpy.props.html?highlight=panel%20bl_category
# https://devtalk.blender.org/t/developing-a-new-editor/894/3
# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui
# 



# 
# 
#  https://blenderartists.org/t/need-help-wiht-addon-for-2-8/1132021/7


bl_info = {
    "name": "Custom Toolx panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy
from bpy.types import Header, Menu

class OBJECT_OT_property_example(bpy.types.Operator):
    bl_idname = "object.property_example"
    bl_label = "Property Example"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        return {'FINISHED'}

#class ACTOR_HT_header(Header):
class ACTOR_HT_header(bpy.types.Panel):
    #bl_space_type = 'EMPTY' #n
    bl_space_type = 'TOPBAR'
    
    def draw(self, context):
        layout = self.layout
        #layout.template_header()
        layout.operator("object.select_random")
        pass

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomToolx_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom ToolX Panel"
    bl_idname = "OBJECT_PT_CustomToolx"

    #works all tab props
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'

    #work tool tab
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_category = "Custom Hello"

    #work tool tab
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'

    #work all tool navbar
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_category = "Hello"

    # works
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'UI'
    #bl_category = 'Custom Hello'


    #not
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'
    #bl_category = "Beta"

    #not
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "TOOLS"
    #bl_category = "Custom Runtime"

    #my_float: bpy.props.FloatProperty(name="Some Floating Point")

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header(self, context):
        layout = self.layout
        obj = context.object
        #layout.prop(obj, "select", text="")

    def draw(self, context):
        layout = self.layout            
        obj = context.object
        row = layout.row()
        row.prop(obj, "hide_select")
        row.prop(obj, "hide_render")

        box = layout.box()
        box.label(text="Selection Tools")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")




        self.layout.operator('object.property_example')
        row = layout.row()
        row.label(text="Custom Tool All.", icon='WORLD_DATA')

        #props = self.layout.operator('object.property_example')
        #props.my_bool = True
        #props.my_string = "Shouldn't that be 47?"
        #row.operator("object.ht_operator")
        #print(context.mode) #edit, object
'''
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
'''
#array
'''
classes = (
    CustomToolx_Panel,
    CustomSideBarPanel
)
'''

classes = (
    #ACTOR_HT_header,
    CustomToolx_Panel,
    OBJECT_OT_property_example
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