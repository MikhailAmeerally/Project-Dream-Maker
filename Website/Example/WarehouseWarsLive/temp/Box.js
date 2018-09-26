const EnvironmentEntity = require('./EnvironmentEntity.js');

class Box extends EnvironmentEntity {
    constructor(x, y, imageSrc) {
        super(x, y, 'icons/emblem-package-2-24.png', "box", true);
    }

    move(xDir, yDir) {
        var nextX = this.getX() + xDir;
        var nextY = this.getY() + yDir;

    }
}

module.exports = Box;
