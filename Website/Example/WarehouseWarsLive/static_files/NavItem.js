class NavItem extends React.Component
{
    constructor(props){
        super(props);
        

    }

    handleClick(name,e){
        console.log("Clicked Me!");
        this.props.navigate(name);
    }

    render(){
        return(
        <li> <a onClick={this.handleClick.bind(this,this.props.name)}> {this.props.name} </a> </li>
        )
    }
}