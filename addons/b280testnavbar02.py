# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
#
# https://docs.blender.org/api/blender2.8/bpy.context.html?highlight=window#bpy.context.window
# https://docs.blender.org/api/blender2.8/bpy.ops.wm.html?highlight=panel#bpy.ops.wm.call_panel
# https://blenderartists.org/t/override-context-for-operator-called-from-panel/1143240
#
# https://blender.stackexchange.com/questions/97647/how-to-access-properties-of-the-3d-viewport
# https://blenderartists.org/t/windows-areas-and-screens-with-python/607275/4


bl_info = {
    "name": "Custom NavbarTab",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "PROPERTIES",
    "category": "Custom",
    "warning": "",
    "wiki_url": "",
}

import bpy

# run panel command
class CustomContextOperator(bpy.types.Operator):
    bl_idname = "object.customcontext_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("navbar")
        #bpy.ops.screen.workspace_cycle(direction='NEXT')
        #print(dir(bpy.context.space_data))
        #print(bpy.context.space_data.bl_rna)
        #print(bpy.context.space_data.show_region_header)
        #print(bpy.context.space_data.type)
        #'TOOL', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'SCENE', 'WORLD', 'OBJECT', 'MODIFIER', 'PARTICLES', 'PHYSICS', 'CONSTRAINT', 'DATA', 'MATERIAL', 'TEXTURE'
        bpy.context.space_data.context = 'TOOL' 
        #bpy.context.space_data.context = 'EMPTY' #does not work
        #bpy.context.space_data.context = 'Custom' #does not work
        return {'FINISHED'}

# 
class CustomButtonOperator(bpy.types.Operator):
    bl_idname = "object.custombutton_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("navbar")

        window = bpy.context.window
        screen = bpy.context.screen
        scene = bpy.context.scene
        print("------")
        for area in screen.areas:
            print(area.type)
            #if area.type == "VIEW_3D":
                #break



        #bpy.context.area.ui_type =""
        #bpy.context.area.ui_type = 'NLA_EDITOR'
        return {'FINISHED'}
		
class CustomButtonsPanel:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "custom"

#NavBarTab
class CustomNavBarTab_Panel(CustomButtonsPanel, bpy.types.Panel):
    bl_label = ""
    bl_idname = "OBJECT_PT_CustomNavBarTab"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'NAVIGATION_BAR'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        #view = context.space_data
        layout.scale_x = 1.4
        layout.scale_y = 1.4
        # https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/UI_API
        #layout.operator('object.customcontext_operator',icon='WORLD_DATA')
        layout.operator('object.customcontext_operator',icon='HEART')

#Context
class Custom_Context(bpy.types.Panel):
    bl_idname = "OBJECT_PT_Custom"
    bl_label = "Custom Context"
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_context = "tools"

    #work tool tab left VIEW_3D
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'

    #display in active tool workspace settings in properties
    #display in view3d on right under tool tab group
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'UI'
    #bl_category = "Tool"

    #display custom tab in view3d on right under tool tab
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'UI'
    #bl_category = "custom"

    #nope
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW' # fail(TOOL_HEADER TOOLS TOOL_PROPS UI TOOL_HEADER FOOTER) pass( HEADER,NAVIGATION_BAR  )
    #bl_category = "Tools"
    #bl_context = "tool"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    #bl_context = "mystuff"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')

		#row.operator('object.custombutton_operator',icon='HEART')
        row = layout.row()
        row.operator('object.custombutton_operator')

        

classes = (
	CustomButtonOperator,
    CustomContextOperator,
    CustomNavBarTab_Panel,
	Custom_Context,
)

def register():
    #print("Hello World")
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #print("Goodbye World")
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
