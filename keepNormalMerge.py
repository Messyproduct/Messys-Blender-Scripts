import bpy

bpy.ops.object.mode_set(mode='OBJECT')

selection_names = [obj for obj in bpy.context.selected_objects]

for object in selection_names:
    bpy.ops.object.select_all(action='DESELECT')
    main_obj = object
    bpy.context.view_layer.objects.active = main_obj
    main_obj.select_set(True)
    
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":False, "use_automerge_and_split":False})
    nor_obj = bpy.context.active_object

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = main_obj
    main_obj.select_set(True)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(use_sharp_edge_from_normals=True)

    bpy.ops.object.editmode_toggle()
    bpy.ops.object.modifier_add(type='DATA_TRANSFER')
    bpy.context.object.data.use_auto_smooth = True
    bpy.context.object.modifiers["DataTransfer"].object = nor_obj
    bpy.context.object.modifiers["DataTransfer"].use_loop_data = True
    bpy.context.object.modifiers["DataTransfer"].data_types_loops = {'CUSTOM_NORMAL'}
    bpy.context.object.modifiers["DataTransfer"].loop_mapping = 'TOPOLOGY'

    bpy.ops.object.modifier_apply(modifier="DataTransfer")

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = nor_obj
    nor_obj.select_set(True)

    bpy.ops.object.delete()
