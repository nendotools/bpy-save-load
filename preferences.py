# type: ignore 
import json
from os import path

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

    def draw(self, _: Context):
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

    def to_dict(self):
        return {
            "string_pref": self.string_pref,
            "int_pref": self.int_pref,
            "float_pref": self.float_pref,
            "bool_pref": self.bool_pref,
            "color_pref": list(self.color_pref),
            "coordinate_pref": list(self.coordinate_pref),
            "name_number_sets": [
                {
                    "string_prop": item.string_prop,
                    "int_prop": item.int_prop
                }
                for item in self.name_number_sets
            ]
        }

    def from_dict(self, data):
        self.string_pref = data.get("string_pref", "")
        self.int_pref = data.get("int_pref", 0)
        self.float_pref = data.get("float_pref", 0.0)
        self.bool_pref = data.get("bool_pref", False)
        self.color_pref = data.get("color_pref", (0.7, 0.7, 0.7, 1.0))
        self.coordinate_pref = data.get("coordinate_pref", (0.0, 0.0, 0.0))
        self.name_number_sets.clear()

        if "name_number_sets" not in data:
            return
        for item in data.get("name_number_sets", []):
            new_item = self.name_number_sets.add()
            new_item.string_prop = item.get("string_prop", "")
            new_item.int_prop = item.get("int_prop", 0)

    def save(self):
        data = self.to_dict()
        file = path.abspath(path.dirname(__file__) + "/preferences.json")
        with open(file, "w") as file:
            json.dump(data, file, indent=4)
    
    def load(self):
        # check file exists
        file = path.abspath(path.dirname(__file__) + "/preferences.json")
        try:
            with open(file, "r") as file:
                data = json.load(file)
                self.from_dict(data)
        except:
            return None
