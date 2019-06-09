#
# https://docs.blender.org/api/blender2.8/bpy.types.Menu.html
# https://docs.blender.org/api/blender2.8/bpy.types.Menu.html
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API
# https://docs.blender.org/api/blender2.8/info_quickstart.html
#
#
#
#
#
# https://blenderartists.org/t/editing-the-menu-bars-without-using-the-python-api/1126562/2
# cycber punk2077 4.16.2020
#


bl_info = {
    "name": "Custom SubMenu",
    "author":"Lightnet",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "View3D",
    "category": "Menu",
}

import bpy

class custom_menu_op(bpy.types.Operator):
    bl_idname = "object.custom_menu_op"
    bl_label = "sub menu"

    def execute(self, context):
        print("Hello World sub")
        return {'FINISHED'}


class customtest_op(bpy.types.Operator):
    bl_idname = "object.custom_menu_op"
    bl_label = "custom test op"

    def execute(self, context):
        print("Hello World sub")
        return {'FINISHED'}

class VIEW3D_MT_custommenu(bpy.types.Menu):
    #bl_idname = "menu.custommenu"
    bl_label = "custommenu"

    def draw(self, context):
        #self.layout.operator("mesh.primitive_monkey_add")
        self.layout.operator("object.custom_menu_op")
        #self.layout.operator("OBJECT_MT_select_test")

def addcustommenu_callback(self, context):	
	self.layout.menu("VIEW3D_MT_custommenu")

class SubMenuTest_OT(bpy.types.Operator):
    bl_idname = "object.submenutest"
    bl_label = "Sub Menu Test"

    def execute(self, context):
        print("Sub Menu Test")
        #scene = context.scene

        #for obj in scene.objects:
            #obj.animation_data_clear()

        return {'FINISHED'}

class BasicSubMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    #bl_label = "Select Test"
    bl_label = "Select Test"

    def draw(self, context):
        layout = self.layout

        #layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        #layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        #layout.operator("object.select_random", text="Random")
        layout.operator("object.select_random", text="Test")

# test call to display immediately.
#bpy.ops.wm.call_menu(name="OBJECT_MT_select_test")

def menu_draw(self, context):
    layout = self.layout
    #self.layout.operator("wm.save_homefile")
    #layout.operator("object.select_random", text="Test Sub")
    layout.menu(CustomMenu.bl_idname)


class CustomMenu(bpy.types.Menu):
    bl_label = "Custom Menu"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.custom_menu_op")
        #layout.operator("wm.open_mainfile")
        #layout.operator("wm.save_as_mainfile").copy = True

def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)


classes = (SubMenuTest_OT, 
    BasicSubMenu, 
    VIEW3D_MT_custommenu,
    custom_menu_op,
    customtest_op,
    CustomMenu
    )

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addcustommenu_callback) #3d viewport menu header
    #bpy.types.VIEW3D_MT_editor_menus.append(draw_item)
    #bpy.types.TOPBAR_MT_file.append(menu_draw)
    bpy.types.TOPBAR_MT_file.append(draw_item)# File Menu Top Left

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addcustommenu_callback)
    #py.types.TOPBAR_MT_file.remove(menu_draw)
    #bpy.types.TOPBAR_MT_file.remove(draw_item)

    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()