# Agent tools

The agent drives the CAM system through **158 tools** grouped by area. You normally do not
call them yourself — the agent picks the right tool for a request and shows every call in the
chat for approval — but the catalog below tells you what the assistant is capable of.

| Category | Tools |
|----------|-------|
| **Project & lifecycle** | cam_info, cam_status, cam_new_project, cam_open_project, cam_save_project, cam_calculate, cam_simulate |
| **Composite pipelines** | cam_open_and_calculate, cam_calculate_and_save, cam_run_pipeline, cam_scan_project |
| **Operations** | cam_create_operation, cam_select_operation, cam_set_params, cam_get_params, cam_set_safe_level, cam_list_operation_types, cam_reset_toolpath, cam_reset_simulation |
| **Operation parameters** | cam_list_params |
| **Geometry** | cam_import_geometry, cam_list_geometry, cam_assign_geometry, cam_export_selected_to_step, cam_add_hole, cam_add_group, cam_list_job_items, cam_set_job_item |
| **Sketcher** | cam_add_point, cam_add_line, cam_add_normal_line, cam_add_polyline, cam_add_spline |
| **Tools** | cam_list_tools, cam_add_tool, cam_assign_tool, cam_get_tool_properties, cam_set_tool_properties |
| **Machine** | cam_set_machine, cam_list_machine_connectors, cam_setup_workpiece, cam_get_machine_config, cam_set_machine_config, cam_get_approach_return, cam_set_approach_return, cam_set_tool_connector, cam_add_fixture, cam_set_cs |
| **NC code & saving** | cam_generate_nc, cam_save_cldata, cam_save_machining_result |
| **Simulation method** | cam_set_simulation_method, cam_get_simulation_method |
| **Simulation panel** | cam_simulation_goto_error, cam_simulation_get_current_frame, cam_simulation_read_frames, cam_get_tool_position |
| **Macros** | cam_list_macros, cam_macro_schema, cam_create_macro, cam_run_macro, cam_delete_macro |
| **Macro recording** | cam_macro_record_start, cam_macro_record_capture, cam_macro_record_add_step, cam_macro_record_add_recognize_feature, cam_macro_record_status, cam_macro_record_save, cam_macro_record_discard |
| **View** | cam_rotate_view, cam_zoom_all, cam_zoom_to_point, cam_set_work_mode, cam_screenshot, cam_get_visibility, cam_set_visibility |
| **Kinematics** | cam_analyze_kinematics |
| **Utilities** | cam_list_utilities, cam_run_utility |
| **Feeds & speeds** | cam_list_feeds_speeds, cam_query_feeds_speeds, cam_calculate_mrr_toollife, cam_estimate_cycle_time |
| **Documentation** | cam_list_docs, cam_search_docs, cam_read_doc, cam_search_docs_semantic |
| **Feature recognition** | cam_find_features, cam_select_entities |
| **Segmentation (ML)** | cam_brep_classify, cam_smart_override_segment, cam_segment_step, cam_aagnet_segment, cam_cadnet_segment |
| **AI skills** | skill_search, skill_list, skill_update, skill_upload, user_skill_add, user_skill_delete, user_skill_list, user_skill_import |
| **Projects** | project_index, project_search, project_list |
| **History** | conversation_search, conversation_store, conversation_sessions, conversation_cleanup |
| **Standalone** | cam_analyze_stl, cam_compare_result, cam_list_system_data, cam_list_supplement |
| **Export & logs** | cam_export_info, cam_collect_logs |
| **Operator** | ask_human, ask_human_choice |
| **Health** | cam_ping, cam_is_alive, rag_ping |

## Postprocessor development (pp_)

17 tools for driving the postprocessor IDE: open or create a postprocessor, read and edit
its structure and code, compile it, run it over CLData, and manage IDE instances.

| Category | Tools |
|----------|-------|
| **Postprocessor** | pp_open_post, pp_create_post, pp_get_structure, pp_get_code, pp_set_code, pp_delete, pp_get_registers, pp_set_registers, pp_open_cld, pp_translate, pp_run |
| **IDE instances** | pp_launch, pp_instances, pp_select_instance, pp_close, pp_kill |
| **Health** | pp_ping |

## CLData inspection (cld_)

15 tools for inspecting CLData projects: structure, commands, parameters, machine info.

| Category | Tools |
|----------|-------|
| **Projects** | cld_open_project, cld_close_project, cld_list_projects |
| **Structure** | cld_list_files, cld_get_skeleton, cld_get_unique_command_names |
| **Commands** | cld_list_commands, cld_get_command, cld_find_command, cld_command_code |
| **Parameters** | cld_get_parameter, cld_find_parameter, cld_get_project_parameter |
| **Machine & export** | cld_get_machine_info, cld_dump_json |
