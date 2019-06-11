# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
#

# 
# #tool is on left where viewport3d

bl_info = {
    "name": "custom view3d toolbar panel (left)",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

class HDToolOperator(bpy.types.Operator):
    bl_idname = "object.hdtool_operator"
    bl_label = "Hello Tool Operator"
    #infomsg: bpy.props.StringProperty(name="Message",default="Fail?",options={'HIDDEN'})

    def execute(self, context):
        print("tool bar")
        return {'FINISHED'}


class CustomToolBar_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Tool Bar Panel"
    bl_idname = "OBJECT_PT_CustomToolBar"

    #work tool tab
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    #bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        #obj = context.object
        #row = layout.row()
        #row.label(text="Toolbar.", icon='WORLD_DATA')
        layout.scale_x = 1.4
        layout.scale_y = 1.4
        row = layout.row()
        row.operator("object.hdtool_operator", icon='WORLD_DATA')
        #print(context.mode) #edit, object

#array
classes = [
    CustomToolBar_Panel,
    HDToolOperator
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