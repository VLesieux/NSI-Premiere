


$(function() {

var plateau={a1:57,b1:58,c1:59,d1:60,e1:61,f1:62,g1:63,h1:64,a2:49,b2:50,c2:51,d2:52,e2:53,f2:54,g2:55,h2:56,a3:41,b3:42,c3:43,d3:44,e3:45,f3:46,g3:47,h3:48,a4:33,b4:34,c4:35,d4:36,e4:37,f4:38,g4:39,h4:40,a5:25,b5:26,c5:27,d5:28,e5:29,f5:40,g5:31,h5:32,a6:17,b6:18,c6:19,d6:20,e6:21,f6:22,g6:23,h6:24,a7:9,b7:10,c7:11,d7:12,e7:13,f7:14,g7:15,h7:16,a8:1,b8:2,c8:3,d8:4,e8:5,f8:6,g8:7,h8:8}




console.log(plateau["g7"])


var historique=[];


document.getElementById('colonnes').innerHTML = "&nbsp;a b c d e f g h" ;
document.getElementById('lignes').innerHTML = "<br><br>8<br><br><br><br>7<br><br><br><br>6<br><br><br><br>5<br><br><br><br>4<br><br><br><br>3<br><br><br><br>2<br><br><br><br>1" ;


document.getElementById("left").addEventListener("click", gauche);
document.getElementById("right").addEventListener("click", droite);




document.getElementById('file').onchange = function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){
    // Entire file
    console.log(this.result);

    // By lines
    var lines = this.result.split('\n');
    

date=lines[2]

console.log(date)
white=lines[4]
black=lines[5]

console.log(white)
console.log(black)

historique=""
for(var line = 10; line < lines.length; line++){
historique+=lines[line]
    }

historique=historique.replaceAll('\r',' ');
console.log(historique)

historique=historique.split(' ');

console.log(historique)
  };
  reader.readAsText(file);
};




//****************cavalier blanc_g

function Cavalier_blanc_g() {

this.positions="";
this.case=58;
this.nom="cavalier_blanc_g";

}

cavalier_blanc_g=new Cavalier_blanc_g();

//****************cavalier blanc_d

function Cavalier_blanc_d() {

this.positions="";
this.case=63;
this.nom="cavalier_blanc_d";

}

cavalier_blanc_d=new Cavalier_blanc_d();

//****************fou noir_g

function Fou_noir_g() {

this.positions="";
this.case=59;
this.nom="fou_noir_g";

}

fou_noir_g=new Fou_noir_g();

//****************fou noir_d

function Fou_noir_d() {

this.positions="";
this.case=62;
this.nom="fou_noir_d";

}

fou_noir_d=new Fou_noir_d();

//****************fou blanc_g

function Fou_blanc_g() {

this.positions="";
this.case=59;
this.nom="fou_blanc_g";

}

fou_blanc_g=new Fou_blanc_g();

//****************fou blanc_d

function Fou_blanc_d() {

this.positions="";
this.case=62;
this.nom="fou_blanc_d";

}

fou_blanc_d=new Fou_blanc_d();


//****************roi blanc

function Roi_blanc() {

this.nom="roi_blanc";
this.positions="";
this.case=61;

}

roi_blanc=new Roi_blanc();

//****************pion blanc 53

function Pion_blanc_53() {

this.nom="pion_blanc_53";
this.positions="";
this.case=53;

}

pion_blanc_53=new Pion_blanc_53();

//****************pion blanc 53

function Pion_blanc_49() {

this.nom="pion_blanc_49";
this.positions="";
this.case=49;

}

pion_blanc_49=new Pion_blanc_49();

//****************pion blanc 50

function Pion_blanc_50() {

this.nom="pion_blanc_50";
this.positions="";
this.case=50;

}

pion_blanc_50=new Pion_blanc_50();

//****************pion blanc 51

function Pion_blanc_51() {

this.nom="pion_blanc_51";
this.positions="";
this.case=51;

}

pion_blanc_51=new Pion_blanc_51();

//****************pion blanc 52

function Pion_blanc_52() {

this.nom="pion_blanc_52";
this.positions="";
this.case=52;

}

pion_blanc_52=new Pion_blanc_52();

//****************pion blanc 54

function Pion_blanc_54() {

this.nom="pion_blanc_54";
this.positions="";
this.case=54;

}

pion_blanc_54=new Pion_blanc_54();

//****************pion blanc 55

function Pion_blanc_55() {

this.nom="pion_blanc_55";
this.positions="";
this.case=55;

}

pion_blanc_55=new Pion_blanc_55();

//****************pion blanc 56

function Pion_blanc_56() {

this.nom="pion_blanc_56";
this.positions="";
this.case=56;

}

pion_blanc_56=new Pion_blanc_56();

//****************cavalier noirg

function Cavalier_noir_g() {

this.nom="cavalier_noir_g";
this.positions="";
this.case=63;

}

cavalier_noir_g=new Cavalier_noir_g();

//****************cavalier noird

function Cavalier_noir_d() {

this.nom="cavalier_noir_d";
this.positions="";
this.case=58;

}

cavalier_noir_d=new Cavalier_noir_d();

//****************pion noir 9

function Pion_noir_9() {

this.nom="pion_noir_9";
this.positions="";
this.case=56;

}

pion_noir_9=new Pion_noir_9();

//****************pion noir 10

function Pion_noir_10() {

this.nom="pion_noir_10";
this.positions="";
this.case=55;
}

pion_noir_10=new Pion_noir_10();
//****************pion noir 11

function Pion_noir_11() {

this.nom="pion_noir_11";
this.positions="";
this.case=54;

}

pion_noir_11=new Pion_noir_11();

//****************pion noir 12

function Pion_noir_12() {

this.nom="pion_noir_12";
this.positions="";
this.case=53;

}

pion_noir_12=new Pion_noir_12();
//****************pion noir 13

function Pion_noir_13() {

this.nom="pion_noir_13";
this.positions="";
this.case=52;

}

pion_noir_13=new Pion_noir_13();
//****************pion noir 14

function Pion_noir_14() {

this.nom="pion_noir_14";
this.positions="";
this.case=51;


}

pion_noir_14=new Pion_noir_14();

//****************pion noir 15

function Pion_noir_15() {

this.nom="pion_noir_15";
this.positions="";
this.case=50;

}

pion_noir_15=new Pion_noir_15();

//****************pion noir 16

function Pion_noir_16() {

this.nom="pion_noir_16";
this.positions="";
this.case=49;

}

pion_noir_16=new Pion_noir_16();
//****************roi noir

function Roi_noir() {

this.nom="roi_noir";
this.positions="";
this.case=60;

}

roi_noir=new Roi_noir();

//****************dame noire

function Dame_noir() {

this.nom="dame_noir";
this.positions="";
this.case=61;

}

dame_noir=new Dame_noir();

//****************dame blanc

function Dame_blanc() {

this.nom="dame_blanc";
this.positions="";
this.case=60;
}

dame_blanc=new Dame_blanc();

//****************tour blanc d

function Tour_blanc_d() {

this.nom="tour_blanc_d";
this.positions="";
this.case=64;

}

tour_blanc_d=new Tour_blanc_d();

//****************tour blanc d

function Tour_blanc_g() {

this.nom="tour_blanc_g";
this.positions="";
this.case=57;

}

tour_blanc_g=new Tour_blanc_g();
//****************tour noir g

function Tour_noir_g() {

this.nom="tour_noir_g";
this.positions="";
this.case=64;

}

tour_noir_g=new Tour_noir_g();

//****************tour noir d

function Tour_noir_d() {

this.nom="tour_noir_d";
this.positions="";
this.case=57;

}

tour_noir_d=new Tour_noir_d();

//********************************************************************************************

$(cavalier_blanc_g_piece).draggable({ disabled: false }); 

for (i=1;i<=64;i++) {

$('#div'+i).droppable({

drop : function(event,ui){

position=$(this).attr('id');

position=Number(position.replace('div',''));


var offset = $(this).offset();


if ($(ui.draggable).attr('id')=="cavalier_blanc_g_piece") {
 $(cavalier_blanc_g_piece).offset({top:offset.top+11,left: offset.left+11});
 
var old= cavalier_blanc_g.case  ;

cavalier_blanc_g.case=position;

console.log(position)

historique.push(["cavalier_blanc_g_piece",old,position]);

console.log(historique);


}



}
})
}

function droite() {

search(43);

}

function gauche() {

search(58)

}


function search(position) {

var gauche=$('#div'+position).offset().left+11-$("#cavalier_blanc_g_piece").offset().left;
var haut=$('#div'+position).offset().top+11-$("#cavalier_blanc_g_piece").offset().top;

$("#cavalier_blanc_g_piece").animate({top:"+="+haut,left:"+="+gauche},600);	

}





  }); 
