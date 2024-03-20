shader_type canvas_item;

uniform float threshold = 0.5; // Variable pour l'animation

void fragment() {
    if (UV.x < threshold * sin(TIME)) { //comment trouver la zone a colorier 
        COLOR.rgb = vec3(0.0, 1.0, 0.0); // Couleur verte
    }
}
