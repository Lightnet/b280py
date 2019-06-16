# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://blender.stackexchange.com/questions/3219/how-to-show-to-the-user-a-progression-in-a-script
bl_info = {
    "name": "Custom Progress bar console logging 01",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy
import sys
from time import sleep

def consoleoutput(self, context):
    sys.stdout.write("Some job description: ")
    sys.stdout.flush()
    some_list = [0] * 100
    for idx, item in enumerate(some_list):
        msg = "item %i of %i" % (idx, len(some_list)-1)
        sys.stdout.write(msg + chr(8) * len(msg))
        sys.stdout.flush()
        sleep(0.02)

    sys.stdout.write("DONE" + " "*len(msg)+"\n")
    sys.stdout.flush()


class TestBtnOperator(bpy.types.Operator):
    bl_idname = "object.testbtn_operator"
    bl_label = "Btn Test"

    def draw(self, context): # Draw options (typically displayed in the tool-bar)
        row = self.layout.row()
        row.label(text="Hello Dialog", icon='WORLD_DATA')

    def execute(self, context):
        print("test?")

        consoleoutput(self, context)

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        print(wm)
        return wm.invoke_props_dialog(self)
    
classes = (
    TestBtnOperator,
)

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
    kmi = km.keymap_items.new(TestBtnOperator.bl_idname, 'D', 'PRESS')
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