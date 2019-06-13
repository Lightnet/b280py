# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================

bl_info = {
    "name": "custom gpu draw line",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

# https://www.youtube.com/watch?v=EgrgEoNFNsA

import bpy
from . draw_op import OT_draw_operator

addon_kymaps = []

#array
classes = ()

def register():
    #print("Hello World")

    #for cls in classes:
        #bpy.utils.register_class(cls)

    bpy.utils.register_class(OT_draw_operator)

    kcfg = bpy.context.window_manager.keyconfig.addons
    if kcfg:
        km = kcfg.keymaps.new(name='3D View',space_type='VIEW_3D')

        kmi = km.keymap_items.new('object.draw_op','F','PRESS',shift=True,ctrl=True)

        addon_kymaps.append((km,kmi))


def unregister():
    #print("Goodbye World")
    #for cls in classes:
        #bpy.utils.unregister_class(cls)

    for km, kmi in addon_kymaps:
        km.keymap_items.remove(kmi)

    addon_kymaps.clear()

    bpy.utils.unregister_class(OT_draw_operator)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()