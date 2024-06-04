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
import bpy

from .preferences import Preferences

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


has_run = False
def register():
    bpy.utils.register_class(Preferences)
    bpy.context.preferences.addons[__package__.split('.')[0]].preferences.load() # type: ignore


def unregister():
    bpy.context.preferences.addons[__package__.split('.')[0]].preferences.save() # type: ignore
    bpy.utils.unregister_class(Preferences)
