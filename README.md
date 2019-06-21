# b280py

# License: MIT

# Information:
  Simple files test build addons. Those just test files to deal with simple menu setup that I know.

# Notes:
 * My Scripting file are currently messy. It base on idea and researching from blender API, scripting workspace, the blender community, and dev site blender and stack(Q&A).
 * Cheatsheet under Blender > Help > Cheatsheet
    * Under workspace > scripting / Texteditor > Browse List icon
 * Blender > workspace > scripting > Templates (few script tend to crash)

# Links:
 * https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html

 ```
bl_info = {
    "name": "Base",
    "author":"name",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
    "description":"testing menu"
}

import bpy

#array class
classes = (...)

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
 ```