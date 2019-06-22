# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: 
# 
# ===============================================

bl_info = {
    "name": "custom gpu blf progress 01",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

# https://www.youtube.com/watch?v=EgrgEoNFNsA
# https://docs.blender.org/api/blender2.8/gpu.html

import bpy
from bpy.props import EnumProperty, CollectionProperty, IntProperty, StringProperty, BoolProperty

import gpu
import blf
import sys
import datetime
from time import sleep
from gpu_extras.batch import batch_for_shader
import time
import threading


font_info = {
    "font_id": 0,
    "handler": None,
}

vertices = (
    (100, 100), (300, 100),
    (100, 200), (300, 200))

indices = (
    (0, 1, 2), (2, 1, 3))

shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'TRIS', {"pos": vertices}, indices=indices)

def draw():
    shader.bind()
    shader.uniform_float("color", (0, 0.5, 0.5, 1.0))
    batch.draw(shader)

def draw_callback_px(self, context):
    """Draw on the viewports"""
    scene = context.scene
    draw()
    font_id = font_info["font_id"]
    blf.position(font_id, 2, 80, 0)
    blf.size(font_id, 50, 72)
    if scene.customprogressbars != None:
        blf.draw(font_id, "Progress " + scene.customprogressbars + "%")
    else:
        blf.draw(font_id, "Progress 0%")

# https://docs.blender.org/api/blender2.8/bpy.app.timers.html?highlight=thread
# https://docs.blender.org/api/blender_python_api_current/bpy.types.Operator.html
# https://docs.blender.org/api/blender2.8/bpy.types.Operator.html
class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modaldraw_operator"
    bl_label = "Simple Modal View3D Operator"
    bl_options = {'REGISTER', 'INTERNAL'}

    _handle = None
    _timer = None
    _updating = False
    _calcs_done = False

    def __del__(self):
        #context.window_manager.event_timer_remove(self._timer)
        if self._handle != None:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        print("End")

    def do_calcs(self):
        wm = bpy.context.window_manager
        # would be good if you can break up your calcs
        # so when looping over a list, you could do batches
        # of 10 or so by slicing through it.
        # do your calcs here and when finally done

        sys.stdout.write("Some job description: ")
        sys.stdout.flush()
        some_list = [0] * 100
        for idx, item in enumerate(some_list):
            msg = "item %i of %i" % (idx, len(some_list)-1)
            #note if thread is run it will render text progress
            wm.progress_update(idx) # close draw progress bar percent real time
            bpy.data.scenes[0].customprogressbars = str(idx)
            sys.stdout.write(msg + chr(8) * len(msg))
            sys.stdout.flush()
            sleep(0.02)

        sys.stdout.write("DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        self._calcs_done = True

    def modal(self, context, event):
        wm = bpy.context.window_manager
        #print(context.area.type)
        #context.area.tag_redraw()
        bpy.context.area.tag_redraw()
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw() #bgl redraw in VIEW_3D
                break

        #now = datetime.datetime.now()
        #print("update? "  + now.strftime("%H:%M:%S"))
        #bpy.data.scenes[0].customprogressbars = now.strftime("%H:%M:%S")

        if event.type == 'TIMER' and self._updating == False:#do once
            self._updating = True
            #self.do_calcs()
            build = threading.Thread(target=self.do_calcs)
            build.start()

        if event.type == 'TIMER':
            try:
                pp = float(context.scene.customprogressbars)
                wm.progress_update(pp)
            except ValueError:
                #print("Not a float")
                pass
            
        if self._calcs_done:#check if calcs is done
            print("time finish!")
            wm.progress_end()
            self.cancel(context) #remove this operator context
            return {'FINISHED'}

        if event.type in {'ESC'}:
            wm.progress_end()
            self.cancel(context) 
            print("finish remove draw")
            return {'CANCELLED'}

        #print("update...")
        #return {'PASS_THROUGH'}
        return {'RUNNING_MODAL'} 
# https://docs.blender.org/api/blender2.8/bpy.types.Operator.html

    def invoke(self, context, event):
        #print(context.area.type )
        args = (self, context)
        wm = context.window_manager
        wm.progress_begin(0, 10000)
        # the arguments we pass the the callback
        wm.modal_handler_add(self)
        self._timer = wm.event_timer_add(0.1, window=context.window)
        # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
        self._handle = bpy.types.SpaceView3D.draw_handler_add(
            draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
        return {'RUNNING_MODAL'}

    def finish(self):
        context.window_manager.event_timer_remove(self._timer)
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        print("finish")
        return {"FINISHED"}

    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        self._timer = None
        print("operator time remove!")
        return {'CANCELLED'}

classes = (
    ModalDrawOperator,
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
    kmi = km.keymap_items.new("view3d.modaldraw_operator", 'F', 'PRESS',alt=False, ctrl=False, shift=True)
    #kmi = km.keymap_items.new(WorkMacro.bl_idname, 'E', 'PRESS', alt=False, ctrl=False, shift=False)
    #kmi = km.keymap_items.new("OBJECT_MT_pie_template", 'E', 'PRESS', alt=False, ctrl=False, shift=False)
    #kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS')
    #kmi.properties.name = "OBJECT_MT_pie_template"
    addon_keymaps.append(km)

    bpy.types.Scene.customprogressbars = StringProperty()

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