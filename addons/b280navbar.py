# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.context.html?highlight=window#bpy.context.window
# https://docs.blender.org/api/blender2.8/bpy.ops.wm.html?highlight=panel#bpy.ops.wm.call_panel
# https://blenderartists.org/t/override-context-for-operator-called-from-panel/1143240
# 
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
        #override = bpy.context.copy()

        #bpy.ops.wm.call_panel('INVOKE_DEFAULT',name="OBJECT_PT_Custom")
        bpy.ops.wm.call_panel('INVOKE_DEFAULT',name=CUSTOM_PT_context_custom.bl_idname)
        

        """
        for area in screen.areas:
            #print(area.type)
            if area.type == 'PROPERTIES':
                for region in area.regions:
                    #print(region.type)
                    if region.type == 'WINDOW':
                        override = {'region': region, 'area': area}
        """
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
    """Creates a Tab Navigation Bar in the Object properties window"""
    bl_label = ""
    bl_idname = "OBJECT_PT_CustomNav"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'NAVIGATION_BAR'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        layout.scale_x = 1.4
        layout.scale_y = 1.4
        # https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/UI_API
        #layout.operator('object.customcontext_operator',icon='WORLD_DATA')
        layout.operator('object.customcontext_operator',icon='HEART')

#Custom Panel
class CUSTOM_PT_context_custom(CustomButtonsPanel,bpy.types.Panel):
    bl_idname = "CUSTOM_PT_context_custom"
    bl_label = ""
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_label = "Custom Panel"
    
    #bl_options = {'HIDE_HEADER'}
    #bl_options = {'DEFAULT_CLOSED'}
    #@classmethod
    #def poll(cls, context):
        #return context.scene
    #@classmethod
	#def poll(cls, context):
		#return context.active_object is not None
    @classmethod
    def poll(cls, context):
        print(dir(context))
        #print(context.space_data.type)
        #print(context.space_data.bl_rna)
        #print(context.space_data.show_region_header)
        #print(dir(context.space_data))
        #print(context.space_data.tree_type)
        return context.scene
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        #print(dir(context))
		#layout.operator('object.custombutton_operator',icon='HEART')
        row = layout.row()
        row.label(text="Hello", icon='WORLD_DATA')
        layout.operator('object.custombutton_operator')

#array
classes = (
	CustomButtonOperator,
    CustomContextOperator,
    CustomNav_Panel,
	CUSTOM_PT_context_custom,
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
