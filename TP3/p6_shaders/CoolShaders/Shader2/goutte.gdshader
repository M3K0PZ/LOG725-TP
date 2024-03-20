shader_type canvas_item;

void vertex() {
    if (UV.x > 0.2) { // Ajustez cette valeur pour cibler la "partie avant" spécifique
		//Normalized texture coordinates. Range from 0 to 1. source doc
        VERTEX.x += sin(TIME + VERTEX.y) * 5.0;
    }
}
