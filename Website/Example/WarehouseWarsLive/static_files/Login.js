class Login extends React.Component {
    constructor(props) {
        super(props);
    }


    handleChange(name,e)
    {
        this.props.handleChange(name,e);
    }

    

    
    render(){
        return (  
            <div className = "myDiv" > 
                <p> {this.props.errors} </p>
                <input type="text" id="username" placeholder="Username" onChange= {this.handleChange.bind(this,"username")} required/> <br/>
                <input type="password" id="password" placeholder="Password" onChange= {this.handleChange.bind(this,"password")} required/> <br/>
                <br/>
                <button className="pulse" id="Login" value="Login" onClick={this.props.loginClickHandler} > Login </button>
                <button className="pulse" id="Register" value="Register" onClick={this.props.registerClickHandler}> Register </button>
            </div>
        );
    }
}
//Do not render to DOM because this is part of parent.x
//ReactDOM.render( <Login />, document.getElementById("Login"));
//