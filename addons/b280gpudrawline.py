# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: 
# 
# ===============================================

bl_info = {
    "name": "custom gpu draw line",
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
import gpu
import blf
#import time
import datetime
from gpu_extras.batch import batch_for_shader

font_info = {
    "font_id": 0,
    "handler": None,
}

coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'LINES', {"pos": coords})

def draw_callback_px(self, context):
    """Draw on the viewports"""
    """
    scene = context.scene
    # BLF drawing routine
    font_id = font_info["font_id"]
    blf.position(font_id, 2, 80, 0)
    blf.size(font_id, 50, 72)
    #if bpy.data.scenes[0].helloname != None:
        #blf.draw(font_id, "Hello World" + bpy.data.scenes[0].helloname)
    #if scene.helloname != None:
        #blf.draw(font_id, "Hello World" + scene.helloname)
    #else:
        #blf.draw(font_id, "Hello World")
    blf.draw(font_id, "Hello World")
    """

    shader.bind()
    shader.uniform_float("color", (1, 1, 0, 1))
    batch.draw(shader)



class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modaldraw_operator"
    bl_label = "Simple Modal View3D Operator"
    bl_options = {'REGISTER', 'INTERNAL'}

    _handle = None
    _timer = None

    def modal(self, context, event):
        #print(context.area.type)
        #context.area.tag_redraw()
        #bpy.context.area.tag_redraw()
        for a in context.screen.areas:
            if a.type == 'VIEW_3D':
                a.tag_redraw() #bgl redraw in VIEW_3D
                break

        now = datetime.datetime.now()
        #print("update? "  + now.strftime("%H:%M:%S"))
        #bpy.data.scenes[0].helloname = now.strftime("%H:%M:%S")

        # Add the region OpenGL drawing callback
        # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
        if not self._handle:
            args = (self, context)
            #self._handle = bpy.types.SpaceView3D.draw_handler_add(
            #draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self._handle = bpy.types.SpaceView3D.draw_handler_add(
            draw_callback_px, args, 'WINDOW', 'POST_VIEW')

        if event.type in {'ESC'}:
            self.cancel(context) 
            print("finish remove draw")
            return {'CANCELLED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        print(context.area.type )
        # the arguments we pass the the callback
        context.window_manager.modal_handler_add(self)
        wm = context.window_manager
        self._timer = context.window_manager.event_timer_add(0.1, window=context.window)
        return {'RUNNING_MODAL'}

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