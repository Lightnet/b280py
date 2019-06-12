# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.props.html?highlight=bpy%20props%20intproperty
# https://docs.blender.org/api/blender2.8/bpy.props.html
#

bl_info = {
    "name": "Custom Properties Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy

#note this will save in filename.blend but the variable not be same name else conflict (not yet tested read some where)
bpy.types.Scene.Ecustom_bool = bpy.props.BoolProperty(name="My Bool", default=False)
bpy.types.Scene.Ecustom_string = bpy.props.StringProperty(name="My String", default="hello")
bpy.types.Scene.Ecustom_float = bpy.props.FloatProperty(name="My Float", default=10)
bpy.types.Scene.Ecustom_int = bpy.props.IntProperty(name="My Int", default=1)

bpy.types.Scene.Ecustom_boolvector = bpy.props.BoolVectorProperty(name="boolvector", default=(False, False, False))
bpy.types.Scene.Ecustom_floatvector = bpy.props.FloatVectorProperty(name="floatvector", default=(0.1, 0.0, 1.0))
bpy.types.Scene.Ecustom_intvector = bpy.props.IntVectorProperty(name="intvector", default=(-1, 0, 1))

#bpy.props.PointerProperty(name="pointer")# does not work
#bpy.props.CollectionProperty()
#bpy.props.EnumProperty()

class CustomProps_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Props Panel"
    bl_idname = "OBJECT_PT_CustomProps"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        row = layout.row()
        row.label(text="Custom Tool All.", icon='WORLD_DATA')

        layout.prop(scene, "Ecustom_bool", text="boolean Property")
        layout.prop(scene, "Ecustom_string", text="string Property")
        layout.prop(scene, "Ecustom_float", text="float Property")
        layout.prop(scene, "Ecustom_int", text="int Property")

        layout.prop(scene, "Ecustom_boolvector", text="boolvector Property")
        layout.prop(scene, "Ecustom_floatvector", text="floatvector Property")
        layout.prop(scene, "Ecustom_intvector", text="intvector Property")
        #layout.prop(scene, "Ecustom_pointer", text="pointer Property")

classes = (
    CustomProps_Panel,
)
register, unregister = bpy.utils.register_classes_factory(classes)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()