# Information:
 Working on the simple guides. Blender API is design to have module buiilds. As the classes has to call to display as menu, panel, object data and others. To execute command from bpy.ops.___ bpy.wm.___ from call functions with params or not.

 Data storing can be save from filename.blend

 * https://docs.blender.org/api/master/info_api_reference.html#data-access

# Prefix Naming:
 Having the name prefix is a must. Reason is simple to able to call out their function class. As well they are case sensitive. Else give error warning the prefix. 

# Tips:
 * Best way to handle when create variable that all must be under register and unregister function call to clear data leaking. When you can refresh in addon to reload script else it remain blender current running.

# Guides:
