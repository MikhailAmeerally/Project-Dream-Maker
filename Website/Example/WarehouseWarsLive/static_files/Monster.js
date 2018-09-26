const GameEntity = require('./GameEntity.js');
const Blank = require('./Blank.js');

class Monster extends GameEntity {
    constructor(x, y) {
        super(x, y, 'icons/face-devil-grin-24.png', "monster");
        
        this.xVals = [-1, 0, 1, -1, 1, -1, 0, 1];
        this.yVals = [-1, -1, -1, 0, 0, 1, 1, 1];
        this.moveLen = this.xVals.length;
    }

    death() {
        console.log("Monster dead");
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
            gameSpace[this.getX()][this.getY()] = this;
        }
    }

    moveRandomly(stage) {

        // Random index
        var randIndex = Math.floor(Math.random() * this.moveLen);
        var randX = this.xVals[randIndex];
        var randY = this.yVals[randIndex];

        this.move(randX, randY, stage);
    }

    checkSurroundings(stage) {

    }

}

module.exports = Monster;
