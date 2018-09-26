const EnvironmentEntity = require('./EnvironmentEntity.js');

class Blank extends EnvironmentEntity {
    // Creating the blank
    constructor(x, y) {
        super(x, y, 'icons/blank.gif', "blank", true);
    }
}

module.exports = Blank;
