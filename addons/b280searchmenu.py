

# https://blender.stackexchange.com/questions/8699/what-ui-would-work-for-choosing-from-a-long-long-list

bl_info = {
    "name": "Base",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "none",
    "category": "none",
    "warning": "",
    "wiki_url": "",
}

import bpy

def item_cb(self, context):
    return [(str(i), "Item %i" % i, "") for i in range(100)]


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    bl_property = "my_enum"

    my_enum : bpy.props.EnumProperty(items=item_cb)

    def execute(self, context):
        self.report({'INFO'}, "Selected: %s" % self.my_enum)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator('INVOKE_DEFAULT')