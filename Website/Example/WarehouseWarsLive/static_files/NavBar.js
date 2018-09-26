
class NavBar extends React.Component 
{
    constructor(props){
        super(props);
    }

    render(){
        return(
        <ul>
            <NavItem name="Game" navigate= {this.props.navigate} />
            <NavItem name="Profile" navigate = {this.props.navigate}/>
            <NavItem name="Logout" navigate = {this.props.navigate}/>
        </ul>
        );
    }
}