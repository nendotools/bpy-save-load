from bpy.props import IntProperty
from bpy.types import Operator

from .preferences import Preferences

class AddMenuItemOperator(Operator):
    bl_idname = "wm.add_menu_item"
    bl_label = "Add Menu Item"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        preferences: Preferences = context.preferences.addons[__package__.split('.')[0]].preferences # type: ignore
        preferences.name_number_sets.add()
        return {'FINISHED'}

class RemoveMenuItemOperator(Operator):
    bl_idname = "wm.remove_menu_item"
    bl_label = "Remove Menu Item"
    bl_options = {'REGISTER', 'UNDO'}
    index: IntProperty() # type: ignore
    def execute(self, context):
        preferences: Preferences = context.preferences.addons[__package__.split('.')[0]].preferences # type: ignore
        preferences.name_number_sets.remove(self.index)
        return {'FINISHED'}
