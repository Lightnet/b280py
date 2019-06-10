# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================

# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui
# https://docs.blender.org/api/blender2.8/bpy.types.Operator.html

bl_info = {
    "name": "Example Dialog Message",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "",
    "category": "",
}

import bpy

class DialogOperator(bpy.types.Operator):
    bl_idname = "object.dialog_operator"
    bl_label = "Simple Dialog Operator"
    
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

#bpy.utils.register_class(DialogOperator)
# Test call
#bpy.ops.object.dialog_operator('INVOKE_DEFAULT',infomsg="test")

#display button
class displaydialog_op(bpy.types.Operator):
    bl_idname = "object.displaydialog_op"
    bl_label = "Show Dialog"

    def execute(self, context):
        #print("Hello World sub")
        bpy.ops.object.dialog_operator('INVOKE_DEFAULT', infomsg="test") #DialogOperator.bl_idname = object.dialog_operator
        return {'FINISHED'}

#display File > Show Dialog
def draw_item_submenu(self, context):
    layout = self.layout
    layout.operator("object.displaydialog_op")

classes = (DialogOperator, displaydialog_op)

def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file.append(draw_item_submenu)# File Menu Top Left

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file.remove(draw_item_submenu)# File Menu Top Left

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()