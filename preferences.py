# type: ignore 

from bpy.types import AddonPreferences, Context
from bpy.props import (
    StringProperty,
    IntProperty,
    FloatProperty,
    BoolProperty,
    FloatVectorProperty
)

class Preferences(AddonPreferences):
    bl_idname = __package__

    string_pref: StringProperty(
        name="String",
        default="",
    )

    int_pref: IntProperty(
        name="Integer",
        default=0,
    )

    float_pref: FloatProperty(
        name="Float",
        default=0.0,
    )

    bool_pref: BoolProperty(
        name="Boolean",
        default=False,
    )

    color_pref: FloatVectorProperty(
        name="Color",
        subtype="COLOR",
        size=4,
        default=(0.0, 0.0, 0.0, 1.0),
    )

    coordinate_pref: FloatVectorProperty(
        name="Coordinate",
        subtype="XYZ",
        size=3,
        default=(0.0, 0.0, 0.0),
    )

    def draw(self, context: Context):
        layout = self.layout
        layout.label(text="This is an example of how to save and load settings in Blender.")

        layout.prop(self, "string_pref")
        layout.prop(self, "int_pref")
        layout.prop(self, "float_pref")
        layout.prop(self, "bool_pref")
        layout.prop(self, "color_pref")
        layout.prop(self, "coordinate_pref")

    def save(self):
        print("Saved")
    
    def load(self):
        print("Loaded")
