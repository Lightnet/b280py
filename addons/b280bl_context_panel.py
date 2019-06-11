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
#

bl_info = {
    "name": "Custom bl_context Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "PROPERTIES",
    "category": "object",
    "warning": "",
    "wiki_url": "",
}

import bpy

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class CustomToolx_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Tool Render Panel"
    bl_idname = "OBJECT_PT_CustomToolRender"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = "render"
    #bl_context = "output"
    #bl_context = "view_layer" #view layer
    #bl_context = "scene"
    #bl_context = "world"
    bl_context = "object"
    #bl_context = "modifier"
    #bl_context = "particle" # Particles
    #bl_context = "effects" #unknown
    #bl_context = "physics"
    #bl_context = "constraint" #object constraint
    #bl_context = "bone"
    #bl_context = "bone_constraint"
    #bl_context = "data" #object data
    #bl_context = "material"
    #bl_context = "texture"

    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout        

        self.layout.operator('object.property_example')
        row = layout.row()
        row.label(text="Custom Tool All.", icon='WORLD_DATA')

classes = [CustomToolx_Panel]

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