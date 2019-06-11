# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
#

bl_info = {
    "name": "Custom Tool and workspace settings Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "Active Tool and workspace settings",
    "category": "Panel",
}

import bpy

class HelloActionOperator(bpy.types.Operator):
    bl_idname = "object.helloaction_operator"
    bl_label = "Hello Operator"

    def execute(self, context):
        print("Hello World! op!")
        return {'FINISHED'}

#[PROPERTIES] display tool tab in panel sub PROPERTIES
class HelloCustomTool_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello Custom Tool Panel"
    bl_idname = "OBJECT_PT_HelloCustomTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')

        row = layout.row()
        row.operator("object.helloaction_operator")
        #print(context.mode) #edit, object

classes = (HelloActionOperator,
    HelloCustomTool_Panel
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