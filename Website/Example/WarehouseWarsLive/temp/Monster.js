const GameEntity = require('./GameEntity.js');
class Monster extends GameEntity {
    constructor(x, y) {
        super(x, y, 'icons/face-devil-grin-24.png', "monster");
    }

    move(xDir, yDir) {

    }

    setLocation(x, y) {
        
    }

}

module.exports = Monster;