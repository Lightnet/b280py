
# Blender Preferences:
```
 Inferface > 
   Display >
     [check] Python Tooltips
     [check] Tooltips
     [check] Developer Extras
```
 Notes:
  * Used for bpy.types.VIEW3D_MT_editor_menus.append(addmenu_callback) when hover the mouse to know the menu button location.

# Blender UI:
 * 2.80\scripts\startup\bl_ui
 * properties_workspace.py
 * properties_view_layer.py
 * properties_texture.py
 * properties_scene.py
 * properties_render.py
 * space_properties.py 
 * space_topbar.py
 * 
 * 
 * 
 * 

# Call:
```

#bpy.ops.wm.call_menu(name="OBJECT_MT_test")

```
 * https://docs.blender.org/api/blender2.8/bpy.types.Operator.html



# Commands:
z = menu shading
, = pos,rot,scale
. = poivt
f3 = menu search

# Object Mode:


# Edit Mode:


# 

# bl_region_type
enum in [‘WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL_PROPS’, ‘PREVIEW’, ‘HUD’, ‘NAVIGATION_BAR’, ‘EXECUTE’, ‘FOOTER’, ‘TOOL_HEADER’], default ‘WINDOW’


# bl_space_type > The space where the panel is going to be used in
```
EMPTY > Empty.
VIEW_3D > 3D Viewport, Manipulate objects in a 3D environment.
IMAGE_EDITOR > UV/Image Editor, View and edit images and UV Maps.
NODE_EDITOR > Node Editor, Editor for node-based shading and compositing tools.
SEQUENCE_EDITOR > Video Sequencer, Video editing tools.
CLIP_EDITOR > Movie Clip Editor, Motion tracking tools.
DOPESHEET_EDITOR > Dope Sheet, Adjust timing of keyframes.
GRAPH_EDITOR > Graph Editor, Edit drivers and keyframe interpolation.
NLA_EDITOR > Nonlinear Animation, Combine and layer Actions.
TEXT_EDITOR > Text Editor, Edit scripts and in-file documentation.
CONSOLE > Python Console, Interactive programmatic console for advanced editing and script development.
INFO > Info, Log of operations, warnings and error messages.
TOPBAR > Top Bar, Global bar at the top of the screen for global per-window settings.
STATUSBAR > Status Bar, Global bar at the bottom of the screen for general status information.
OUTLINER > Outliner, Overview of scene graph and all available data-blocks.
PROPERTIES > Properties, Edit properties of active object and related data-blocks.
FILE_BROWSER > File Browser, Browse for files and assets.
PREFERENCES > Preferences, Edit persistent configuration settings.
```

# PROPERTIES > Render > Custom Panel
```
class CustomToolx_Panel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = "render"
    #bl_context = "output"
    #bl_context = "view_layer" #view layer
    #bl_context = "scene"
    #bl_context = "world"
    #bl_context = "object"
    #bl_context = "modifier"
    #bl_context = "particle" # Particles
    #bl_context = "effects" #unknown
    #bl_context = "physics"
    #bl_context = "constraint" #object constraint
    #bl_context = "bone"
    #bl_context = "bone_constraint"
    #bl_context = "data" #object data
    #bl_context = "material"
    #bl_context = "texture"
```
 Note:
  * Can be found in 2.80\scripts\startup\bl_ui folder.



# Menu / Header
```python
#def menu_func(self, context):
    #layout = self.layout
    #layout.separator()
    #layout.operator(WM_OT_button_context_test.bl_idname)

#bpy.types.TOPBAR_MT_file.append(menu_func)# File Menu Top Left
#bpy.types.TOPBAR_MT_file_import.append(menu_func)
#bpy.types.TOPBAR_MT_file_export.append(menu_func)

#bpy.types.VIEW3D_MT_editor_menus.append(menu_func)
#bpy.types.VIEW3D_MT_object.append(menu_func)

#bpy.types.WM_MT_button_context.append(menu_func)

#bpy.types.VIEW3D_MT_object.remove(menu_func)
```
 Note:
  * append and remove for class or callback




