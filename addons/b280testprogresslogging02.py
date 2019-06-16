# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://blender.stackexchange.com/questions/3219/how-to-show-to-the-user-a-progression-in-a-script
bl_info = {
    "name": "Custom Progress bar console logging 02",
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

# https://blender.stackexchange.com/questions/3219/how-to-show-to-the-user-a-progression-in-a-script
# https://blenderartists.org/t/showing-progress-of-your-script-running/647230/9
# https://blender.stackexchange.com/questions/138973/blender-2-8-event-timer-add-error
# https://blenderartists.org/t/showing-progress-of-your-script-running/647230/10
# https://stackoverflow.com/questions/13485720/blender-python-scripting-trying-to-prevent-ui-lock-up-while-doing-large-calcula
# https://docs.blender.org/api/master/bpy.types.Operator.html?highlight=cancel#bpy.types.Operator.cancel
# https://blender.stackexchange.com/questions/120868/network-decode-with-modal-operator

#Blender 2.8 > scripting > template > operator_modal_timer.py
class TestBtnOperator(bpy.types.Operator):
    bl_idname = "object.testbtn_operator"
    bl_label = "Run with progress"
    bl_options = {'REGISTER', 'INTERNAL'}

    _updating = False
    _calcs_done = False
    _timer = None

    def do_calcs(self):
        wm = bpy.context.window_manager
        # would be good if you can break up your calcs
        # so when looping over a list, you could do batches
        # of 10 or so by slicing through it.
        # do your calcs here and when finally done
        if self._calcs_done:
            print("done?")
            return

        sys.stdout.write("Some job description: ")
        sys.stdout.flush()
        some_list = [0] * 100
        for idx, item in enumerate(some_list):
            msg = "item %i of %i" % (idx, len(some_list)-1)
            wm.progress_update(idx) # close draw progress bar percent real time
            sys.stdout.write(msg + chr(8) * len(msg))
            sys.stdout.flush()
            sleep(0.02)

        sys.stdout.write("DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        self._calcs_done = True

    def modal(self, context, event):
        wm = context.window_manager
        if event.type == 'TIMER' and self._updating == False:
            self._updating = True
            self.do_calcs()
            #self._updating = False
            #print("update????")
            #print(self._updating)
            wm.progress_end() # close draw progress bar when done
        #print(self._calcs_done)
        if self._calcs_done:
            print("time finish!")
            self.cancel(context) #remove this operator context
            return {'CANCELLED'} # this go to cancel function else cancel will loop

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        #wm.progress_begin(0., 100.)
        wm.progress_begin(0, 10000) #100% odd bug #init draw progress bar
        context.window_manager.modal_handler_add(self)
        self._updating = False
        self._timer = context.window_manager.event_timer_add(0.5, window=context.window)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        #context.window_manager.event_timer_remove(self._timer)
        if self._timer == None:#make sure it ingore the 2nd call
            #print("none???")
            return {'CANCELLED'}
        print("operator time remove!")
        context.window_manager.event_timer_remove(self._timer)
        self._timer = None
        #context.window_manager.event_timer_add(0.5, window=context.window)
        return {'CANCELLED'}


class Progress_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Progress"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Objectq", icon='WORLD_DATA')
        row = layout.row()
        row.operator("object.testbtn_operator")


classes = (
    TestBtnOperator,
    Progress_Panel,
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