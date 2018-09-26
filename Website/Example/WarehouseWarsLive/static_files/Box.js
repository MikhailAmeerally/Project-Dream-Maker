const EnvironmentEntity = require('./EnvironmentEntity.js');
const Blank = require('./Blank.js');

class Box extends EnvironmentEntity {
    constructor(x, y, imageSrc) {
        super(x, y, 'icons/emblem-package-2-24.png', "box", true);
    }

    move(xDir, yDir, stage) {

        var gameSpace = stage.getGameSpace();
        
        var newX = this.getX() + xDir;
        var newY = this.getY() + yDir;

        if (gameSpace[newX][newY].getType() == "blank") {

            console.log(gameSpace[this.getX()][this.getY()]);
            
            // Change curr gameSpace to blank
            gameSpace[this.getX()][this.getY()] = new Blank(this.getX(), this.getY());

            this.setX(newX);
            this.setY(newY);

            // Change the gameSpace to the new monster location
            gameSpace[this.getX()][this.getY()] = this;

        } else if (gameSpace[newX][newY].getType() == "box") {

            // Move the box
            gameSpace[newX][newY].move(xDir, yDir, stage);

            if (gameSpace[newX][newY].getType() == "blank") {
                this.move(xDir, yDir, stage);
            }

        }
    }
}

module.exports = Box;
