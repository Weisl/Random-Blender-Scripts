"""Force selected object materials not to use nodes"""
import bpy

for obj in bpy.context.selected_objects:
    if obj.type != 'EMPTY':
        obj.active_material.use_nodes = False
