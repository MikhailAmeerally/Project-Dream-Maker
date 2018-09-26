class User extends React.Component 
{
    constructor(props)
    {
        super(props);
        this.state = {Login: true, Register: false, Profile: false, Game: false, Lobby: false,
                        username: "", password: "", email: "", name: "", highestScore: 0,
                        gender: "", errors: "", loggedIn: false
                        }
        this.newRegisterClickHandler = this.newRegisterClickHandler.bind(this);
        this.loginClickHandler = this.loginClickHandler.bind(this);
        this.getProfileInformation = this.getProfileInformation.bind(this);
        this.addNewPlayer = this.addNewPlayer.bind(this);
        this.changePassword = this.changePassword.bind(this);
        this.deleteProfile = this.deleteProfile.bind(this);
        this.navigate = this.navigate.bind(this);
	this.playGame = this.playGame.bind(this);
    }


	playGame(e){
		this.setState({Game: false});
	}	



    changePassword(newPassword){

        $.ajax({
            method: "PUT",
            url: "/updatePassword/",
            data: {username: this.state.username, password: newPassword},
            success:function(data){
                console.log("Updated Successfully.");
                this.setState({password: newPassword});
            }.bind(this),
            error:function(){
                console.log("Something went wrong. Could not update.");
                this.setState({errors: "Could not update password."});
            }.bind(this)
        })

        
    }

    loginClickHandler(e){

        if(this.state.username == "")
        {
            this.setState({errors: "Username Required."});
            return;
        }
        else if(this.state.password == "")
        {
            this.setState({errors: "Password Required."});
            return;
        }
        else{

            var user = this.state.username;
            var pass = this.state.password;
            
            $.ajax({ 
                method: "POST", 
                url: "/login/",
                data: {username: user, password: pass},
                success:function(data)
                {
                    
                    this.setState({Login: false, Register: false, Profile: false, Game: true,
                        email: data['email'], name: data['name'], gender: data['gender'] , loggedIn: true, 
                        highestScore: data['highestScore'],errors: ""})
                }.bind(this),
                error:function()
                {
                    console.log("ERROR");
                    this.setState({errors: "Incorrect Email or Password."});
                }.bind(this)
            });
        }
     }

    newRegisterClickHandler(e)
    {
        this.setState({Login: false, Register: true});
    }

    addNewPlayer(e)
    {
        var username = this.state.username;
        var password = this.state.password;
        var email = this.state.email;
        var name = this.state.name;
        var gender = this.state.gender;

        if(name == ""){
            this.setState({errors: "Name Required!"});
            return;
        }

        if(username == ""){
            this.setState({errors: "Username Required!"});
            return;
        }
        if(password == ""){
            this.setState({errors: "Password Required!"});
            return;
        }
        if(email == ""){
            this.setState({errors: "Email Required!"});
            return;
        }

        if(gender == ""){
            this.setState({errors: "Gender Required!"});
            return
        }

        

        else{
            console.log("Registering...");

            $.ajax({ 
                method: "POST", 
                url: "/register/",
                data: {username: this.state.username},
                success:function(data)
                {
                    console.log("Available.");
                    $.ajax({
                        method: "PUT",
                        url: "registerput",
                        data: {username: this.state.username, password: this.state.password, email: this.state.email,
                                name: this.state.name, gender: this.state.gender, highestScore: 0},
                        success:function(data)
                        {
                            console.log("Registered Successfully.");
                            this.setState({Login: false, Register: false, Profile: false,Game: true , errors: "", loggedIn: true});
                        }.bind(this),
                        error:function()
                        {
                            console.log("Could not Register.");
                            this.setState({errors: "Something went wrong."});
                        }
                    })
                }.bind(this),
                error:function()
                {
                    console.log("ERROR");
                    this.setState({errors: "Username Already Taken."});
                }.bind(this)
            });



        }

        
    }

    deleteProfile(e){

        $.ajax({
            method: "DELETE",
            url: "/delete/",
            data: {username: this.state.username},
            success:function(data){
                console.log("Profile Deleted");
                this.setState({Login: true, Register: false, Profile: false, Game: false,
                    username: "", password: "", email: "", name: "", highestScore: 0,
                    gender: "", errors: ""
                    });
            }.bind(this),
            error:function(){
                console.log("Profile not deleted");
                this.setState({errors: "Whoops! Something Went Wrong!!! Not Deleted."});
            }
        })


        
    }

    getProfileInformation()
    {
        var user = this.state.username;
        console.log("Getting profile info");
        
        $.ajax({ 
            method: "POST", 
            url: "/profile/",
            data: {username: user},
            success:function(data)
            {
                console.log("GOT DATA SUCCESSFULLY!");
                return data
            },
            error:function()
            {
                console.log("ERROR");
                return {error: "Profile not in DB!"};
            }
        });
        
    }

    navigate(name,e){

        if(name == "Profile"){
            this.setState({Login: false, Register: false, Game: false, errors: "", Profile: true});
            return;
        }
        if(name == "Logout"){
            this.setState({Login: true, Register: false, Profile: false, Game: false,
                username: "", password: "", email: "", name: "", highestScore: 0,
                gender: "", errors: "", loggedIn: false
                });
            return;
        }
    }

    handleChange(name,e)
    {
        let field = e.target.value;

        if(name == "username")
        {
            this.setState({username: field});
        }
        if(name == "password")
        {
            this.setState({password: field});
        }
        if(name == "email")
        {
            this.setState({email: field});
        }

        if(name == "name"){
            this.setState({name: field});
        }

        if(name == "gender"){
            this.setState({gender: field});
        }

        if(name == "confirm")
        {
            if(e.target.value != this.state.password)
            {
                this.setState({errors: "Passwords must match."});
            }
            else{this.setState({errors: ""});}
        }
    }

    render()
    {
        //console.log(this.state);
        return(
            <div>
		        {(this.state.Game || this.state.Profile || this.state.Lobby || this.state.loggedIn) && 
                <NavBar navigate = {this.navigate.bind(this)}/>} <br/> <br/>
                {this.state.Login && < Login handleChange = {this.handleChange.bind(this)} 
                registerClickHandler={this.newRegisterClickHandler} 
                loginClickHandler={this.loginClickHandler} errors = {this.state.errors}/>}
                {this.state.Register && < Register addMe = {this.addNewPlayer} 
                handleChange = {this.handleChange.bind(this)} errors = {this.state.errors} />}
                {this.state.Profile && < Profile 
                username = {this.state.username} 
                changePassword={this.changePassword}
                deleteProfile = {this.deleteProfile}
                errors = {this.state.errors}/>}
				{this.state.loggedIn && <Play />}
		        {this.state.Game && <GameLobby username = {this.state.username} playGame={this.playGame}/>}
				
            </div>
        )
        
    }
}

ReactDOM.render( <User />, document.getElementById("User"));
