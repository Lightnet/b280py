# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# 

# 
# 

bl_info = {
    "name": "Custom Tools",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
}

import bpy

class VIEW3D_MT_menu(bpy.types.Menu):
    bl_label = "Test"

    def draw(self, context):
        self.layout.operator("mesh.primitive_monkey_add")
        self.layout.operator("object.simple_operator")

def addmenu_callback(self, context):	
	self.layout.menu("VIEW3D_MT_menu")

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}
#bpy.ops.wm.call_menu(name="object.simple_operator")

class ClearAnimationData(bpy.types.Operator):
    bl_idname = "object.clear_animation_data"
    bl_label = "Clear Animation Data"

    def execute(self, context):
        print("Hello World")
        #print(dir(context))
        scene = context.scene

        for obj in scene.objects:
            obj.animation_data_clear()
            #print(obj)
            #print(dir(obj))
        #for obj in scene.objects:
            #obj.location.x += 1.0
        #myObjects = bpy.data.objects
        #print(list(myObjects))

        return {'FINISHED'}

class BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")
#bpy.ops.wm.call_menu(name="OBJECT_MT_select_test")

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")

        row = layout.row()
        row.operator("object.clear_animation_data")

classes = (
    SimpleOperator,
    BasicMenu,
    HelloWorldPanel, 
    VIEW3D_MT_menu, 
    ClearAnimationData
)

def register():
    #print("Hello World")
    bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback)
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()