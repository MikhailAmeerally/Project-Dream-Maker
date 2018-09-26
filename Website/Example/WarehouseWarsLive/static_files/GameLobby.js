class GameLobby extends React.Component
{

	constructor(props)
	{
		super(props);
		this.socket = null;
		this.initializeConnection();
		this.addPlayer = this.addPlayer.bind(this);
	}		

    draw(gameStage) {
        var mainStage = '<table>';

         for (var row = 0; row < gameStage.length; row++) {
             mainStage += '<tr>';
             for (var col = 0; col < gameStage[row].length; col++) {
                 mainStage += '<td><img src="' + gameStage[col][row]._imageSrc + '"/></td>';
             }
         }
         mainStage += '</table>';
         document.getElementById("stage").innerHTML = mainStage;
    }

	initializeConnection()
	{
		// Sockets of the player
		var socket = null;
		socket = new WebSocket('ws://cslinux.utm.utoronto.ca:10081')

		

			socket.onopen = function(event) {
				console.log("Connected.");
			};

			socket.onclose = function(event) {
				alert("Host closed the server.");
			};

			socket.onmessage =(event) =>  {
				var eventData = JSON.parse(event.data);
				this.draw(eventData);
			};


			this.socket = socket;
			console.log(this.socket);

			addEventListener('keydown', (keyEvent) => {
				var keyCode = keyEvent.keyCode;
				var dir = null;
                console.log(keyCode);

				switch(keyCode){
					case 65:
						//LEFT
						dir = "W";
                        break;
					case 87:
						//UP
						dir = "N";
                        break;
					case 68:
						//RIGHT
						dir = "E";
                        break;
					case 88:
						//DOWN
						dir = "S";
                        break;
					case 81:
						//TOPLEFT
						dir = "NW";
                        break;
					case 69:
						//TOPRIGHT
						dir = "NE";
                        break;
					case 67:
						//BOTTOMRIGHT
						dir = "SE";
                        break;
					case 90:
						//BOTTOMLEFT
						dir = "SW";
                        break;
					default:
						console.log("default");
                        break;

				}

				if(dir != null)
				{
					socket.send(JSON.stringify({"request": "move", "direction": dir, "username": this.props.username}));
				}
			});
	}
	

addPlayer(e){
	this.props.playGame(e);
	this.socket.send(JSON.stringify({"request": "add", "username": this.props.username}));
}


	render()
	{
		return(
			<div className="myDiv">
				<h2> Game Lobby </h2>

				<button onClick={this.addPlayer}> Join Game! </button>
			</div>
		);
	}

}
