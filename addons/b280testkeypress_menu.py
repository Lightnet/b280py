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
    "name": "Custom Key Map Press menu",
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

class OBJECT_test_operator(bpy.types.Operator):
    bl_idname = "object.test_operator"
    bl_label = "Input Key Test"
    def execute(self, context):
        return {'FINISHED'}

class OBJECT_Btn_operator(bpy.types.Operator):
    bl_idname = "object.btn_operator"
    bl_label = "Input Key Test"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        print("test....")
        #bpy.ops.wm.call_menu_pie('INVOKE_DEFAULT',name="OBJECT_MT_pie_template")
        bpy.ops.wm.call_menu('INVOKE_DEFAULT',name="OBJECT_MT_pie_template")
        return {'FINISHED'}

# https://blender.stackexchange.com/questions/120237/how-would-one-code-a-pie-menu-with-an-additional-traditional-menu-beneath-it
class OBJECT_PIE_template(Menu):
    bl_idname = "OBJECT_MT_pie_template"
    # label is displayed at the center of the pie menu.
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout
        print("???")
        layout.operator("object.test_operator")
        #pie = layout.menu_pie()
        #pie.operator("object.testbtn_operator")
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        #pie.operator_enum("mesh.select_mode", "type")
#array
classes = (
    OBJECT_Btn_operator,
    OBJECT_PIE_template,
    OBJECT_test_operator,
)

# https://blender.stackexchange.com/questions/54172/shortcut-to-execute-a-macro-or-script
# https://blender.stackexchange.com/questions/40755/how-to-register-keymaps-for-all-editor-types
# store keymaps here to access after registration
# https://blenderartists.org/t/closed-register-a-keymap-for-all-editors-in-blender-2-8/1133692
# https://blender.stackexchange.com/questions/120237/how-would-one-code-a-pie-menu-with-an-additional-traditional-menu-beneath-it
# https://blender.stackexchange.com/questions/3465/how-do-i-catch-keyboard-input-for-a-blender-plugin
# https://blender.stackexchange.com/questions/1497/how-can-i-call-a-specific-keymap-to-draw-within-my-addonpreferences
# https://stackoverflow.com/questions/19554023/how-to-capture-keyboard-input-in-blender-using-python
addon_keymaps = []
#wm = bpy.context.window_manager
#km = wm.keyconfigs.addon.keymaps.new(name='3D View Generic', space_type='VIEW_3D')
#kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True)
#kmi.properties.name = "VIEW3D_MT_ManipulatorMenu"
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
    kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS')
    kmi.properties.name = "OBJECT_MT_pie_template"
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