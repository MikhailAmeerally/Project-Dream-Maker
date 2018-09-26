const GameEntity = require('./GameEntity.js');
const Blank = require('./Blank.js');

class Player extends GameEntity {
    constructor(x, y, gameID) {
        super(x, y, 'icons/face-cool-24.png', "player");
        this._gameID = gameID;
        this.dead = false;

        this.xVals = [-1, 0, 1, -1, 1, -1, 0, 1];
        this.yVals = [-1, -1, -1, 0, 0, 1, 1, 1];
    }
    
    move(xDir, yDir, stage) {

        var gameSpace = stage.getGameSpace();
        
        var newX = this.getX() + xDir;
        var newY = this.getY() + yDir;

        if (gameSpace[newX][newY].getType() == "blank") {

            // Change curr gameSpace to blank
            gameSpace[this.getX()][this.getY()] = new Blank(this.getX(), this.getY());

            this.setX(newX);
            this.setY(newY);

            // Change the gameSpace to the new monster location
            gameSpace[newX][newY] = this;

        } else if (gameSpace[newX][newY].getType() == "box") {

            // Move the box
            gameSpace[newX][newY].move(xDir, yDir, stage);

            if (gameSpace[newX][newY].getType() == "blank") {
                this.move(xDir, yDir, stage);
            }
        } else if (gameSpace[newX][newY].getType() == "monster") {
            this.kill();
        }
    }

    setLocation(x, y) {
        this.setX(x);
        this.setY(y);
    }

    setGameID(gameID) {
        this._gameID = gameID;
    }

    getGameID() {
        return this._gameID;
    }

    kill() {
        this.dead = true;
    }

    isDead() {
        return this.dead;
    }
}

module.exports = Player;
