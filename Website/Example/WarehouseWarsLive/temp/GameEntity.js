class GameEntity {

    // Have constructor set x, y, and image sources
    constructor(x, y, imageSrc, type) {
        this._x = x;
        this._y = y;
        this._imageSrc = imageSrc;
        this._type = type;

    }

    // Setter and getter for x value
    getX() {
        return this._x;
    }

    setX(x) {
        this._x = x;
    }

    // Setter and getter for y value
    getY() {
        return this._y;
    }

    setY(y) {
        this._y = y;
    }

    // Setter and getter for image source
    getImageSrc() {
        return this._imageSrc;
    }

    setImageSrc(imgSrc) {
        this._imageSrc = imgSrc;
    }

    getType() {
        return this._type;
    }

}

module.exports = GameEntity;