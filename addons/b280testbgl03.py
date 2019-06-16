# ===============================================
# 
# Information:
# Testing load screen with bgl but not working. Might need threading.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bgl.html
# https://b3d.interplanety.org/en/active-objects-access/
# https://blender.stackexchange.com/questions/125197/draw-handler-add-and-draw-handler-remove
# https://blender.stackexchange.com/questions/110763/why-doesnt-the-draw-callback-update-with-mousemove?noredirect=1&lq=1
# https://blender.stackexchange.com/questions/125197/draw-handler-add-and-draw-handler-remove
# https://blender.stackexchange.com/questions/61699/how-to-draw-geometry-in-3d-view-window-with-bgl
# https://docs.blender.org/api/blender2.8/info_gotcha.html
# 
bl_info = {
    "name": "custom bgl example 03",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

# import stand alone modules
import blf
import bpy
import sys
from time import sleep
from bpy.props import EnumProperty, CollectionProperty, IntProperty, StringProperty, BoolProperty
import datetime

font_info = {
    "font_id": 0,
    "handler": None,
}

def draw_callback_px(self, context):
    """Draw on the viewports"""
    scene = context.scene
    # BLF drawing routine
    font_id = font_info["font_id"]
    blf.position(font_id, 2, 80, 0)
    blf.size(font_id, 50, 72)
    #if bpy.data.scenes[0].helloname != None:
        #blf.draw(font_id, "Hello World" + bpy.data.scenes[0].helloname)
    if scene.helloname != None:
        blf.draw(font_id, "Hello World Time:" + scene.helloname)
    else:
        blf.draw(font_id, "Hello World")

class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modal_operator"
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
        bpy.data.scenes[0].helloname = now.strftime("%H:%M:%S")

        # Add the region OpenGL drawing callback
        # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
        if not self._handle:
            args = (self, context)
            self._handle = bpy.types.SpaceView3D.draw_handler_add(
            draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

        if event.type in {'ESC'}:
            #bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            #bpy.context.area.tag_redraw()
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
        #bpy.context.area.tag_redraw()
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        self._timer = None
        #bpy.context.area.tag_redraw()
        #context.window_manager.event_timer_add(0.5, window=context.window)
        print("operator time remove!")
        return {'CANCELLED'}

class TestBGL_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Progress"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = "object"
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="bgl Panel", icon='WORLD_DATA')
        col.operator("view3d.modal_operator")

classes = (
    TestBGL_Panel,
    ModalDrawOperator,
)

def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.helloname = StringProperty()
    
def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
    #addscreen()