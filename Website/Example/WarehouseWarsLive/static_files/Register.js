class Register extends React.Component {
    constructor(props) {
        super(props);
        this.addMe = this.addMe.bind(this);
        
    }
    
    handleChange(name,e)
    {
        this.props.handleChange(name,e);
    }


    addMe(e)
    {
        this.props.addMe(e);
    }

    render(props){
        return (  
            <div className="myDiv" > 
                <p> {this.props.errors} </p>

                    <input type="text" id="name" placeholder="John Appleseed" onChange={this.handleChange.bind(this,"name")} required /> <br/>
                    <input type="text" id="username" placeholder="Username" onChange= {this.handleChange.bind(this,"username")} required/> <br/>
                    <input type="password" id="password" placeholder="Password" onChange= {this.handleChange.bind(this,"password")}  required/> <br/>
                    <input type="password" id="confirm" placeholder="Confirm Password" onChange= {this.handleChange.bind(this,"confirm")}  required /> <br/>
                    <input type="email" id="email" placeholder="Email" onChange= {this.handleChange.bind(this,"email")} required /> <br/>


                    <input className="option-input" type="radio" name="gender" value="Male" onClick={this.handleChange.bind(this,"gender")} required />Male <br/>
                    <input className="option-input" type="radio" name="gender" value="Female" onClick={this.handleChange.bind(this,"gender")} required />Female <br/>
                    <input className="option-input" type="radio" name="gender" value="Other" onClick={this.handleChange.bind(this,"gender")} required />  Other <br/> <br/>
                    
                    <button className="pulse" id="Register" onClick={this.addMe} disabled = {false} >Register</button>
            </div>
        )
    }
}
//Do not render to DOM because this is part of parent.