
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

#
```python
bl_info = {
  "name": "None",
  "author":"none",
  "version":(0,0,1),
  "blender": (2,80,0),
  "location": "none",
  "category": "none",
  "warning": "",
  "wiki_url": "",
}
import bpy

def register():
  #print("Hello World")
  # Notes varaible setup should be here.
  # Reason is bpy.data update later
  bpy.types.Scene.my_int = IntProperty()
  print(bpy.data.scenes[0].my_int)

def unregister():
  #print("Goodbye World")

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
```


# Blender UI Ref:
 * 2.80\scripts\startup\bl_ui
 * properties_workspace.py
 * properties_view_layer.py
 * properties_texture.py
 * properties_scene.py
 * properties_render.py
 * space_properties.py 
 * space_topbar.py

# operator:

```
bpy.ops.screen
```


# Calls:
```python
# https://docs.blender.org/api/master/bpy.context.html?highlight=space_data
# https://docs.blender.org/api/master/bpy.ops.html
# https://docs.blender.org/api/master/bpy.ops.wm.html
#bpy.ops.wm.call_menu(name="OBJECT_MT_test")

bpy.ops.wm.operator_cheat_sheet()

bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.object.editmode_toggle()
bpy.ops.sculpt.sculptmode_toggle()
bpy.ops.paint.texture_paint_toggle()

bpy.context.space_data.context = 'OBJECT'
bpy.context.space_data.context = 'WORLD'
bpy.context.space_data.context = 'SCENE'

'TOOL', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'SCENE', 'WORLD', 'OBJECT', 'MODIFIER', 'PARTICLES', 'PHYSICS', 'CONSTRAINT', 'DATA', 'MATERIAL', 'TEXTURE'


bpy.context.area.ui_type = 'VIEW_3D'
bpy.context.area.ui_type = 'PROPERTIES'
bpy.context.area.ui_type = 'FILE_BROWSER'

'VIEW_3D', 'VIEW', 'UV', 'ShaderNodeTree', 'CompositorNodeTree', 'TextureNodeTree', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET', 'TIMELINE', 'FCURVES', 'DRIVERS', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES'


class ExampleOperator(Operator):
  bl_idname = "object.exampleoperator"
  bl_label = "example operator"


  def invoke(self, context, event):
    wm = context.window_manager
    return wm.invoke_props_dialog(self)
#
# invoke_props_dialog
# invoke_props_popup
# invoke_confirm
```
 * https://docs.blender.org/api/blender2.8/bpy.types.Operator.html


# Data Store:
```python
# note it depend where to store data.
# * from plugin
# * from blend

from bpy.props import EnumProperty, CollectionProperty, IntProperty, StringProperty, BoolProperty

bpy.types.Scene.my_int = IntProperty(default=1)
bpy.types.Material.my_int = IntProperty(default=2)
bpy.types.Object.my_int = IntProperty(default=3)
bpy.types.World.my_int = IntProperty(default=3)
bpy.types.Texture.my_int = IntProperty(default=3)

bpy.types.Collection.my_int = IntProperty(default=3)

print(bpy.data.scenes[0].my_int)
print(bpy.data.materials[0].my_int)
print(bpy.data.objects[0].my_int)
print(bpy.data.worlds[0].my_int)

print(bpy.data.collections[0].my_int)

print(dir(bpy.types))

# As long bpy.data.____[0].(custom var or group) that has attach to access
# print(dir(bpy.data)) to list the data to be access

```



# Commands:
```
z = menu shading
, = pos,rot,scale
. = poivt
f3 = menu search
```
# Object Mode:


# Edit Mode:



# bl_region_type
```
WINDOW
HEADER
CHANNELS
TEMPORARY
UI
TOOLS
TOOL_PROPS
PREVIEW
HUD
NAVIGATION_BAR
EXECUTE
FOOTER
TOOL_HEADER

default ‘WINDOW’
```

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
```python
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


# template_list
```python
class ExamplePropsGroup(bpy.types.PropertyGroup):
    boolean : BoolProperty(default=False)
    name : StringProperty() #default for name display in list
    bexport : BoolProperty(default=False, name="Export", options={"HIDDEN"},
                           description = "This will be ignore when exported")
    bselect : BoolProperty(default=False, name="Select", options={"HIDDEN"},
                           description = "This will be ignore when exported")
    otype : StringProperty(name="Type",description = "This will be ignore when exported")
bpy.utils.register_class(ExamplePropsGroup)
bpy.types.Scene.examplecollection_list = CollectionProperty(type=ExamplePropsGroup)
bpy.types.Scene.examplecollection_list_idx = IntProperty()

class CustomTemplateList_Panel(bpy.types.Panel):
  bl_idname = "OBJECT_PT_CustomTemplateList"
  bl_space_type = 'PROPERTIES'
  bl_region_type = 'WINDOW'

  def draw(self, context):
    layout = self.layout
    row = layout.row()
    row.template_list("UI_UL_list",
      "examplecollection_list", 
      context.scene, 
      "examplecollection_list",
      context.scene, 
      "examplecollection_list_idx",
      rows=5
    )

```


