# ===============================================
# 
# Information:
# Simple format for blender plugin add on.
# Status: Prototyping build
# 
# ===============================================
# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API
# https://docs.blender.org/api/blender2.8/bmesh.ops.html
# https://docs.blender.org/api/blender_python_api_current/bpy.types.Mesh.html
# https://blender.stackexchange.com/questions/1311/how-can-i-get-vertex-positions-from-a-mesh
# https://blender.stackexchange.com/questions/14000/how-to-output-the-number-of-vertices-edges-and-faces-given-a-polygon-with-pytho
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
# https://blender.stackexchange.com/questions/125114/how-to-get-the-class-of-selected-object-in-blender-2-8
# http://wiki.theprovingground.org/blender-py-mathmesh
# https://docs.blender.org/api/blender2.8/bmesh.html
# https://blender.stackexchange.com/questions/95408/how-do-i-create-a-new-object-using-python-in-blender-2-80
# https://docs.blender.org/api/blender2.8/bpy.types.Object.html
# https://blender.stackexchange.com/questions/132825/python-selecting-object-by-name-in-2-8/124628
# https://blender.stackexchange.com/questions/61879/create-mesh-then-add-vertices-to-it-in-python/61893
# https://devtalk.blender.org/t/selecting-an-object-in-2-8/4177
# https://developer.blender.org/T57366
# https://blender.stackexchange.com/questions/101216/how-to-use-loops-foreach-set-and-polygons-foreach-set-to-add-faces-to-a-mesh
# https://blender.stackexchange.com/questions/56385/python-edit-panel-to-edit-custom-bmesh-face-layers
# https://blenderartists.org/t/how-to-build-an-armature-in-2-5x-from-xml-data/507619/3
# https://blender.stackexchange.com/questions/51684/python-create-custom-armature-without-ops
# https://docs.blender.org/api/blender2.8/info_gotcha.html
# https://docs.blender.org/api/blender2.8/info_gotcha.html#editbones-posebones-bone-bones



# https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Mesh_API




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
import json
import os
import sys
import time
from time import sleep

from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
)

class ObjectQ_Operator(bpy.types.Operator):
    bl_idname = "object.objectq_operator"
    bl_label = "object test"

    def execute(self, context):
        print("Hello World")
        #print(dir(context))
        scene = context.scene
        return {'FINISHED'}

#================================================
# Read json to create Mesh 
#================================================
class ObjectICM_Operator(bpy.types.Operator):
    bl_idname = "object.objecticm_operator"
    bl_label = "Read Mesh json"

    def execute(self, context):
        start_time = time.time()
        bpy.ops.object.mode_set(mode='OBJECT')
        sys.stdout.write("==========\n")
        sys.stdout.flush()
        print("Read Mesh Json")
        scene = context.scene
        sys.stdout.write("Importing file...\n")
        sys.stdout.flush()

        filepath = bpy.data.filepath
        #if bpy.data.filepath == "":
            #filepath = bpy.data.filepath

        if context.scene.objectfilepath == "":
            filename = "meshtest.json"
        else:
            filename = context.scene.objectfilepath
        filename = bpy.path.basename(filename)

        filenamnepath = os.path.join(os.path.dirname(filepath), filename)
        #print("filenamnepath")
        #print(filenamnepath)

        sys.stdout.write("File:" + filenamnepath + "\n")
        sys.stdout.flush()
        
        file = open(filenamnepath)
        data = json.load(file)
        #print(data)
        file.close()

        sys.stdout.write("loaded file...\n")
        sys.stdout.flush()
        #print(data['vertices'])
        verts = data['vertices']
        edges = data['edges']
        faces = data['faces']
        uvs = data['uv']

        bpy.ops.object.mode_set(mode='OBJECT')
        mesh = bpy.data.meshes.new('emptyMesh')
        obj = bpy.data.objects.new("object_name", mesh)
        for o in bpy.context.collection.objects:
            #print(o)
            o.select_set(False) 
        bpy.context.collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)  # select object
        #mesh.uv_textures.new("spiral")
        #mesh.uv_layers.new(name="spiral")
        #print(dir(mesh))

        bm = bmesh.new()
        msg = ""
        #print(dir(bm))
        #print("vertices")
        sys.stdout.write("Init Bmesh...\n")
        sys.stdout.flush()

        #for v in verts:
        for idx, v in enumerate(verts):
            msg = "verts %i of %i" % (idx, len(edges)-1)
            bm.verts.new(v)  # add a new vert
            sys.stdout.write(msg + chr(8) * len(msg))
            sys.stdout.flush()
            #sleep(0.02)
            pass
        bm.verts.ensure_lookup_table() #update array index
        sys.stdout.write("verts DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()
        #print(edges)
        
        for idx, e in enumerate(edges):
            msg = "edges %i of %i" % (idx, len(edges)-1)
            if len(e) == 2:
                bm.edges.new((bm.verts[e[0]], bm.verts[e[1]]))
                pass
            sys.stdout.write(msg + chr(8) * len(msg))
            sys.stdout.flush()
            #sleep(0.02)
            pass
        sys.stdout.write("edges DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        #print("faces")
        #for f in faces:
        for idx, f in enumerate(faces):
            #print(bm.verts[f[0]])
            #print(len(f))
            if len(f) == 3:
                bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
                #print((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
                pass
            if len(f) == 4:
                #bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]], bm.verts[f[3]] ))
                #print((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]], bm.verts[f[3]] ))
                pass
            #if len(f)
            #bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
            #sleep(0.02)
            pass
        sys.stdout.write("faces DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        #print(len(bm.uv_layers))
        #bm.uv_layers.new(do_init=False)
        #print(len(bm.uv_layers))

        #print(dir(bm))
        """
        for idx, uv in enumerate(uvs):
            #print(uv)
            #print(len(uv))
            print("UV Layer...")
            #uv_layer = bm.loops.layers.uv[0]
            #print(dir(bm))

            #print(dir(bm))

            for idxf, face in enumerate(uv):
                #print(face['face'])
                #print(face['verts'])
                #print(len(face['verts']))
                if len(face['verts']) == 3:
                    #bm.faces[face].loops[0][uv_layer].uv = (face['verts'][0]['co'][0], face['verts'][0]['co'][1])
                    #bm.faces[face].loops[1][uv_layer].uv = (face['verts'][1]['co'][0], face['verts'][1]['co'][1])
                    #bm.faces[face].loops[2][uv_layer].uv = (face['verts'][2]['co'][0], face['verts'][2]['co'][1])
                    print(face['verts'][0]['co'][0],face['verts'][0]['co'][1])

                #for v in enumerate(face['verts']):
                    #print(v)
                    #print(v[1]['co'])
                #pass
            pass
        sys.stdout.write("UV(s) DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()
        """

        #create mesh from python data
        #mesh.from_pydata(verts,edges,faces)
        # make the bmesh the object's mesh
        bm.to_mesh(mesh)  
        bm.free()  # always do this when finished
        sys.stdout.write("Bmesh DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()
        #print("UV ????")

        # https://blenderartists.org/t/get-selected-uv-vertices-coordinates/697274/4
        # https://blenderartists.org/t/accessing-uv-data-in-python-script/540440/9

        mesh.uv_layers.new(do_init=False) #create uv layer texture


        for uvidx, uv_layer in enumerate(mesh.uv_layers):
            #print("uv")
            #print(dir(uvl.data))
            #for uv in uv_layer.data:
                #print(dir(uv.index))
            #print(len(mesh.loop_triangles))
            uvfaces = uvs[uvidx]
            for idx, tri in enumerate(mesh.polygons):
                msg = "[" + str(uvidx) +"] uv %i of %i" % (idx, len(mesh.polygons)-1)
                #print(dir(tri))
                #print(tri.index)
                #print(uvfaces[idx])
                #print(uvfaces[idx]['verts'])
                verts = uvfaces[idx]['verts']
                for i, loop_index in enumerate(tri.loop_indices):
                    #print(loop_index, i)
                    #print(uv_layer.data[loop_index].uv)
                    uv_layer.data[loop_index].uv = (verts[i]['co'][0],verts[i]['co'][1])
                    #print(uv_layer.data[loop_index].uv)
                sys.stdout.write(msg + chr(8) * len(msg))
                sys.stdout.flush()
                #sleep(0.5)

        sys.stdout.write("UV(s) DONE" + " "*len(msg)+"\n")
        sys.stdout.flush()

        """
        for idx, face in enumerate(mesh.polygons):
            for i in face.loop_indices:
                l = mesh.loops[i]
                v = mesh.vertices[l.vertex_index]
                print("	Loop index", l.index, "points to vertex index", l.vertex_index,"at position", v.co)

                for j, ul in enumerate(mesh.uv_layers):
                    print("l.index")
                    print(l.index)
                    print("		UV Map", j, "has coordinates", ul.data[l.index].uv, "for this loop index")
                    ul.data[l.index].uv = (0,0)
            pass
        """

        #import_obj.py
        #print(len(mesh.uv_layers))
        #for uv_layer in mesh.uv_layers:
            #print("....")
            #print(len(mesh.loop_triangles))
            #for tri in mesh.loop_triangles:
                #print("ddddd")
                #for loop_index in tri.loops:
                    #print("dddddssss")
                    #print(uv_layer.data[loop_index].uv)
        

        bpy.ops.object.mode_set(mode='OBJECT')  # return to object mode
        print('finished import in %s seconds' %
                  ((time.time() - start_time)))
        return {'FINISHED'}

#================================================
# Create Mesh test
#================================================
class ObjectCM_Operator(bpy.types.Operator):
    bl_idname = "object.objectcm_operator"
    bl_label = "Create Mesh"

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
        #mesh.update()
        
        # make the bmesh the object's mesh
        bm.to_mesh(mesh)  
        bm.free()  # always do this when finished
        bpy.ops.object.mode_set(mode='OBJECT')  # return to object mode

        #self.report({'WARNING', 'INFO'}, "mesh create!")
        print("finish")

        return {'FINISHED'}

#================================================
# Mesh Write to json
#================================================
class ObjectWM_Operator(bpy.types.Operator):
    bl_idname = "object.objectwm_operator"
    bl_label = "Write Mesh json"

    def execute(self, context):
        start_time = time.time()
        print("==========")
        scene = context.scene
        sys.stdout.write("Checking Object Mesh!\n")
        sys.stdout.flush()
        
        objectType = bpy.context.object.type
        #print(objectType)
        if objectType == "MESH":
            objjson = {}
            sys.stdout.write("Init Object json!\n")
            sys.stdout.flush()
            ob = bpy.context.object
            #print(dir(ob))
            me = bpy.context.object.data
            #print(dir(me))

            msg = ""

            sys.stdout.write("Writing Object Mesh...\n")
            sys.stdout.flush()
            vertices = []
            for idx, v in enumerate(me.vertices):
                msg = "Vertices %i of %i" % (idx, len(me.vertices)-1)
                vertices.append((v.co[0],v.co[1],v.co[2]))
                sys.stdout.write(msg + chr(8) * len(msg))
                sys.stdout.flush()
                #sleep(0.05)
                pass
            objjson["vertices"] = vertices
            sys.stdout.write("Vertices DONE" + " "*len(msg)+"\n")
            sys.stdout.flush()


            #sys.stdout.write("Reading Edges!\n")
            #sys.stdout.flush()
            edges = []
            for idx, edge in enumerate(me.edges):
                msg = "Edges %i of %i" % (idx, len(me.vertices)-1)
                if 2 == len(edge.vertices):
                    #print(edge.vertices[0].real,edge.vertices[1].real)
                    edges.append((edge.vertices[0].real,edge.vertices[1].real))
                    pass
                sys.stdout.write(msg + chr(8) * len(msg))
                sys.stdout.flush()
                #sleep(0.05)
                pass
            objjson["edges"] = edges
            sys.stdout.write("Edges DONE" + " "*len(msg)+"\n")
            sys.stdout.flush()


            #sys.stdout.write("Reading Faces!\n")
            #sys.stdout.flush()
            faces = []
            #for face in me.polygons:
            for idx, face in enumerate(me.polygons):
                msg = "Faces %i of %i" % (idx, len(me.polygons)-1)
                if 3 == len(face.vertices):
                    #print(face.vertices[0],face.vertices[1],face.vertices[2])
                    faces.append((face.vertices[0],face.vertices[1],face.vertices[2]))
                    pass
                if 4 == len(face.vertices):
                    #print(face.vertices[0],face.vertices[1],face.vertices[2],face.vertices[3])
                    faces.append((face.vertices[0],face.vertices[1],face.vertices[2],face.vertices[2]))
                    pass
                sys.stdout.write(msg + chr(8) * len(msg))
                sys.stdout.flush()
                #sleep(0.05)
                pass
            objjson["faces"] = faces
            sys.stdout.write("Faces DONE" + " "*len(msg)+"\n")
            sys.stdout.flush()

            #sys.stdout.write("Reading UV(s)!\n")
            #sys.stdout.flush()

            #sys.stdout.write("UV count: "+ str(len(me.uv_layers)) + "!\n")
            #sys.stdout.flush()
            # https://blender.stackexchange.com/questions/9399/add-uv-layer-to-mesh-add-uv-coords-with-python
            uv_layers = []
            #print(len(me.uv_layers))
            if len(me.uv_layers) > 0:
                uv_layer = me.uv_layers.active.data
                uvfaces = []
                for poly in me.polygons:
                    #print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))
                    msg = "face uv %i of %i" % (poly.index, len(me.polygons)-1)
                    # range is used here to show how the polygons reference loops,
                    # for convenience 'poly.loop_indices' can be used instead.
                    uv = []
                    for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
                        #print("    Vertex: %d" % me.loops[loop_index].vertex_index)
                        #print("    UV: %r" % uv_layer[loop_index].uv)
                        uv.append({"index":me.loops[loop_index].vertex_index,"co":(uv_layer[loop_index].uv[0],uv_layer[loop_index].uv[1])})
                        pass
                    #print(uv)
                    uvfaces.append({"face":poly.index,"verts":uv})
                    sys.stdout.write(msg + chr(8) * len(msg))
                    sys.stdout.flush()
                    #sleep(0.05)
                uv_layers.append(uvfaces)
                    
            objjson["uv"] = uv_layers
            sys.stdout.write("UV Layers DONE" + " "*len(msg)+"\n")
            sys.stdout.flush()
            
            # stringjson = json.dumps(objjson)
            stringjson = json.dumps(objjson,indent=4)
            #print("==========================")
            #print(stringjson)
            # https://docs.blender.org/api/blender2.8/bpy.data.html
            # https://blender.stackexchange.com/questions/6842/how-to-get-the-directory-of-open-blend-file-from-python

            filepath = bpy.data.filepath
            directory = os.path.dirname(filepath)
            filename = context.scene.objectfilepath
            if context.scene.objectfilepath == "":
                filename = "meshtest.json"
            filename = bpy.path.basename(filename)
            filenamnepath = os.path.join(directory, filename)

            sys.stdout.write("Open and write file json!\n")
            sys.stdout.flush()
            print("Output : " + filenamnepath)
            f= open(filenamnepath,"w+")
            f.write(stringjson)
            f.close()
            sys.stdout.write("Close file json!\n")
            sys.stdout.flush()

        #sys.stdout.write("End Object json!\n")
        #sys.stdout.flush()
        print('Finished Export in %s seconds' %
                  ((time.time() - start_time)))
        return {'FINISHED'}

#================================================
# Armture test
#================================================
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

# To edit bone is to object edit mode. Not pose or object mode.
# bpy.context.active_pose_bone #pose mode
# bpy.context.active_bone
# bpy.context.selected_editable_bones #edit bone
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
#================================================
# Panel
#================================================
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

        col = layout.column()
        col.label(text="Objectq", icon='WORLD_DATA')

        col.label(text="Active object is: " + obj.name)
        col.prop(obj, "name")

        col.label(text="Test ")
        col.operator("object.objectq_operator")
        col.separator_spacer()
        col.label(text="MESH")
        col.operator("object.objectcm_operator")
        
        col.prop(context.scene,"objectfilepath")
        col.operator("object.objecticm_operator")
        col.operator("object.objectwm_operator")

        col.separator_spacer()
        col.label(text="ARMATURE")
        col.operator("object.objectca_operator")

classes = (
    ObjectQ_Operator,
    ObjectICM_Operator, #read mesh json
    ObjectCM_Operator, # create mesh
    ObjectWM_Operator, # wrtie mesh json
    ObjectCA_Operator,
    ObjectA_Operator,
    Objectq_Panel,
)

def register():
    #print("Hello World")
    #bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback) 
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.objectfilepath = StringProperty(subtype='FILE_PATH')
    bpy.types.Scene.meshfilepath = StringProperty(subtype='FILE_PATH')
    

def unregister():
    #print("Goodbye World")
    #bpy.types.VIEW3D_MT_editor_menus.remove(addmenu_callback) 
    for cls in classes:
        bpy.utils.unregister_class(cls)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()