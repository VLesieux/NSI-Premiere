


$(function() {


var historique=[];


document.getElementById('colonnes').innerHTML = "&nbsp;a b c d e f g h" ;
document.getElementById('lignes').innerHTML = "<br><br>8<br><br><br><br>7<br><br><br><br>6<br><br><br><br>5<br><br><br><br>4<br><br><br><br>3<br><br><br><br>2<br><br><br><br>1" ;

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

$(cavalier_blanc_g_piece).offset({top:$('#div'+34).offset().top+11,left: $('#div'+34).offset().left+11 });


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

$(cavalier_blanc_g_piece).attr( "class",position);

console.log(historique)

var numero_colonne=Math.round(($(cavalier_blanc_g_piece).offset().left-11-$("#div1").offset().left)/($("#div2").offset().left-$("#div1").offset().left))+1;

var numero_ligne=Math.round(($(cavalier_blanc_g_piece).offset().top-11-$("#div1").offset().top)/($("#div9").offset().top-$("#div1").offset().top))+1;


console.log(numero_colonne,numero_ligne)

}



}
})
}

  }); 
