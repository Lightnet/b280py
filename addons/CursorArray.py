
# https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# https://blender.stackexchange.com/questions/5359/how-to-set-cursor-location-pivot-point-in-script
# https://devtalk.blender.org/t/cursor-location-as-scene-attribute/6110
# https://blender.stackexchange.com/questions/126577/blender-2-8-api-python-set-active-object
# not yet finish

bl_info = {
    "name": "Cursor Array",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "menu",
}

import bpy

class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    #bl_options = {'REGISTER', 'UNDO'}

    total : bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    def execute(self, context):
        scene = context.scene
        cursor = context.scene.cursor.location
        #print(context.scene.cursor.location)
        obj = bpy.context.active_object

        #for i in range(self.total):
            #obj_new = obj.copy()
            #scene.objects.link(obj_new)
            #factor = i / self.total
            #obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

class BasicViewportMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_viewportmenu"
    bl_label = "custom menu"

    def draw(self, context):
        layout = self.layout
        #layout.operator("object.select_random", text="Random")
        #layout.operator("object.helloviewport_operator", text="Random")
        layout.operator(ObjectCursorArray.bl_idname)

def menu_func(self, context):
    #self.layout.menu("OBJECT_MT_viewportmenu")
    self.layout.operator(ObjectCursorArray.bl_idname)

classes = (
    ObjectCursorArray,
    BasicViewportMenu
)

def register():
    bpy.types.VIEW3D_MT_object.append(menu_func)
    #bpy.types.VIEW3D_MT_editor_menus.append(menu_func)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    #bpy.types.VIEW3D_MT_editor_menus.remove(menu_func)
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()