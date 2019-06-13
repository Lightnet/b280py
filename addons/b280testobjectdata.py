# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# bpy.context.scene.update()
# 


bl_info = {
    "name": "Custom Objectq Panel",
    "author":"none",
    "version":(0,0,1),
    "blender": (2,80,0),
    "location": "PROPERTIES",
    "category": "Object"
}

import bpy

class ObjectQ_Operator(bpy.types.Operator):
    bl_idname = "object.objectq_operator"
    bl_label = "object test"

    def execute(self, context):
        print("Hello World")
        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}


# https://blender.stackexchange.com/questions/125114/how-to-get-the-class-of-selected-object-in-blender-2-8
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API
# https://docs.blender.org/api/blender2.8/bmesh.ops.html
# https://docs.blender.org/api/blender_python_api_current/bpy.types.Mesh.html

# https://blender.stackexchange.com/questions/1311/how-can-i-get-vertex-positions-from-a-mesh

class ObjectM_Operator(bpy.types.Operator):
    bl_idname = "object.objectm_operator"
    bl_label = "mesh raw"

    def execute(self, context):
        scene = context.scene

        objectType = bpy.context.object.type
        print(objectType)
        ob = bpy.context.object
        if objectType == "MESH":
            print(dir(ob))
            me = bpy.context.object.data
            print(me)
            uv_layer = me.uv_layers.active.data
            for poly in me.polygons:
                print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))

                # range is used here to show how the polygons reference loops,
                # for convenience 'poly.loop_indices' can be used instead.
                for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
                    print("    Vertex: %d" % me.loops[loop_index].vertex_index)
                    print("    UV: %r" % uv_layer[loop_index].uv)


        print("Hello World")
        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}

# https://docs.blender.org/api/blender2.8/info_gotcha.html
# https://docs.blender.org/api/blender2.8/info_gotcha.html#editbones-posebones-bone-bones
#
# To edit bone is to object edit mode. Not pose or object mode.
# bpy.context.active_pose_bone #pose mode
# bpy.context.active_bone
# bpy.context.selected_editable_bones #edit bone
# 
# 
# 
class ObjectA_Operator(bpy.types.Operator):
    bl_idname = "object.objecta_operator"
    bl_label = "armture raw"

    def execute(self, context):
        print("Hello World")

        objectType = bpy.context.object.type
        print(objectType)
        ob = bpy.context.object
        if objectType == "ARMATURE":
            #print(dir(ob))
            armdata = bpy.context.object.data
            bones = bpy.context.object.data.bones
            for bone in bones:
                print(bone.name)










        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}

class Objectq_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Objectq Panel"
    bl_idname = "OBJECT_PT_Objectq"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Objectq", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("object.objectq_operator")
        row = layout.row()
        row.operator("object.objectm_operator")
        row = layout.row()
        row.operator("object.objecta_operator")

classes = (
    ObjectQ_Operator,
    ObjectM_Operator,
    ObjectA_Operator,
    Objectq_Panel
)

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