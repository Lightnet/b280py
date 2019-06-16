# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# https://blender.stackexchange.com/questions/109796/how-to-populate-a-menu-using-path-menu


bl_info = {
    "name": "Custom file Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "PROPERTIES",
    "category": "Object"
}

import bpy
import time
import os
from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
)

def validinsert(ext):
	return ext in {".txt",".inc",".pov"}

class FileQ_Operator(bpy.types.Operator):
    bl_idname = "object.fileq_operator"
    bl_label = "File Path"
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        )

    filepath : StringProperty(
        name=".txt",
        description="Filepath used for exporting the file",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    def execute(self, context):
        start_time = time.time()
        print('\n_____START_____')
        props = self.properties
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)

        #exported = do_export(context, props, filepath)
        exported = True

        if exported:
            print('finished export in %s seconds' %
                  ((time.time() - start_time)))
            print(filepath)
            #self.report({'INFO'}, "Export Finish")
            #self.report({'ERROR'}, "Export Finish")
            #bpy.ops.object.dialogie_operator('INVOKE_DEFAULT', infomsg="Export Finish!")
            bpy.data.scenes[0].myfile = filepath

        return {'FINISHED'}

    def invoke(self, context, event):
        import os
        if not self.filepath:
            blend_filepath = context.blend_data.filepath
            if not blend_filepath:
                blend_filepath = "untitled"
            else:
                blend_filepath = os.path.splitext(blend_filepath)[0]

            self.filepath = blend_filepath + self.filename_ext
            
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# This class has to be exactly named like that to insert an entry in the right click menu
class WM_MT_button_context(bpy.types.Menu):
    bl_label = "Unused"

    def draw(self, context):
        pass


class Object_MT_BasicMenu(bpy.types.Menu):
    bl_idname = "Object_MT_BasicMenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout
        list = []
        #row = layout.row()
        #row.operator("object.fileq_operator")
        """
        self.path_menu(list,
                       "object.fileq_operator",
                       #{"internal": True},
					   filter_ext= validinsert
                       )
        """
#bpy.ops.wm.call_menu(name="OBJECT_MT_BasicMenu")

class Fileq_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Objectq"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Objectq", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.prop(context.scene,"myfile")
        list = []
        row = layout.row()
        row.operator("object.fileq_operator")
        #row.menu(Object_MT_BasicMenu.bl_idname)
        """
        layout.path_menu(list,
                       "object.fileq_operator",
                       #{"internal": True},
					   filter_ext= validinsert
                       )
        """

classes = (
    Fileq_Panel,
    FileQ_Operator,
    WM_MT_button_context,
    #Object_MT_BasicMenu,
)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.myfile = StringProperty()

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback)
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()