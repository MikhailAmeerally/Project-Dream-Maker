var WebSocketServer = require('ws').Server
   ,wss = new WebSocketServer({port: 10081});

var messages=[];

var Worlds = {};

const GameWorld = require('./temp/GameWorld.js');

wss.on('close', function() {
    console.log('disconnected');
});

wss.broadcast = function(world){
	for(let ws of world['players']){ 
		ws.send(world['currStage']);
	}

	// Alternatively
	// this.clients.forEach(function (ws){ ws.send(message); });
}

wss.on('connection', function(ws) {

	Worlds['host']['players'].push(ws);

	ws.on('message', function(message) {
		console.log(message);
	});
});

function setup() {
	// Initiate a new game world
	const gameWorld = new GameWorld(0, "stage");

	Worlds['host'] = {
		players: [],
		currStage: JSON.stringify(gameWorld.getCurrentStage())
	};
	
	// Start the game world
	gameWorld.startGame(setInterval(function() {
		var gameSpace = gameWorld.update();
		Worlds['host']['currStage'] = JSON.stringify(gameSpace);
		wss.broadcast(Worlds['host']);
	}, 250));
}

setup();
