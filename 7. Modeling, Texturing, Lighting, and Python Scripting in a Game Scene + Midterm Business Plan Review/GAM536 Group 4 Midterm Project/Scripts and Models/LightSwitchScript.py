import bpy

def setup_day_night_lighting():
    scene = bpy.context.scene
    
    # Create custom property if not present
    if "lighting_mode" not in scene:
        scene["lighting_mode"] = "DAY"

    # Remove old lights if they exist
    for obj in bpy.data.objects:
        if obj.name.startswith("Day_Light") or obj.name.startswith("Night_Light"):
            bpy.data.objects.remove(obj, do_unlink=True)

    # Create Day Light (Sun)
    day_light = bpy.data.lights.new(name="Day_Light", type='SUN')
    day_light_obj = bpy.data.objects.new(name="Day_Light", object_data=day_light)
    bpy.context.collection.objects.link(day_light_obj)
    day_light_obj.rotation_euler = (0.785, 0, 0.785)  # 45 degrees down
    day_light.energy = 5.0
    day_light.color = (1.0, 0.95, 0.8)

    # Create Night Light (Point)
    night_light = bpy.data.lights.new(name="Night_Light", type='POINT')
    night_light_obj = bpy.data.objects.new(name="Night_Light", object_data=night_light)
    bpy.context.collection.objects.link(night_light_obj)
    night_light_obj.location = (0, 0, 5)
    night_light.energy = 50.0
    night_light.color = (0.4, 0.6, 1.0)

    # Hide one of them based on state
    if scene["lighting_mode"] == "DAY":
        night_light_obj.hide_viewport = True
        night_light_obj.hide_render = True
    else:
        day_light_obj.hide_viewport = True
        day_light_obj.hide_render = True


def toggle_lighting():
    scene = bpy.context.scene

    # Update toggle state
    current_mode = scene.get("lighting_mode", "DAY")
    new_mode = "NIGHT" if current_mode == "DAY" else "DAY"
    scene["lighting_mode"] = new_mode

    # Toggle visibility
    for obj in bpy.data.objects:
        if obj.name == "Day_Light":
            obj.hide_viewport = (new_mode == "NIGHT")
            obj.hide_render = (new_mode == "NIGHT")
        if obj.name == "Night_Light":
            obj.hide_viewport = (new_mode == "DAY")
            obj.hide_render = (new_mode == "DAY")

    print(f"Switched to {new_mode} lighting.")

# Run setup once (creates lights if not present)
setup_day_night_lighting()

# Toggle lighting every time the script runs
toggle_lighting()