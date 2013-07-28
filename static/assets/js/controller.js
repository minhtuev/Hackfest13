// JQuery code for controller.

// case 'wasd':
up_key = 87
down_key = 83
left_key = 65
right_key = 68

$(document).keydown(function(event){
	switch (event.keyCode) {
		case left_key:
		$("#currentKey").text("Left");
		//left();
		break;
		case up_key:
		$("#currentKey").text("Up");
		//up();
		break;
		case right_key:
		$("#currentKey").text("Right");
		//right();
		break;
		case down_key:
		$("#currentKey").text("Down");
		//down();
		break;
		case 38:
		break;
	}});


// case 'arrows':
// up_key = 38
// down_key = 40
// left_key = 37
// right_key = 39
// break;
// case 'wasd':
// up_key = 87
// down_key = 83
// left_key = 65
// right_key = 68
// break;
// case 'keypad':
// up_key = 104
// down_key = 98
// left_key = 100
// right_key = 102
// break;
// case 'ijkl':
// up_key = 73
// down_key = 75
// left_key = 74
// right_key = 76
// break;