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
import bmesh

class ObjectQ_Operator(bpy.types.Operator):
    bl_idname = "object.objectq_operator"
    bl_label = "object test"

    def execute(self, context):
        print("Hello World")
        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}
# http://wiki.theprovingground.org/blender-py-mathmesh
# https://docs.blender.org/api/blender2.8/bmesh.html
# https://blender.stackexchange.com/questions/95408/how-do-i-create-a-new-object-using-python-in-blender-2-80
# https://docs.blender.org/api/blender2.8/bpy.types.Object.html
# https://blender.stackexchange.com/questions/132825/python-selecting-object-by-name-in-2-8/124628
# https://blender.stackexchange.com/questions/61879/create-mesh-then-add-vertices-to-it-in-python/61893
# https://devtalk.blender.org/t/selecting-an-object-in-2-8/4177
# https://developer.blender.org/T57366
# https://docs.blender.org/api/blender2.8/bmesh.ops.html
# https://blender.stackexchange.com/questions/101216/how-to-use-loops-foreach-set-and-polygons-foreach-set-to-add-faces-to-a-mesh
#
# bmesh.types.BMVert
# bmesh.types.BMEdge
#
# https://blender.stackexchange.com/questions/56385/python-edit-panel-to-edit-custom-bmesh-face-layers

class ObjectCM_Operator(bpy.types.Operator):
    bl_idname = "object.objectcm_operator"
    bl_label = "mesh create"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        print("create mesh")
        scene = context.scene

        verts = [(2.0, 2.0, 2.0), (-2.0, 2.0, 2.0),(-2.0, -2.0, 2.0)]  # 2 verts made with XYZ coords
        edges = []
        #edges = [(0, 1), (1, 2), (2, 0)]
        faces = []
        faces = [(0, 1, 2)]

        mesh = bpy.data.meshes.new('emptyMesh')
        obj = bpy.data.objects.new("object_name", mesh)
        #scene.objects.link(obj)  # put the object into the scene (link)
        for o in bpy.context.collection.objects:
            #print(o)
            o.select_set(False) 
        bpy.context.collection.objects.link(obj)

        #scene.object.active = obj  # set as the active object in the scene
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)  # select object
        #print(dir(scene.objects))
        #print(scene.objects.active )
        # convert the current mesh to a bmesh (must be in edit mode)
        #mesh = bpy.context.object.data
        #bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.object.mode_set('SELECT')
        bm = bmesh.new()
        #print(dir(bm))
        for v in verts:
            bm.verts.new(v)  # add a new vert
            pass
        for e in edges:
            #print(e)
            #bm.edges.new(e)
            pass

        for f in faces:
            #print(f)
            #bm.faces.new(f)
            #bm.faces.append(f)
            pass

        vert1 = bm.verts.new(verts[0])
        vert2 = bm.verts.new(verts[1])
        vert3 = bm.verts.new(verts[2])
        bm.verts.ensure_lookup_table() #update array index
        #face = bm.faces.new((vert1, vert2, vert3))
        print("=============")
        #for i in bm.verts:
            #print(i)
        #print("=====")
        #print(bm.verts[0])
        for f in faces:
            #print(bm.verts[f[0]])
            bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
            pass



        #bm.tessfaces.add(len(faces))
        #bm.faces.new(faces)
        #print(isinstance(faces[0], bmesh.types.BMVert))

        #f = bm.faces.new()
        #print(f)
        #create mesh from python data
        #mesh.from_pydata(verts,edges,faces)
        mesh.update()
        

        # make the bmesh the object's mesh
        bm.to_mesh(mesh)  
        bm.free()  # always do this when finished
        bpy.ops.object.mode_set(mode='OBJECT')  # return to object mode

        #mesh = bpy.context.object.data
        #bm = bmesh.new()
        # convert the current mesh to a bmesh (must be in edit mode)
        #bpy.ops.object.mode_set(mode='EDIT')
        #bm.from_mesh(mesh)
        #bpy.ops.object.mode_set(mode='OBJECT')  # return to object mode

        #for v in verts:
            #bm.verts.new(v)  # add a new vert

        # make the bmesh the object's mesh
        #bm.to_mesh(mesh) 
        #bm.free()  # always do this when finished

        #bpy.context.collection.objects.link(theObj)

        #scene.update()
        #print(dir(scene))
        #self.report({'WARNING', 'INFO'}, "mesh create!")
        print("finish")

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


# https://blenderartists.org/t/how-to-build-an-armature-in-2-5x-from-xml-data/507619/3
# https://blender.stackexchange.com/questions/51684/python-create-custom-armature-without-ops
class ObjectCA_Operator(bpy.types.Operator):
    bl_idname = "object.objectca_operator"
    bl_label = "armture create"

    def execute(self, context):

        # create the armature object
        armdata = bpy.data.armatures.new("skeleton")
        objarm = bpy.data.objects.new("skeleton", armdata)

        bpy.context.collection.objects.link(objarm)
        #scene.object.active = obj  # set as the active object in the scene
        bpy.context.view_layer.objects.active = objarm
        objarm.select_set(True)  # select object

        # set to edit mode
        bpy.ops.object.mode_set(mode='EDIT')

        edit_bones = objarm.data.edit_bones

        b = edit_bones.new('bone1')
        # a new bone will have zero length and not be kept
        # move the head/tail to keep the bone
        b.head = (1.0, 1.0, 0.0)
        b.tail = (1.0, 1.0, 1.0)

        b2 = edit_bones.new('bone2')
        b2.head = (1.0, 2.0, 0.0)
        b2.tail = (1.0, 2.0, 1.0)

        # parent bone2 to bone1
        b2.parent = objarm.data.edit_bones["bone1"] 

        # exit edit mode to save bones so they can be used in pose mode
        bpy.ops.object.mode_set(mode='OBJECT')

        print("created armature")

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

        col = layout.column()
        col.operator("object.objectq_operator")
        col.operator("object.objectcm_operator")
        col.operator("object.objectm_operator")
        col.operator("object.objecta_operator")
        col.operator("object.objectca_operator")

classes = (
    ObjectQ_Operator,
    ObjectM_Operator,
    ObjectCM_Operator,
    ObjectCA_Operator,
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