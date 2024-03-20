shader_type canvas_item;

void vertex() {
    VERTEX.x += sin(TIME + VERTEX.y) * 5.0;
    VERTEX.y += sin(TIME + VERTEX.x) * 5.0;
	
	//sin time + vertex pour faire un effet goute plus stylé que juste grossir
}

