load=function()
		{
			canvas = document.getElementById("myCanvas");
			context = canvas.getContext("2d");
			canvas.width=window.innerWidth;
			canvas.height=window.innerHeight;
			context.font = "30px Arial";
			context.fillText("Hello World",10,50);
		};

load();
