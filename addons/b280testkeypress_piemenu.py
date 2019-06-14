# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/manual/en/dev/advanced/keymap_editing.html
# https://blender.stackexchange.com/questions/54172/shortcut-to-execute-a-macro-or-script

# D Key Press 
bl_info = {
    "name": "Custom Key Map Press pie menu",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy
from bpy.types import Menu

class TestBtnOperator(bpy.types.Operator):
    bl_idname = "object.testbtn_operator"
    bl_label = "Btn Test"

    def execute(self, context):
        print("test?")
        return {'FINISHED'}

class OBJECT_Pie_Operater(bpy.types.Operator):
    """Origin to Selection"""
    bl_idname = "object.keyinputtest"
    bl_label = "Input Key Test"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        print("test....")
        bpy.ops.wm.call_menu_pie('INVOKE_DEFAULT',name="OBJECT_MT_pie_template")
        return {'FINISHED'}
# https://blender.stackexchange.com/questions/120237/how-would-one-code-a-pie-menu-with-an-additional-traditional-menu-beneath-it
class OBJECT_MT_template(Menu):
    bl_idname = "OBJECT_MT_pie_template"
    # label is displayed at the center of the pie menu.
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout
        #print("???")
        pie = layout.menu_pie()

        pie.operator("object.testbtn_operator")
        pie.operator("object.testbtn_operator")
        pie.operator("object.testbtn_operator")
        pie.operator("object.testbtn_operator")
        pie.operator("object.testbtn_operator")
        pie.operator("object.testbtn_operator")
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        #pie.operator_enum("mesh.select_mode", "type")
#array
classes = (
    TestBtnOperator,
    OBJECT_Pie_Operater,
    OBJECT_MT_template
)

# https://blender.stackexchange.com/questions/54172/shortcut-to-execute-a-macro-or-script
# https://blender.stackexchange.com/questions/40755/how-to-register-keymaps-for-all-editor-types
# store keymaps here to access after registration
# https://blenderartists.org/t/closed-register-a-keymap-for-all-editors-in-blender-2-8/1133692
# https://blender.stackexchange.com/questions/120237/how-would-one-code-a-pie-menu-with-an-additional-traditional-menu-beneath-it
addon_keymaps = []

def register():
    #print("Hello World")

    for cls in classes:
        bpy.utils.register_class(cls)

    # handle the keymap
    wm = bpy.context.window_manager
    #km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY', region_type='WINDOW')
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
    #kmi = km.keymap_items.new(WorkMacro.bl_idname, 'E', 'PRESS',alt=False, ctrl=False, shift=False)
    #kmi = km.keymap_items.new(WorkMacro.bl_idname, 'E', 'PRESS', alt=False, ctrl=False, shift=False)
    #kmi = km.keymap_items.new("OBJECT_MT_pie_template", 'E', 'PRESS', alt=False, ctrl=False, shift=False)
    kmi = km.keymap_items.new(OBJECT_Pie_Operater.bl_idname, 'D', 'PRESS')
    addon_keymaps.append(km)

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
    #bpy.ops.wm.call_menu_pie(name="VIEW3D_PIE_template")