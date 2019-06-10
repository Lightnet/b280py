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

bl_info = {
    "name": "topbar header",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy
from bpy.types import Header, Menu

class ACTOR_HT_header(Header):
    bl_space_type = 'TOPBAR'
    
    def draw(self, context):
        layout = self.layout
        #layout.template_header()
        layout.operator("object.select_random")
        pass

classes = []
classes.append(ACTOR_HT_header)

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