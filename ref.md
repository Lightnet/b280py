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
class Object_PT_Custom(bpy.types.Panel):

    def draw(self, context):
    
        #print(context.mode)
        #print(context.area.type)
        #print(context.region.type)
        #space_type = context.space_data.type
        #print(space_type) #PROPERTIES panel
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

```
"WINDOW" ('EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES')
```


# Links:
 * https://docs.blender.org/api/blender2.8/info_tips_and_tricks.html
 * https://docs.blender.org/api/blender2.8/info_overview.html
 * https://theduckcow.com/2019/update-addons-both-blender-28-and-27-support/
 * https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
 * https://wiki.blender.org/wiki/Main_Page
 * https://gist.github.com/AzureDVBB/0b3d941a719e88574533da45d4970492
 * https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo
 * https://blenderartists.org/t/2-80-cheat-sheet-for-updating-add-ons/1148974
 * https://devtalk.blender.org/t/add-on-panel-missing-from-active-tool-workspace-settings/7349/3
 * https://blenderartists.org/t/making-user-interface-with-python-blender-2-8/1153253/2
 * https://github.com/vvoovv/blender-osm/issues/113
 * https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/UI_API
 * https://www.reddit.com/r/gamedev/comments/a41yns/blender_28_python_ui_panels_buttons/
 * https://docs.blender.org/manual/en/dev/interface/window_system/workspaces.html