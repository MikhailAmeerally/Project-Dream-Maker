const GameEntity = require('./GameEntity.js');

class Player extends GameEntity {
    constructor(x, y, imageSource, gameID) {
        super(x, y, 'icons/face-cool-24.png', "player");
        this._gameID = gameID;
        this.dead = false;
    }

    move(xDir, yDir) {
        this.setX(this.getX() + xDir);
        this.setY(this.getY() + yDir);
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
