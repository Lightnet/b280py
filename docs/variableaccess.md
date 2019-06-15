# Variable access:
 There are couples of way of local to global variable access.

```
print(dir(bpy.data)) to list the data to be access
```
This will list the access able variable for global access. When creating a variable.


```
print(bpy.data.scenes[0].my_int) #current scene access variable
```

```
class Example_Panel(bpy.types.Panel):
    bl_label = "Example Panel"
    bl_idname = "OBJECT_PT_Example"

    def draw(self, context):
        scene = context.scene #current scene
        print(scene.my_int)

```