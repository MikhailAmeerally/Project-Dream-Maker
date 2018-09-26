
const Blank = require('./Blank.js');
const Wall = require('./Wall.js');
const Monster = require('./Monster.js');
const Player = require('./Player.js');
const Box = require('./Box.js');
const EnvironmentEntity = require('./EnvironmentEntity.js');
const GameEntity = require('./GameEntity.js');

class NewStage {
    constructor(width, height) {

        this._width = width;
        this._height = height;

        this._gameSpace = new Array(this._width);
        for (var i = 0; i < this._height; i++) {
            this._gameSpace[i] = new Array(this._height);
        }

        this._freeSpace = [];

        this._initStage();
    }

    _initStage() {
        for (var row = 0; row < this._height; row++) {
            for (var col = 0; col < this._width; col++) {
                this._gameSpace[col][row] = new Blank(col, row);
                this._addBlank(col, row);
            }
        }
        this._buildWalls();
    }

    _buildWalls() {

        for (var col = 0; col < this._width; col++) {
            
            // Create the top and bottom indices
            var YTOP = 0;
            var YBOT = this._height - 1;

            // Add walls to the gameSpace
            this._gameSpace[col][YTOP] = new Wall(col, YTOP);
            this._gameSpace[col][YBOT] = new Wall(col, YBOT);

            // // Update freespace
            this._updateFreeSpace(col, YTOP);
            this._updateFreeSpace(col, YBOT);

        }
            
        for (var row = 0; row < this._height; row++) {

            // Create left and right indices
            var XLEFT = 0;
            var XRIGHT = this._width - 1;

            // Add walls to gamespace
            this._gameSpace[XLEFT][row] = new Wall(XLEFT, row);
            this._gameSpace[XRIGHT][row] = new Wall(XRIGHT, row);

            // Update freespace
            this._updateFreeSpace(XLEFT, row);
            this._updateFreeSpace(XRIGHT, row);

        }
    }

    _generateMonsters(monsterCount) {

        for (var numMon = 0; numMon < monsterCount; numMon++) {
            
            // Get a random index of fresspace, to randomly put the monster there.
            var randIndex = Math.floor(Math.random() * this._freeSpace.length);
            
            // Grab a set of coordinates from freespace
            var randX = this._freeSpace[randIndex].x;
            var randY = this._freeSpace[randIndex].y;

            // Add the monster on the gamespace
            this._gameSpace[randX][randY] = new Monster(randX, randY);

            this._updateFreeSpace(randX, randY);
        }

    }

    _updateFreeSpace(x, y) {
        this._freeSpace = this._freeSpace.filter(function(coordinates) {
            return (coordinates.x != x || coordinates.y != y);
        });
    }

    _addBlank(x, y) {
        this._freeSpace.push(this._getCoordinate(x, y));
    }

    _getCoordinate(col, row) {
        return {
            x: col,
            y: row
        };
    }

    updateStage() {
        for (var i = 0; i < this._gameSpace.length; i++) {
            for (var j = 0; j < this._gameSpace[i].length; j++) {
                this.draw(this._gameSpace[i][j]);
            }
        }
    }

    draw(gameEntity) {
        // document.getElementById(this._getStageID(gameEntity.getX(), gameEntity.getY())).src = gameEntity.getImageSrc();
    }

    getGameSpace() {
        return this._gameSpace;
    }


}

module.exports = NewStage;