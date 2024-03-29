# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# https://gist.github.com/p2or/30b8b30c89871b8ae5c97803107fd494
# https://blender.stackexchange.com/questions/30444/create-an-interface-which-is-similar-to-the-material-list-box

# it under scripting workspace > sidebar > misc

bl_info = {
    "name": "custom material-pointer-uilist-dev",
    "description": "",
    "author": "p2or",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Text Editor",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import bpy

from bpy.props import (IntProperty,
                       BoolProperty,
                       StringProperty,
                       CollectionProperty,
                       PointerProperty)

from bpy.types import (Operator,
                       Panel,
                       PropertyGroup,
                       UIList)


def random_color():
    from mathutils import Color
    from random import random
    return Color((random(), random(), random()))

# -------------------------------------------------------------------
#   Operators
# -------------------------------------------------------------------

class CUSTOM_OT_actions(Operator):
    """Move items up and down, add and remove"""
    bl_idname = "custom.list_action"
    bl_label = "List Actions"
    bl_description = "Move items up and down, add and remove"
    bl_options = {'REGISTER'}

    action: bpy.props.EnumProperty(
        items=(
            ('UP', "Up", ""),
            ('DOWN', "Down", ""),
            ('REMOVE', "Remove", ""),
            ('ADD', "Add", "")))

    def invoke(self, context, event):
        scn = context.scene
        idx = scn.custom_index

        try:
            item = scn.custom[idx]
        except IndexError:
            pass
        else:
            if self.action == 'DOWN' and idx < len(scn.custom) - 1:
                item_next = scn.custom[idx+1].name
                scn.custom.move(idx, idx+1)
                scn.custom_index += 1
                info = 'Item "%s" moved to position %d' % (item.name, scn.custom_index + 1)
                self.report({'INFO'}, info)

            elif self.action == 'UP' and idx >= 1:
                item_prev = scn.custom[idx-1].name
                scn.custom.move(idx, idx-1)
                scn.custom_index -= 1
                info = 'Item "%s" moved to position %d' % (item.name, scn.custom_index + 1)
                self.report({'INFO'}, info)

            elif self.action == 'REMOVE':
                item = scn.custom[scn.custom_index]
                item_name = item.material.name
                mat = item.material                
                mat_obj = bpy.data.materials.get(mat.name, None)
                if mat_obj:
                    bpy.data.materials.remove(mat_obj, do_unlink=True)
                info = 'Item %s removed from scene' % (item_name)
                scn.custom.remove(idx)
                if scn.custom_index == 0:
                    scn.custom_index = 0
                else:
                    scn.custom_index -= 1
                self.report({'INFO'}, info)

        if self.action == 'ADD':
            item = scn.custom.add()
            item.id = len(scn.custom)
            item.material = bpy.data.materials.new(name="Material")
            item.name = item.material.name
            col = random_color()
            item.material.diffuse_color = (col.r, col.g, col.b, 1.0)
            scn.custom_index = (len(scn.custom)-1)
            info = '%s added to list' % (item.name)
            self.report({'INFO'}, info)
        return {"FINISHED"}


class CUSTOM_OT_printItems(Operator):
    """Print all items and their properties to the console"""
    bl_idname = "custom.print_items"
    bl_label = "Print Items to Console"
    bl_description = "Print all items and their properties to the console"
    bl_options = {'REGISTER', 'UNDO'}

    reverse_order: BoolProperty(
        default=False,
        name="Reverse Order")

    @classmethod
    def poll(cls, context):
        return bool(context.scene.custom)

    def execute(self, context):
        scn = context.scene
        if self.reverse_order:
            for i in range(scn.custom_index, -1, -1):        
                mat = scn.custom[i].material
                print ("Material:", mat,"-",mat.name, mat.diffuse_color)
        else:
            for item in scn.custom:
                mat = item.material
                print ("Material:", mat,"-",mat.name, mat.diffuse_color)
        return{'FINISHED'}


class CUSTOM_OT_clearList(Operator):
    """Clear all items of the list and remove from scene"""
    bl_idname = "custom.clear_list"
    bl_label = "Clear List and Remove Materials"
    bl_description = "Clear all items of the list and remove from scene"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return bool(context.scene.custom)

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):

        if bool(context.scene.custom):
            # Remove materials from scene
            for i in context.scene.custom:
                name = i.material.name
                mat_obj = bpy.data.materials.get(name, None)
                if mat_obj:
                    bpy.data.materials.remove(mat_obj, do_unlink=True)
                info = 'Item %s removed from scene' % (name)

            # Clear the list
            context.scene.custom.clear()
            self.report({'INFO'}, "All materials removed from scene")
        else:
            self.report({'INFO'}, "Nothing to remove")
        return{'FINISHED'}


# -------------------------------------------------------------------
#   Drawing
# -------------------------------------------------------------------

class CUSTOM_UL_items(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        mat = item.material
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            split = layout.split(factor=0.3)
            split.label(text="Index: %d" % (index))
            # static method UILayout.icon returns the integer value of the icon ID
            # "computed" for the given RNA object.
            split.prop(mat, "name", text="", emboss=False, icon_value=layout.icon(mat))

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=layout.icon(mat))

    def invoke(self, context, event):
        pass

class CUSTOM_PT_objectList(Panel):
    """Adds a custom panel to the TEXT_EDITOR"""
    bl_idname = 'TEXT_PT_my_panel'
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_label = "Custom Material List Demo"

    def draw(self, context):
        layout = self.layout
        scn = bpy.context.scene

        rows = 2
        row = layout.row()
        row.template_list("CUSTOM_UL_items", "custom_def_list", scn, "custom", 
            scn, "custom_index", rows=rows)

        col = row.column(align=True)
        col.operator("custom.list_action", icon='ZOOM_IN', text="").action = 'ADD'
        col.operator("custom.list_action", icon='ZOOM_OUT', text="").action = 'REMOVE'
        col.separator()
        col.operator("custom.list_action", icon='TRIA_UP', text="").action = 'UP'
        col.operator("custom.list_action", icon='TRIA_DOWN', text="").action = 'DOWN'

        row = layout.row()
        row.template_list("CUSTOM_UL_items", "custom_grid_list", scn, "custom", 
            scn, "custom_index", rows=2, type='GRID')

        row = layout.row()
        col = row.column(align=True)
        row = col.row(align=True)
        row.operator("custom.print_items", icon="LINENUMBERS_ON")
        row = col.row(align=True)
        row.operator("custom.clear_list", icon="X")


# -------------------------------------------------------------------
#   Collection
# -------------------------------------------------------------------

class CUSTOM_objectCollection(PropertyGroup):
    #name: StringProperty() -> Instantiated by default
    material: PointerProperty(
        name="Material",
        type=bpy.types.Material)

# -------------------------------------------------------------------
#   Register & Unregister
# -------------------------------------------------------------------

classes = (
    CUSTOM_OT_actions,
    CUSTOM_OT_printItems,
    CUSTOM_OT_clearList,
    CUSTOM_UL_items,
    CUSTOM_PT_objectList,
    CUSTOM_objectCollection,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    # Custom scene properties
    bpy.types.Scene.custom = CollectionProperty(type=CUSTOM_objectCollection)
    bpy.types.Scene.custom_index = IntProperty()


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.custom
    del bpy.types.Scene.custom_index


if __name__ == "__main__":
    register()