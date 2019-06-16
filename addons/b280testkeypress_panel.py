# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/manual/en/dev/advanced/keymap_editing.html
# https://blender.stackexchange.com/questions/54172/shortcut-to-execute-a-macro-or-script
# https://docs.blender.org/api/blender2.8/bpy.ops.wm.html?highlight=panel#bpy.ops.wm.call_panel
# D Key Press 
bl_info = {
    "name": "Custom Key Map Press panel",
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

class TestBtnPanelOperator(bpy.types.Operator):
    bl_idname = "object.testbtnpanel_operator"
    bl_label = "Btn Test"

    def execute(self, context):
        print("test?")
        return {'FINISHED'}

class Test_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Progress"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = "object"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Hello Panel", icon='WORLD_DATA')
        col.operator("object.testbtnpanel_operator")
        col.label(text="Hello Panel", icon='WORLD_DATA')
        

    
#array
classes = (
    Test_Panel,
    TestBtnPanelOperator,
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
    #kmi = km.keymap_items.new(TestBtnOperator.bl_idname, 'D', 'PRESS')
    kmi = km.keymap_items.new('wm.call_panel', 'D', 'PRESS')
    kmi.properties.name = Test_Panel.bl_idname
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