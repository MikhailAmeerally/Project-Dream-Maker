class SmartMonster extends Monster {

	constructor(x,y)
	{
		super(document.getElementById("monsterImage").src,"Monster",x,y);
	}

	getValidSteps()
	{
		

		if(document.getElementById((this.x-1)+","+(this.y-1)).src == document.getElementById("playerImage").src)
		{
			return ["NW"];	
		}

		if(document.getElementById((this.x-1)+","+(this.y)).src == document.getElementById("playerImage").src)
		{
			return ["N"];	
		}


		if(document.getElementById((this.x-1)+","+(this.y+1)).src == document.getElementById("playerImage").src)
		{
			return ["NE"];	
		}

		if(document.getElementById((this.x)+","+(this.y-1)).src == document.getElementById("playerImage").src)
		{
			return ["E"];	
		}

		if(document.getElementById((this.x)+","+(this.y+1)).src == document.getElementById("playerImage").src)
		{
			return ["W"];	
		}

		if(document.getElementById((this.x+1)+","+(this.y-1)).src == document.getElementById("playerImage").src)
		{
			return ["SW"];	
		}


		if(document.getElementById((this.x+1)+","+(this.y+1)).src == document.getElementById("playerImage").src)
		{
			return["SE"];	
		}

		if(document.getElementById((this.x+1)+","+(this.y)).src == document.getElementById("playerImage").src)
		{
			return ["S"];	
		}

		return super.getValidSteps();


}
