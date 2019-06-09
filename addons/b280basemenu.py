bl_info = {
    "name": "Base Menu",
    "author":"Lightnet",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Object",
    "description":"testing menu"
}

import bpy

class HelloOperator(bpy.types.Operator):
    bl_idname = "object.hello_operator"
    bl_label = "Hello Operator"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

class HTOperator(bpy.types.Operator):
    bl_idname = "object.ht_operator"
    bl_label = "HT Operator"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

#[PROPERTIES] display tool tab in panel sub PROPERTIES
class HelloTool_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "HelloTool Panel"
    bl_idname = "OBJECT_PT_HelloTool"
    #bl_category = "Test Addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator("object.ht_operator")
        #print(context.mode) #edit, object

# [PROPERTIES] display navbar in all section in sub PROPERTIES
class HelloII_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "HelloII Panel"
    bl_idname = "OBJECT_PT_HelloII"
    #bl_category = "Test Addon"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator("object.ht_operator")
        #print(context.mode) #edit, object

class Hello_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello Panel"
    bl_idname = "OBJECT_PT_Hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')

        #row = layout.row()
        #row.label(text="Active object is: " + obj.name)
        #row = layout.row()
        #row.prop(obj, "name")

        row = layout.row()
        row.operator("object.hello_operator")

#array
classes = (Hello_Panel, HelloOperator, HelloII_Panel, HTOperator,HelloTool_Panel)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback)  
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback) 
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()