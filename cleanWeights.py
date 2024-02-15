import bpy

selection_names = [obj for obj in bpy.context.selected_objects]
cleanLimit= .01

for object in selection_names:
    bpy.context.view_layer.objects.active = object
    
    bpy.ops.object.vertex_group_clean(group_select_mode='BONE_DEFORM', limit=cleanLimit, keep_single=True)
    bpy.ops.object.vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)
    bpy.ops.object.vertex_group_limit_total()
    bpy.ops.object.vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)