# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================

bl_info = {
    "name": "Custom Panel UE4",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object"
}

import bpy

class UNOUE_OP_Export(bpy.types.Operator):
    bl_idname = "object.unop_export_operator"
    bl_label = "Export"

    def execute(self, context):
        print("Hello World")
        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}

class UE4_UNOExport_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UNOUE4 Panel"
    bl_idname = "OBJECT_PT_UNOUE"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="UNOUE4 Export", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("object.unop_export_operator")

classes = (
    UE4_UNOExport_Panel,
    UNOUE_OP_Export
)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)  
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback) 
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()