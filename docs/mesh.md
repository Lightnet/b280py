# Information:
  There are two way or more way to handle mesh.

  * Creating meshes need import bmesh to build the object.
```python
import bpy
import bmesh

#raws
verts = [(2.0, 2.0, 2.0), (-2.0, 2.0, 2.0),(-2.0, -2.0, 2.0)]
edges = []
#edges = [(0, 1), (1, 2), (2, 0)]
faces = []
faces = [(0, 1, 2)]

bm = bmesh.new()
#me.vertices

#for v in verts:
    #bm.verts.new(v)  # add a new vert

vert1 = bm.verts.new(verts[0])
vert2 = bm.verts.new(verts[1])
vert3 = bm.verts.new(verts[2])

bm.verts.ensure_lookup_table() #update array index else error when assign face

for f in faces:
    #print(bm.verts[f[0]])
    bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))

# for edge is same as the face assign since it can't be array but vertice id system
```

 * Reading mesh from scene
```python
import bpy

me = bpy.context.object.data # current select has to be MESH

vertices = []
for v in me.vertices: #vertices
    #print(dir(v))
    #print(v.co)
    #print(v.co[0])
    vertices.append((v.co[0],v.co[1],v.co[2]))

edges = []
for edge in me.edges: #edges
    if 2 == len(edge.vertices):
        #print("edges id:")
        #print(edge.vertices[0].real,edge.vertices[1].real)
        edges.append((edge.vertices[0].real,edge.vertices[1].real))
faces = []

for face in me.polygons: #faces
    #print(len(face.vertices))
    if 3 == len(face.vertices):
        #print(face.vertices[0],face.vertices[1],face.vertices[2])
        faces.append((face.vertices[0],face.vertices[1],face.vertices[2]))
        pass
    if 4 == len(face.vertices):
        #print(face.vertices[0],face.vertices[1],face.vertices[2],face.vertices[3])
        faces.append((face.vertices[0],face.vertices[1],face.vertices[2],face.vertices[2]))
        pass

uv_layer = me.uv_layers.active.data
for poly in me.polygons:
    #print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))

    # range is used here to show how the polygons reference loops,
    # for convenience 'poly.loop_indices' can be used instead.
    for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
        #print("    Vertex: %d" % me.loops[loop_index].vertex_index)
        #print("    UV: %r" % uv_layer[loop_index].uv)
        pass
```

 * Read Mesh from scene and add to it.
```python
#It required object scene and bmesh to add or modified mesh.

import bpy
import bmesh

mesh = bpy.context.object.data
bm = bmesh.new()
# convert the current mesh to a bmesh (must be in edit mode)
bpy.ops.object.mode_set(mode='EDIT')
bm.from_mesh(mesh)
bpy.ops.object.mode_set(mode='OBJECT')  # return to object mode
verts = [(2.0, 2.0, 2.0), (-2.0, 2.0, 2.0),(-2.0, -2.0, 2.0)]
for v in verts:
    bm.verts.new(v)  # add a new vert

# make the bmesh the object's mesh
bm.to_mesh(mesh) 
bm.free()  # always do this when finished

```

# Link object to scene and update
```
#bpy.context.collection.objects.link(Obj)

# Update view layer
#layer = bpy.context.view_layer
#layer.update()
```

 * https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API