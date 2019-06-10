# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.context.html?highlight=window#bpy.context.window
# https://docs.blender.org/api/blender2.8/bpy.ops.wm.html?highlight=panel#bpy.ops.wm.call_panel
# 
# https://blenderartists.org/t/override-context-for-operator-called-from-panel/1143240
# 

bl_info = {
    "name": "Custom Navbar",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy

class CustomContextOperator(bpy.types.Operator):
    bl_idname = "object.customcontext_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("navbar")

        screen = context.screen
        override = bpy.context.copy()

        for area in screen.areas:
            #print(area.type)
            if area.type == 'PROPERTIES':
                for region in area.regions:
                    #print(region.type)
                    if region.type == 'WINDOW':
                        override = {'region': region, 'area': area}


        return {'FINISHED'}
		
class CustomButtonOperator(bpy.types.Operator):
    bl_idname = "object.custombutton_operator"
    bl_label = "Hello"

    def execute(self, context):
        print("navbar")
        return {'FINISHED'}
		
class CustomButtonsPanel:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "custom"

class CustomNav_Panel(CustomButtonsPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = ""
    bl_idname = "OBJECT_PT_CustomNav"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'NAVIGATION_BAR'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        #view = context.space_data
        #region = context.region
        #print(region)
        layout.scale_x = 1.4
        layout.scale_y = 1.4
        # https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/UI_API
        #layout.operator('object.customcontext_operator',icon='WORLD_DATA')
        layout.operator('object.customcontext_operator',icon='HEART')

#class Custom_PT_Context(bpy.types.Panel):
class Object_PT_Custom(bpy.types.Panel):
    bl_idname = "OBJECT_PT_Custom"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_label = "Custom Panel"
    #bl_options = {'HIDE_HEADER'}
    #bl_options = {'DEFAULT_CLOSED'}

    #@classmethod
    #def poll(cls, context):
        #return context.scene

    #@classmethod
	#def poll(cls, context):
		#return context.active_object is not None
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        #print(dir(context))

        #print(context.mode)
        #print(context.area.type)
        #print(context.region.type)

        screen = context.screen

        # Update the context 
        #for area in screen.areas:
            #print(area.type)
            #if area.type == 'PROPERTIES':
                #for region in area.regions:
                    #print(region.type)
                    #if region.type == 'WINDOW':
                        #override = {'region': region, 'area': area}


		#layout.operator('object.custombutton_operator',icon='HEART')
        layout.operator('object.custombutton_operator')

        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')
#array
classes = (
	CustomButtonOperator,
    CustomContextOperator,
    CustomNav_Panel,
	Object_PT_Custom,
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
