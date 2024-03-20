shader_type canvas_item;

void vertex() {
	// Called for every vertex the material is visible on.
}

void fragment() {
    if (COLOR.r > 0.8 && COLOR.b < 0.2) { // Condition pour cibler une couleur spécifique (doc)
        COLOR.rgb = vec3(0.0, 1.0, 0.0); // Remplace par du vert
    }
}

//void light() {
	// Called for every pixel for every light affecting the CanvasItem.
	// Uncomment to replace the default light processing function with this one.
//}
