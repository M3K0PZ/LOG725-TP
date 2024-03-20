shader_type canvas_item;

void vertex() {
    VERTEX.y += sin(TIME + VERTEX.x) * 5.0; // Transformation en Y style goutte
}

void fragment() {
	
    COLOR.rgb = mix(COLOR.rgb, vec3(1.0, 0.0, 0.0), sin(TIME)); // Mélange avec du rouge selon le temps 
}
