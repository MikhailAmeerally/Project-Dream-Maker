const NewStage = require('./NewStage.js');
class GameWorld {

    constructor(worldNum, stageID) {

        this.deathInterval = null;
        this.refreshRate = null;
        this.worldNum = worldNum;

        this.xVals = [-1, 0, 1, -1, 1, -1, 0, 1];
        this.yVals = [-1, -1, -1, 0, 0, 1, 1, 1];

        this.gameStage = new NewStage(20, 20);

        this.playersList = {};
    }

    startGame(interval) {

        this.addPlayer("James");

        // An on running death interval that checks if a player has died
        this.deathInterval = setInterval(function() {

        }, 50);

        // This is the game's refresh rate
        this.refreshRate = interval;
    }

    update() {
        this.gameStage.updateStage();
        return this.getCurrentStage();
    }

    getCurrentStage() {

        return this.gameStage.getGameSpace();
    }

    endGame() {

        // Clear the intervals
        clearInterval(this.deathInterval);
        clearInterval(this.refreshRate);

    }

    addPlayer(playerID) {

        console.log("Adding player...");

        // // Get the gameSpace for the stage
        // var gameSpace = this.gameStage.getGameSpace();
        
        // // Get the emptySpace for the stage
        // var emptySpace = this.gameStage.getEmptySpace();
        
        // // Get a random index from emptySpace
        // var randIndex = Math.floor(Math.random() * emptySpace.length);
                
        // // Get the coordinates
        // var randX = emptySpace[randIndex].x;
        // var randY = emptySpace[randIndex].y;
        
        // // Add a new player
        // gameSpace[randX][randY] = new Player(randX, randY, playerID);
        
        // // Add player to players list
        // this.playersList[playerID] = gameSpace[randX][randY];

        // // add the player to the gameStage's list of players
        // this.gameStage.addPlayer(playerID, gameSpace[randX][randY]);
    }

    killPlayer(playerID) {
    }

    movePlayer(playerID) {

        // Pull out the Player object
        var currPlayer = this.playersList[playerID];

        // if (keyCode == 'q') {
        //     var nextActor = gameSpace[][];
        // }

        // if (keyCode == 'q') this.player.move(-1, -1);
		// else if (keyCode == 'w') this.player.move(0, -1);
		// else if (keyCode == 'e') this.player.move(1, -1);
		// else if (keyCode == 'a') this.player.move(-1, 0);
		// else if (keyCode == 'd') this.player.move(1, 0);
		// else if (keyCode == 'z') this.player.move(-1, 1);
		// else if (keyCode == 'x') this.player.move(0, 1);
		// else if (keyCode == 'c') this.player.move(1, 1);

        // Change the player's coordinates

    }


}

module.exports = GameWorld;