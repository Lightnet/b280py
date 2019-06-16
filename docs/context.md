


# Redraw

```python
for a in bpy.context.screen.areas:
    if a.type == 'VIEW_3D':
        a.tag_redraw() #bgl redraw in VIEW_3D
        break
```

```python
def draw(self,context)
    for a in context.screen.areas:
        if a.type == 'VIEW_3D':
            a.tag_redraw() #bgl redraw in VIEW_3D
            break
```

```python
    bpy.context.area.tag_redraw()

```


# Nav Bar Properties:
 To set view panel.

```python
bpy.context.space_data.context = 'OBJECT'
```
```
'TOOL', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'SCENE', 'WORLD', 'OBJECT', 'MODIFIER', 'PARTICLES', 'PHYSICS', 'CONSTRAINT', 'DATA', 'MATERIAL', 'TEXTURE'
```

# Viewport Type Set:

```python
bpy.context.area.ui_type = 'VIEW_3D'
```
```
'VIEW_3D', 'VIEW', 'UV', 'ShaderNodeTree', 'CompositorNodeTree', 'TextureNodeTree', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET', 'TIMELINE', 'FCURVES', 'DRIVERS', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES'
```

# window manager:
```python
bpy.context.window_manager
```
```python
def invoke(self, context, event):
    wm = context.window_manager
```

# active object

```python
obj = bpy.context.active_object
```

```python
def execute(self, context):
    obj = context.active_object
```

# Scene link object:
```python
bpy.context.collection.objects.link(Obj)
```


# update scene layer:
```python
layer = bpy.context.view_layer
layer.update()
```
