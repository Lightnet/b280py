 # Notes:
  * Subject change if API updated.
  * Those are tested.

```
# [PROPERTIES] Navbar > Active Tool and workspace settings
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
```

```
# [PROPERTIES] Navbar > ALL >
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
```

```
# [PROPERTIES] Navbar > Object
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
```

```
# https://blenderartists.org/t/editing-the-menu-bars-without-using-the-python-api/1126562/2
# Here's the classes for File, Edit, Render, Window, Help

#  TOPBAR_MT_file
#  TOPBAR_MT_edit
#  TOPBAR_MT_render
#  TOPBAR_MT_window
#  TOPBAR_MT_help

def draw_item(self, context):	
	self.layout.menu("..._MT_custommenu")

#bpy.types.VIEW3D_MT_editor_menus.append(draw_item) #3d viewport menu header
#bpy.types.TOPBAR_MT_file.append(draw_item)# File Menu Top Left

#bpy.types.VIEW3D_MT_editor_menus.remove(draw_item)
#bpy.types.TOPBAR_MT_file.remove(draw_item)
```

validating class: enum "WINDOW" not found in ('EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES')


https://devtalk.blender.org/t/add-on-panel-missing-from-active-tool-workspace-settings/7349/3



