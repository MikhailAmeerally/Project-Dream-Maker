class Stage {
    constructor(width, height, id) {
        this._width = width;
        this._height = height;
        this._id = id;

        this._gameSpace = new Array(this._width);        
        for (var i = 0; i < this._height; i++) {
            this._gameSpace[i] = new Array(this._height);
        }

        this._freeSpace = [];

        this.blankImgSrc = document.getElementById('blankImage').src;
        // this.monsterImgSrc = document.getElementById('monsterImage').src;
        // this.boxImgSrc = document.getElementById('boxImage').src;
        // this.playerImgSrc = document.getElementById('playerImage').src;
        // this.wallImgSrc = document.getElementById('wallImage').src;

        this.LEVELS = [1, 2, 3];

        // Create an empty playersList
        // Design: key pair values, with playerID as key, and value to be the actual Player object
        this.playersList = {};

        console.log("Constructing Stage...");

        this._initializeStage();
    }

    // ******* ALL PRIVATE METHODS ******* //

    _getCoordinate(col, row) {
        return {
            x: col,
            y: row
        };
    }

    _initializeStage() {

        var mainStage = '<table>';
    
        for (var row = 0; row < this._height; row++) {
            mainStage += '<tr>';
            for (var col = 0; col < this._width; col++) {
                mainStage += '<td><img src="' + this.blankImgSrc + '" id="'+ this._getStageID(col, row) + '" /></td>';

                this._gameSpace[col][row] = new Blank(col, row);

                // Add that coordinate in the freespace tracking array
                this.addBlank(col, row);
                // this._freeSpace.push(this._getCoordinate(col, row));
            }
        }
        mainStage += '</table>';
        document.getElementById(this._id).innerHTML = mainStage;


        // Build the WALLS of JERICHO
        this._buildWalls();

        // Generate some boxes (will need to be different per world?)
        this._generateBoxes(2);

        // Generate some monsters (generic number or dynamic?)
        this._generateMonsters(5);

        // this.addPlayer("James");

        console.log("Stage initialization complete!");
    }

    _buildWalls() {

        for (var col = 0; col < this._width; col++) {

            // Create the top and bottom indices
            var YTOP = 0;
            var YBOT = this._height - 1;

            // Add walls to the gameSpace
            this._gameSpace[col][YTOP] = new Wall(col, YTOP);
            this._gameSpace[col][YBOT] = new Wall(col, YBOT);

            // Update freespace
            this._updateFreeSpace(col, YTOP);
            this._updateFreeSpace(col, YBOT);

        }

        for (var row = 0; row < this._height; row++) {

            // Create left and right indices
            var XLEFT = 0;
            var XRIGHT = this._width - 1;

            // Add walls to gamespace
            this._gameSpace[XLEFT][row] = new Wall(XLEFT, row, this.wallImgSrc);
            this._gameSpace[XRIGHT][row] = new Wall(XRIGHT, row, this.wallImgSrc);

            // Update freespace
            this._updateFreeSpace(XLEFT, row);
            this._updateFreeSpace(XRIGHT, row);

        }

        console.log("Building game walls...");
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

        console.log("Generating monsters...");
    }

    _generateBoxes(level) {
        if (!this.LEVELS.includes(level)) {
            level = 1;
        }

        var maxBoxCount = (Math.ceil((this._width - 2) * (this._height - 2)) * this.LEVELS[level - 1]*1.0 / 10) - 1;

        for (var boxCount = 0; boxCount < maxBoxCount; boxCount++) {
            var randIndex = Math.floor(Math.random() * this._freeSpace.length);

            var randX = this._freeSpace[randIndex].x;
            var randY = this._freeSpace[randIndex].y;

            // Create a box and add it to the gamespace
            this._gameSpace[randX][randY] = new Box(randX, randY);

            // Update the free spaces
            this._updateFreeSpace(randX, randY);
        }
    }

    // Changes the freespace by removing any of the coordinates that is still in the freeSpace
    _updateFreeSpace(x, y) {
        this._freeSpace = this._freeSpace.filter(function(coordinates) {
            return (coordinates.x != x || coordinates.y != y);
        });
    }

    _getStageID(x, y) {
        return "stageID_" + x + "_" + y;
    }

    // ******* END PRIVATE METHODS ******* //

    // ******* ALL PUBLIC METHODS ******* //
    updateStage() {
        for (var i = 0; i < this._gameSpace.length; i++) {
            for (var j = 0; j < this._gameSpace[i].length; j++) {
                this.draw(this._gameSpace[i][j]);
            }
        }
    }

    getEmptySpace() {

        var emptySpace = [];

        for (var x = 0; x < this._gameSpace.length; x++) {
            for (var y = 0; y < this._gameSpace[x].length; y++) {
                if (this._gameSpace[x][y].getType() == "blank") {
                    emptySpace.push(this._getCoordinate(x, y));
                    // return;
                }
            }
        }

        return emptySpace;
    }

    getGameSpace() {
        return this._gameSpace;
    }

    addPlayer(playerID, playerObj) {
        this.playersList[playerID] = playerObj;
    }

    addBlank(x, y) {
        this._freeSpace.push(this._getCoordinate(x, y));
    }

    // Changes the gameSpace given the x and y coordinate and the gameEntity to put there
    changeGameSpace(x, y, gameEntity) {
        this._gameSpace[x][y] = gameEntity;
    }

    draw(gameEntity) {
        document.getElementById(this._getStageID(gameEntity.getX(), gameEntity.getY())).src = gameEntity.getImageSrc();
    }

    // ******* END PUBLIC METHODS ******* // 

} 
