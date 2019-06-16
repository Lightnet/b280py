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
# 
bl_info = {
    "name": "custom bgl example 02",
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
        blf.draw(font_id, "Hello World" + scene.helloname)
    else:
        blf.draw(font_id, "Hello World")

class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Simple Modal View3D Operator"
    bl_options = {'REGISTER', 'INTERNAL'}

    _handle = None
    _calcs_done = False
    _time = 0
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
        area = None
        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':
                area = a
                #a.tag_redraw()
                break

        sys.stdout.write("Some job description: ")
        sys.stdout.flush()
        some_list = [0] * 100
        for idx, item in enumerate(some_list):
            msg = "item %i of %i" % (idx, len(some_list)-1)
            wm.progress_update(idx) # close draw progress bar percent real time
            #area.tag_redraw()

            for a in bpy.context.screen.areas:
                if a.type == 'VIEW_3D':
                    #area = a
                    a.tag_redraw()
                    break

            sys.stdout.write(msg + chr(8) * len(msg))
            sys.stdout.flush()
            sleep(0.02)

        sys.stdout.write("DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        self._calcs_done = True

    def modal(self, context, event):
        #print(context.area.type)
        #context.area.tag_redraw()
        #bpy.context.area.tag_redraw()
        for a in context.screen.areas:
            if a.type == 'VIEW_3D':
                a.tag_redraw()
                break
        
        self._time = self._time + 1
        print("update?"+str(self._time))
        bpy.data.scenes[0].helloname = str(self._time)


        # Add the region OpenGL drawing callback
        # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
        if not self._handle:
            args = (self, context)
            self._handle = bpy.types.SpaceView3D.draw_handler_add(
            draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
        if event.type == 'TIMER' and self._updating == False:
            self._updating = True
            self.do_calcs()

        if event.type in {'ESC'}:
            #bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            bpy.context.area.tag_redraw()
            self.cancel(context) 
            print("finish remove draw")
            return {'CANCELLED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        # the arguments we pass the the callback
        context.window_manager.modal_handler_add(self)
        wm = context.window_manager
        wm.progress_begin(0, 10000) #100% odd bug #init draw progress bar
        self._updating = False
        self._timer = context.window_manager.event_timer_add(0.1, window=context.window)
        
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        #context.window_manager.event_timer_remove(self._timer)
        #if self._timer == None:#make sure it ingore the 2nd call
            #print("none???")
            #return {'CANCELLED'}
        print("operator time remove!")
        context.window_manager.event_timer_remove(self._timer)
        self._timer = None
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        bpy.context.area.tag_redraw()
        #context.window_manager.event_timer_add(0.5, window=context.window)
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
    if font_info["handler"] != None:
        bpy.types.SpaceView3D.draw_handler_remove(font_info["handler"],'WINDOW')

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
    #addscreen()