/* Name: Daniel-TheProgrammer
   File: draw_Clock.js
*/

// Takes in 2 ints, returns a number between minTime and maxTime
function getRandomTime(minTime, maxTime){
	return Math.floor((Math.random() * maxTime) + minTime);
}

// Returns an hour, adjusted to be put on the analog clock
function adjustHour(hour, minute, second) {
    hour = (hour*Math.PI/6) + (minute*Math.PI/(6*60)) + (second*Math.PI/(360*60));
 	return hour
}

// Returns a minute, adjusted to be put on the analog clock
function adjustMinute(minute, second) {
	minute = (minute*Math.PI/30) + (second*Math.PI/(30*60));
	return minute;
}

// Returns a second, adjusted to be put on the analog clock
function adjustSecond(second) {
	second=(second*Math.PI/30);
	return second;
}

// Input: context, float pos (already transformed into correct angle), int length, int width
// Draws a hand on the clock at the correct position
function drawHand(context, pos, length, width) {
	context.beginPath(); // starting a new line
	context.lineWidth = width; // how wide the hand is
	context.lineCap = "round"; // round at the ends of the hand
	context.moveTo(0,0); // start of hand
	context.rotate(pos); // rotate to the correct position for the hand
	context.lineTo(0, -length); // end of hand
	context.stroke(); // Draw it
	context.rotate(-pos); // reset rotation
}

// Input: context, int radius
// Gets a random time for each hand (hour, minute, second) and draw the hands on the clock
function drawTime(context, radius, hr, min, sec){
	hr = adjustHour(hr, min, sec);
	min = adjustMinute(min, sec);
	sec = adjustSecond(sec);

	drawHand(context, hr, radius*0.5, radius*0.07); // Draw hour hand, short
	drawHand(context, min, radius*0.8, radius*0.07); // Draw minute hand, longer
//  drawHand(context, sec, radius*0.9, radius*0.02); // Draw second hand, longest and thin
}

// Input: context, int radius
// Draws the numbers on the clock
function drawNumbers(context, radius) {
	var angle;
	context.font = radius*0.15 + "px arial"; // font size and type
	context.textBaseline="middle";
	context.textAlign="center";

	// Draw the numbers from 1 to 12 on the clock
	for(var num = 1; num < 13; num++){
		angle = num * Math.PI / 6; // correct angle for writing the number
		context.rotate(angle);
		context.translate(0, -radius*0.85);
		context.rotate(-angle);
		context.fillText(num.toString(), 0, 0); // write the number
		context.rotate(angle);
		context.translate(0, radius*0.85); // reset translation
		context.rotate(-angle);
	}
}

// Input: context, int radius
// Drawing the style of the clock
function drawFace(context, radius) {
	var gradient;
	context.beginPath();
	context.arc(0, 0, radius, 0, 2*Math.PI);
	context.fillStyle = 'white'; // clock is white
	context.fill();

	/* Setting up the outside of the clock */
	gradient = context.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
	gradient.addColorStop(0, '#333'); // hand colors become black
	// outside of the clock
	gradient.addColorStop(0.5, 'white'); 
	gradient.addColorStop(1, '#333');
	context.strokeStyle = gradient;
	context.lineWidth = radius*0.1;
	context.stroke(); // draw the 

	/* Setting up middle of the clock */
	context.beginPath();
	context.arc(0, 0, radius*0.1, 0, 2*Math.PI);
	context.fillStyle = '#333';
	context.fill();
}

// Draw the clock onto the canvas
function drawClock() {
	drawFace(context, radius);
	drawNumbers(context, radius);
	drawTime(context, radius, hour, minute, second); // takes in global hour, minute, second, but doesn't change them
}

// Create a new clock, with new values for hour, minute, and second
function getNewClock() {
	hour = getRandomTime(1, 12);
	minute = getRandomTime(0, 11) * 5;
	second = 0;
	drawClock();
}

var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d"); // get methods for canvas
var radius = canvas.height / 2;
var hour, minute, second; // for the clock

context.translate(radius, radius); // Starting everything at the middle of the canvas
radius = radius * 0.90;
getNewClock(); // Starting clock