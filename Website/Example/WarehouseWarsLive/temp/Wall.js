const EnvironmentEntity = require('./EnvironmentEntity.js');
class Wall extends EnvironmentEntity {
    constructor(x, y) {
        super(x, y, 'icons/wall.jpeg', "wall", false);
    }
}

module.exports = Wall;
