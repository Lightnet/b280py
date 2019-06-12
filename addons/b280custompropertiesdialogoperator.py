# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Finish
# 
# ===============================================
# https://docs.blender.org/api/blender2.8/bpy.types.Operator.html
# 

bl_info = {
    "name": "Custom Properties Dialog operator",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy

#bpy.props.IntProperty()
#bpy.props.StringProperty()
#bpy.props.FloatProperty()
#
#bpy.types.Scene.testprop = bpy.props.FloatProperty(update=update_func)
#bpy.types.Scene.customnameprop = bpy.props.StringProperty()
#print(bpy.context.scene.testprop)
#print(bpy.types.Scene.customnameprop)#not right
#print(bpy.context.scene.customnameprop)#right var

# Assign a custom property to an existing type.
#bpy.types.Material.custom_float = bpy.props.FloatProperty(name="Test Property")

# Test the property is there.
#bpy.data.materials[0].custom_float = 5.0

bpy.types.Scene.Ecustom_bool = bpy.props.BoolProperty(name="My Bool", default=False)
bpy.types.Scene.Ecustom_string = bpy.props.StringProperty(name="My String", default="hello")
bpy.types.Scene.Ecustom_float = bpy.props.FloatProperty(name="My Float", default=10)
bpy.types.Scene.Ecustom_int = bpy.props.IntProperty(name="My Int", default=1)

bpy.types.Scene.Ecustom_boolvector = bpy.props.BoolVectorProperty(name="boolvector", default=(False, False, False))
bpy.types.Scene.Ecustom_floatvector = bpy.props.FloatVectorProperty(name="floatvector", default=(0.1, 0.0, 1.0))
bpy.types.Scene.Ecustom_intvector = bpy.props.IntVectorProperty(name="intvector", default=(-1, 0, 1))

#bpy.types.Scene.Ecustom_pointer = bpy.props.PointerProperty(name="pointer")

# bpy.props.CollectionProperty
# bpy.props.EnumProperty

class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Minimal Operator"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

class HDOperator(bpy.types.Operator):
    bl_idname = "wm.hw"
    bl_label = "open test Operator"

    def execute(self, context):
        print("Hello World")
        bpy.ops.object.property_example('INVOKE_DEFAULT')
        return {'FINISHED'}

class OBJECT_OT_property_example(bpy.types.Operator):
    bl_idname = "object.property_example"
    bl_label = "Property Example"
    bl_options = {'REGISTER', 'UNDO'}

    my_float: bpy.props.FloatProperty(name="Some Floating Point")
    my_bool: bpy.props.BoolProperty(name="Toggle Option")
    my_string: bpy.props.StringProperty(name="String Value")

    # draw props
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "my_bool", text="my_bool")
        layout.prop(self, "my_float", text="my_float")
        layout.prop(self, "my_string", text="my_string")

    def execute(self, context):
        self.report(
            {'INFO'}, 'F: %.2f  B: %s  S: %r' %
            (self.my_float, self.my_bool, self.my_string)
        )
        print('My float:', self.my_float)
        print('My bool:', self.my_bool)
        print('My string:', self.my_string)
        return {'FINISHED'}
    #diplay window    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class CustomProps_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Props Panel"
    bl_idname = "OBJECT_PT_CustomProps"

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #my_string = bpy.props.StringProperty(name="String Value",default="Unknown")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        #row = layout.row()
        #row.label(text="Custom Props.", icon='WORLD_DATA')
        #row = layout.row()
        #row.operator('wm.hello_world')
        #row = layout.row()
        #row.operator('wm.hw')
        #props = self.layout.operator('object.property_example')
        #props.my_bool = True
        #props.my_string = "Shouldn't that be 47?"
        #layout.prop(props, "my_bool", text="ops my_bool") # can't be edit
        #layout.prop(props, "my_float", text="ops my_float") # can't be edit
        #layout.prop(props, "my_string", text="ops my_string") # can't be edit

        layout.prop(scene, "Ecustom_bool", text="boolean Property")
        layout.prop(scene, "Ecustom_string", text="string Property")
        layout.prop(scene, "Ecustom_float", text="float Property")
        layout.prop(scene, "Ecustom_int", text="int Property")

        layout.prop(scene, "Ecustom_boolvector", text="boolvector Property")
        layout.prop(scene, "Ecustom_floatvector", text="floatvector Property")
        layout.prop(scene, "Ecustom_intvector", text="intvector Property")
        #layout.prop(scene, "Ecustom_pointer", text="pointer Property")

        # You can set properties dynamically:
        #if context.object:
            #props.my_float = context.object.location.x
        #else:
            #props.my_float = 327

classes = (
    CustomProps_Panel,
    HelloWorldOperator,
    HDOperator,
    OBJECT_OT_property_example,
)
register, unregister = bpy.utils.register_classes_factory(classes)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()