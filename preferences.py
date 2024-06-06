# type: ignore 

from bpy.types import AddonPreferences, PropertyGroup, Context
from bpy.props import (
    CollectionProperty,
    StringProperty,
    IntProperty,
    FloatProperty,
    BoolProperty,
    FloatVectorProperty
)

class CustomProperties(PropertyGroup):
    string_prop: StringProperty(
        name="String",
        default="",
    )
    int_prop: IntProperty(
        name="Integer",
        default=0,
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
        min=0.0,
        max=1.0,
        default=(0.7, 0.7, 0.7, 1.0),
    )

    coordinate_pref: FloatVectorProperty(
        name="Coordinate",
        subtype="COORDINATES",
        size=3,
        default=(0.0, 0.0, 0.0),
    )
    name_number_sets: CollectionProperty(
        type=CustomProperties
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

        layout.operator("wm.add_menu_item")
        if not self.name_number_sets:
            layout.label(text="No items")
        else:
            for (index, item) in enumerate(self.name_number_sets):
                r = layout.row()
                r.prop(item, "string_prop")
                r.prop(item, "int_prop")
                r.operator("wm.remove_menu_item", text="Remove").index = index


    def save(self):
        print("Saved")
    
    def load(self):
        print("Loaded")
