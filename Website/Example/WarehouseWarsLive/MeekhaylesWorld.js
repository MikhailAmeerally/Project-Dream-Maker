var WebSocketServer = require('ws').Server
   ,wss = new WebSocketServer({port: 10081});

var Worlds = {};

const GameWorld = require('./static_files/GameWorld.js');
const gameWorld = new GameWorld(0, 'stage');

wss.on('close', function() {
    console.log('disconnected');
});

// The broadcast method
// Sends each player a copy of the world that is being updated
wss.broadcast = function(world){
	for(let ws of world['players']){ 

        // Check to see if the player is open
        if (ws.readyState === ws.OPEN) {
            
            // Send the world to all clients
            ws.send(world['currStage']);
        }
	}
}

wss.on('connection', function(ws) {

    // Add the player to the Worlds host
	Worlds['host']['players'].push(ws);

    // 
	ws.on('message', function(message) {
        var data = JSON.parse(message);

        // Check the request value
        if (data["request"] == "move") {

            // move player in world
            gameWorld.movePlayer(data["username"], data["direction"]);
            var newGS = gameWorld.getCurrentStage();
            Worlds['host']['currStage'] = JSON.stringify(newGS);
            wss.broadcast(Worlds['host']);

        } else if (data["request"] == "add") {

            // if the request is add, add the player into the world
            gameWorld.addPlayer(data["username"]);

        }
    });
});

function setup() {

	Worlds['host'] = {
		players: [],
		currStage: JSON.stringify(gameWorld.getCurrentStage())
	};
	
	// Start the game world
	gameWorld.startGame(setInterval(function() {

        // Returns a 2D array of the gamespace
		var gameSpace = gameWorld.update();

        // Puts the JSON.stringified version of that gameSpace
		Worlds['host']['currStage'] = JSON.stringify(gameSpace);

        // Broadcast the worlds to all the clients
		wss.broadcast(Worlds['host']);
	}, 250));
}

setup();
