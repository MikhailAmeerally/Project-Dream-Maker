const NewStage = require('./NewStage.js');
const Blank = require('./Blank.js');
const Player = require('./Player.js');
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

        // Get the gameSpace for the stage
        var gameSpace = this.gameStage.getGameSpace();

        var coordinates = this.gameStage.getFreeSpace();
        
        // Set the gameSpace
        gameSpace[coordinates.x][coordinates.y] = new Player(coordinates.x, coordinates.y, playerID);

        // Add player to players list
        this.playersList[playerID] = gameSpace[coordinates.x][coordinates.y];

    }

    killPlayer(playerID) {
    }

    movePlayer(playerID, direction) {

        // Pull out the Player object
        var currPlayer = this.playersList[playerID];
	
	if (currPlayer == undefined) {
		console.log(playerID);
		return;
	}

        var index = null;

        if (direction == "NW") index = 0;
        else if (direction == "N") index = 1;
        else if (direction == "NE") index = 2; 
        else if (direction == "W") index = 3;
        else if (direction == "E") index = 4; 
        else if (direction == "SW") index = 5;
        else if (direction == "S") index = 6;
        else if (direction == "SE") index = 7;
        
        currPlayer.move(this.xVals[index], this.yVals[index], this.gameStage);

    }


}

module.exports = GameWorld;
