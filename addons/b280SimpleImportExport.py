# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: WIP
# 
# ===============================================

# https://blender.stackexchange.com/questions/6159/changing-default-text-value-in-file-dialogue
# https://blender.stackexchange.com/questions/120608/does-blender-2-8-have-a-working-import-export-plugin-for-after-effects
# https://docs.blender.org/api/blender2.8/bpy.ops.export_scene.html
# https://docs.blender.org/api/blender2.8/info_tips_and_tricks.html
# https://docs.blender.org/api/blender2.8/bpy.types.Operator.html
# https://blender.stackexchange.com/questions/109711/how-to-popup-simple-message-box-from-python-console?noredirect=1&lq=1
# https://docs.blender.org/api/2.79/bpy.types.Operator.html?highlight=bpy%20types%20operator
# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui


bl_info = {
    "name": "Simple Import-Export",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "File > (Export | Import)",
    "category": "Import-Export",
}

import bpy
import time
import os

from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
)

from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper,
    orientation_helper,
    axis_conversion,
    )

class DialogIEOperator(bpy.types.Operator):
    bl_idname = "object.dialogie_operator"
    bl_label = "Simple DialogIE Operator"
    
    infomsg: bpy.props.StringProperty(name="Message",default="Fail?",options={'HIDDEN'})

    def draw(self, context): # Draw options (typically displayed in the tool-bar)
        row = self.layout
        row.prop(self, "report_flag", text="Report Hello World")
        row = self.layout.row()
        row.label(text=self.infomsg, icon='WORLD_DATA')

    def execute(self, context):
        message = (
                self.infomsg
        )
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        print(wm)
        return wm.invoke_props_dialog(self)

#bpy.utils.register_class(DialogIEOperator)
# Test call.
#bpy.ops.object.DialogIEOperator('INVOKE_DEFAULT',infomsg="test")

def do_import(context, props, filepath):
    print(filepath)
    file = open(filepath, "r")
    print(file.read())
    file.close()

    return True

def do_export(context, props, filepath):
    #file = open(filepath, "wb")
    file = open(filepath, "w")
    file.write("test")
    #file.flush()
    file.close()

    return True

class SimpleImporter(bpy.types.Operator,ImportHelper):
    """
    Import to the .txt model format (.txt)
    """
    bl_idname = "export.simpleimport"
    bl_label = ".txt import"
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        )

    def execute(self, context):
        start_time = time.time()
        props = self.properties
        filepath = self.filepath

        imported = do_import(context, props, filepath)

        if imported:
            print('finished import in %s seconds' %
                  ((time.time() - start_time)))
            print(filepath)
            #self.report({'ERROR'}, "Import Finish")
            #self.report({'INFO'}, "Import Finish")
            bpy.ops.object.dialogie_operator('INVOKE_DEFAULT', infomsg="Import Finish!")
        
        return {'FINISHED'}

class SimpleExporter(bpy.types.Operator,ExportHelper):
    """
    Export to the .txt model format (.txt)
    """
    bl_idname = "export.simpleexport"
    bl_label = ".txt Export"
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        )

    filepath = StringProperty(
        name=".txt",
        description="Filepath used for exporting the file",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    #check_extension = True

    bbinary: BoolProperty(
        name="Binary",
        description="Binary or Text export.",
        default=False,)

    def execute(self, context):
        start_time = time.time()
        print('\n_____START_____')
        props = self.properties
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)

        exported = do_export(context, props, filepath)

        if exported:
            print('finished export in %s seconds' %
                  ((time.time() - start_time)))
            print(filepath)
            #self.report({'INFO'}, "Export Finish")
            #self.report({'ERROR'}, "Export Finish")
            bpy.ops.object.dialogie_operator('INVOKE_DEFAULT', infomsg="Export Finish!")

        return {'FINISHED'}

    def invoke(self, context, event):
        #import os
        if not self.filepath:
            blend_filepath = context.blend_data.filepath
            if not blend_filepath:
                blend_filepath = "untitled"
            else:
                blend_filepath = os.path.splitext(blend_filepath)[0]

            self.filepath = blend_filepath + self.filename_ext

        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_import(self, context):
    self.layout.operator(SimpleImporter.bl_idname, text="Import (.txt)")

def menu_export(self, context):
    self.layout.operator(SimpleExporter.bl_idname, text="Export (.txt)")

#array
classes = (SimpleImporter, SimpleExporter, DialogIEOperator)

def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()