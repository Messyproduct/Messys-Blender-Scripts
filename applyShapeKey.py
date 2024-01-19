import bpy

selection_names = [obj for obj in bpy.context.selected_objects]

for object in selection_names:
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.shape_key_add(from_mix=True)
    bpy.ops.object.shape_key_move(type='TOP')
    bpy.context.object.active_shape_key_index = 0
    bpy.ops.object.shape_key_remove(all=False)
    bpy.ops.object.shape_key_remove(all=True, apply_mix=False)