"""Add triangulate modifier to selected objects"""

import bpy

for ob in bpy.context.selectable_objects:
    triangle = False

    mods = ob.modifiers
    for mod in mods:
        if mod.type == 'TRIANGULATE':
            triangle = True

    if triangle == False:
        ob.modifiers.new(type="TRIANGULATE", name="Export Tris")
