class Play extends React.Component
{
    constructor(props){
        super(props);
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

    render(){
        return(
            <div className="myDiv" id="stage"> </div>
        );
    }
}
