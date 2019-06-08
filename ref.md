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


validating class: enum "WINDOW" not found in ('EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES')


https://devtalk.blender.org/t/add-on-panel-missing-from-active-tool-workspace-settings/7349/3



