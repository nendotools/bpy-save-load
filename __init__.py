import bpy

from .operators import AddMenuItemOperator, RemoveMenuItemOperator
from .preferences import CustomProperties, Preferences

bl_info = {
    "name": "Example Save Load",
    "description":
        "This is an example of how to save and load settings in Blender.",
    "author": "NENDO",
    "version": (0, 0, 1),
    "blender": (2, 93, 0),
    "location": "",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "3D View",
}


def register():
    bpy.utils.register_class(AddMenuItemOperator)
    bpy.utils.register_class(RemoveMenuItemOperator)
    bpy.utils.register_class(CustomProperties)
    bpy.utils.register_class(Preferences)
    bpy.context.preferences.addons[__package__.split('.')[0]].preferences.load() # type: ignore


def unregister():
    bpy.context.preferences.addons[__package__.split('.')[0]].preferences.save() # type: ignore
    bpy.utils.unregister_class(Preferences)
    bpy.utils.unregister_class(CustomProperties)
    bpy.utils.unregister_class(RemoveMenuItemOperator)
    bpy.utils.unregister_class(AddMenuItemOperator)
