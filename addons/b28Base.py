bl_info = {
    "name": "Base",
    "author":"Lightnet",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

#array
classes = (

            )

def register():
    print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)  
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback) 
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()