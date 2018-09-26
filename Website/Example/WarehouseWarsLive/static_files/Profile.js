class Profile extends React.Component 
{
    constructor(props)
    {
        super(props);
        this.state = {name: "", username: this.props.username, email: "", password: "", gender: "", highestScore: 0};
        this.changePassword = this.changePassword.bind(this);
    }

    changePassword(e){
        var newPassword = $("#changePassword").val();
        this.setState({password: newPassword});
        this.props.changePassword(newPassword);
    }

    render()
    {
        var user = this.props.username;
        if(this.state.name == "")
        { //Only get once.
            $.ajax({ 
                method: "POST", 
                url: "/profile/",
                data: {username: user},
                success:function(data)
                {
                    console.log("GOT DATA SUCCESSFULLY!");
                    this.setState({name: data['name'], email: data['email'], password: data['password'],
                                    gender: data['gender'], highestScore: data['highestScore']});
                }.bind(this),
                error:function()
                {
                    console.log("ERROR");
                }
            });
        }
        
        
        return(
            <div className = "myDiv">
                <p> {this.props.errors} </p>
                <h1> Profile </h1>
                <h2> Name: {this.state.name} </h2>
                <h2> Email: {this.state.email} </h2>
                <h2> Username: {this.state.username} </h2>
                <h2> Password: {this.state.password} </h2>
                <h2> Gender: {this.state.gender} </h2>
                <h2> Highest Score: {this.state.highestScore} </h2>
                <input type="password" id="changePassword" placeholder="New Password" />
                <button onClick={this.changePassword}>Change Password </button> <br/> <br/>
                <button onClick={this.props.deleteProfile}> DELETE PROFILE! </button>
            </div>
        );
        
    }
}