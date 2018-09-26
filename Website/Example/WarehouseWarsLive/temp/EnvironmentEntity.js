const GameEntity = require('./GameEntity.js');

class EnvironmentEntity extends GameEntity {

    // Create the constructor for a GameEnvironment item
    constructor(x, y, imageSrc, type, moveable) {
        super(x, y, imageSrc, type);
        
        // A boolean to check if the environment entity is 
        this._moveable = moveable;
    }

    // Set the moveable boolean value to either true or false
    setMoveable(moveable) {
        if (typeof moveable === typeof true) {
            this._moveable = moveable;
        }
    }

    // The getter function for the moveabilty of an EnvironmentEntity
    isMoveable() {
        return this._moveable;
    }
}

module.exports = EnvironmentEntity;
