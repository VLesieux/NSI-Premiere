


$(function() {

var plateau={"a1":57,"b1":58,"c1":59,"d1":60,"e1":61,"f1":62,"g1":63,"h1":64,"a2":49,"b2":50,"c2":51,"d2":52,"e2":53,"f2":54,"g2":55,"h2":56,"a3":41,"b3":42,"c3":43,"d3":44,"e3":45,"f3":46,"g3":47,"h3":48,"a4":33,"b4":34,"c4":35,"d4":36,"e4":37,"f4":38,"g4":39,"h4":40,"a5":25,"b5":26,"c5":27,"d5":28,"e5":29,"f5":40,"g5":31,"h5":32,"a6":17,"b6":18,"c6":19,"d6":20,"e6":21,"f6":22,"g6":23,"h6":24,"a7":9,"b7":10,"c7":11,"d7":12,"e7":13,"f7":11,"g7":15,"h7":11,"a8":1,"b8":2,"c8":3,"d8":4,"e8":5,"f8":6,"g8":7,"h8":8}

prise=0;
tour=0;

coup="";
numero_case=0;

prises_noires=0;
prises_blanches=0;

piece_a_retirer=null;

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

historique.shift();

for(var indice = 0; indice < historique.length; indice++){

if (indice%2==0)

{ 

historique[indice]=historique[indice].substring(2,historique[indice].length)
 }  

    }

console.log(historique)
  };
  reader.readAsText(file);
};

// ***************************************************
function possibles_fou(position) {

var valeurs = [ 0,1,2,3,4,5,6,7,8]
function vers_le_haut_droit(x) {
  return position - x * 7
}
function vers_le_haut_bas(x) {
  return position + x * 7
}
function vers_le_bas_haut(x) {
  return position - x * 9
}
function vers_le_bas_bas(x) {
  return position + x * 9
}
diagonale_ascendante_vers_haut=valeurs.map(vers_le_haut_droit);
diagonale_ascendante_vers_bas=valeurs.map(vers_le_haut_bas);
diagonale_descendante_vers_haut=valeurs.map(vers_le_bas_haut);
diagonale_descendante_vers_bas=valeurs.map(vers_le_bas_bas);
positions=diagonale_ascendante_vers_bas.concat(diagonale_ascendante_vers_haut).concat(diagonale_descendante_vers_bas).concat(diagonale_descendante_vers_haut);

return positions
}


//****************cavalier blanc_g

function Cavalier_blanc_g() {

this.case=58;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.nom="cavalier_blanc_g";
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
}

}

cavalier_blanc_g=new Cavalier_blanc_g();

$(cavalier_blanc_g_piece).draggable({ disabled: false });

//****************cavalier blanc_d

function Cavalier_blanc_d() {

this.case=63;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.nom="cavalier_blanc_d";
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
}

}

cavalier_blanc_d=new Cavalier_blanc_d();

$(cavalier_blanc_d_piece).draggable({ disabled: false });

//****************fou noir_g

function Fou_noir_g() {

this.case=59;
this.nom="fou_noir_g";

var valeurs = [ 0,1,2,3,4,5,6,7,8]
function vers_le_haut(x) {
  return this.case - x * 7
}
function vers_le_bas(x) {
  return this.case + x * 7
}
diagonale_ascendante=valeurs.map(vers_le_haut);
diagonale_descendante=valeurs.map(vers_le_bas);
this.positions=diagonale_ascendante.concat(diagonale_descendante);

this.modification=function(new_position) {
this.case=new_position;
diagonale_ascendante=valeurs.map(vers_le_haut);
diagonale_descendante=valeurs.map(vers_le_bas);
this.positions=diagonale_ascendante.concat(diagonale_descendante);}

}

fou_noir_g=new Fou_noir_g();

$(fou_noir_g_piece).draggable({ disabled: false });

//****************fou noir_d

function Fou_noir_d() {
this.case=62;
this.nom="fou_noir_d";

var valeurs = [ 0,1,2,3,4,5,6,7,8]
function vers_le_haut(x) {
  return this.case - x * 7
}
function vers_le_bas(x) {
  return this.case + x * 7
}
diagonale_ascendante=valeurs.map(vers_le_haut);
diagonale_descendante=valeurs.map(vers_le_bas);
this.positions=diagonale_ascendante.concat(diagonale_descendante);

this.modification=function(new_position) {
this.case=new_position;
diagonale_ascendante=valeurs.map(vers_le_haut);
diagonale_descendante=valeurs.map(vers_le_bas);
this.positions=diagonale_ascendante.concat(diagonale_descendante);}

}

fou_noir_d=new Fou_noir_d();

$(fou_noir_d_piece).draggable({ disabled: false });

//****************fou blanc_g

function Fou_blanc_g() {
this.case=59;
this.nom="fou_blanc_g";

this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
}

}

fou_blanc_g=new Fou_blanc_g();

$(fou_blanc_g_piece).draggable({ disabled: false });


//****************fou blanc_d

function Fou_blanc_d() {

this.case=62;
this.nom="fou_blanc_d";
this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
}

}

fou_blanc_d=new Fou_blanc_d();

$(fou_blanc_d_piece).draggable({ disabled: false });
//****************roi blanc

function Roi_blanc() {

this.nom="roi_blanc";
this.positions="";
this.case=61;
this.modification=function(new_position) {
this.case=new_position;
}

}

roi_blanc=new Roi_blanc();

$(roi_blanc_piece).draggable({ disabled: false });

//****************pion blanc 53

function Pion_blanc_53() {

this.nom="pion_blanc_53";
this.positions=[45,37];
this.case=53;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}

}

pion_blanc_53=new Pion_blanc_53();

$(pion_blanc_53_piece).draggable({ disabled: false });

//****************pion blanc 53

function Pion_blanc_49() {

this.nom="pion_blanc_49";
this.positions=[41,33];
this.case=49;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}

}

pion_blanc_49=new Pion_blanc_49();

$(pion_blanc_49_piece).draggable({ disabled: false });

//****************pion blanc 50

function Pion_blanc_50() {

this.nom="pion_blanc_50";
this.positions=[42,34];
this.case=50;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_50=new Pion_blanc_50();

$(pion_blanc_50_piece).draggable({ disabled: false });

//****************pion blanc 51

function Pion_blanc_51() {

this.nom="pion_blanc_51";
this.positions=[43,35];
this.case=51;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_51=new Pion_blanc_51();

$(pion_blanc_51_piece).draggable({ disabled: false });

//****************pion blanc 52

function Pion_blanc_52() {

this.nom="pion_blanc_52";
this.positions=[44,36];
this.case=52;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_52=new Pion_blanc_52();

$(pion_blanc_52_piece).draggable({ disabled: false });

//****************pion blanc 53

function Pion_blanc_53() {

this.nom="pion_blanc_53";
this.positions=[45,37];
this.case=53;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_53=new Pion_blanc_53();

$(pion_blanc_53_piece).draggable({ disabled: false });

//****************pion blanc 54

function Pion_blanc_54() {

this.nom="pion_blanc_54";
this.positions=[46,38];
this.case=54;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_54=new Pion_blanc_54();

$(pion_blanc_54_piece).draggable({ disabled: false });

//****************pion blanc 55

function Pion_blanc_55() {

this.nom="pion_blanc_55";
this.positions=[47,39];
this.case=55;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_55=new Pion_blanc_55();

$(pion_blanc_55_piece).draggable({ disabled: false });
//****************pion blanc 56

function Pion_blanc_56() {

this.nom="pion_blanc_56";
this.positions=[48,40];
this.case=56;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_blanc_56=new Pion_blanc_56();

$(pion_blanc_56_piece).draggable({ disabled: false });
//****************cavalier noirg

function Cavalier_noir_g() {

this.nom="cavalier_noir_g";
this.case=2;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
}

}

cavalier_noir_g=new Cavalier_noir_g();

$(cavalier_noir_g_piece).draggable({ disabled: false });

//****************cavalier noird

function Cavalier_noir_d() {

this.nom="cavalier_noir_d";
this.case=7;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
}

}

cavalier_noir_d=new Cavalier_noir_d();

$(cavalier_noir_d_piece).draggable({ disabled: false });

//****************pion noir 9

function Pion_noir_9() {

this.nom="pion_noir_9";
this.case=9;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}

}

pion_noir_9=new Pion_noir_9();

$(pion_noir_9_piece).draggable({ disabled: false });

//****************pion noir 10

function Pion_noir_10() {

this.nom="pion_noir_10";
this.case=10;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_10=new Pion_noir_10();

$(pion_noir_10_piece).draggable({ disabled: false });
//****************pion noir 11

function Pion_noir_11() {

this.nom="pion_noir_11";
this.case=11;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_11=new Pion_noir_11();

$(pion_noir_11_piece).draggable({ disabled: false });

//****************pion noir 12

function Pion_noir_12() {

this.nom="pion_noir_12";
this.case=12;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_12=new Pion_noir_12();

$(pion_noir_12_piece).draggable({ disabled: false });
//****************pion noir 13

function Pion_noir_13() {

this.nom="pion_noir_13";
this.case=13;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_13=new Pion_noir_13();

$(pion_noir_13_piece).draggable({ disabled: false });
//****************pion noir 11

function Pion_noir_14() {

this.nom="pion_noir_14";
this.case=14;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}

}

pion_noir_14=new Pion_noir_14();

$(pion_noir_14_piece).draggable({ disabled: false });

//****************pion noir 15

function Pion_noir_15() {

this.nom="pion_noir_15";
this.case=15;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_15=new Pion_noir_15();

$(pion_noir_15_piece).draggable({ disabled: false });

//****************pion noir 11

function Pion_noir_16() {

this.nom="pion_noir_16";
this.case=16;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
//************* méthode ******
this.modification=function(new_position) {
this.case=new_position;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
}
}

pion_noir_16=new Pion_noir_16();

$(pion_noir_16_piece).draggable({ disabled: false });
//****************roi noir

function Roi_noir() {

this.nom="roi_noir";
this.case=60;
this.modification=function(new_position) {
this.case=new_position;
}

}

roi_noir=new Roi_noir();

$(roi_noir_piece).draggable({ disabled: false });

//****************dame noire

function Dame_noir() {

this.nom="dame_noir";
this.positions="";
this.case=61;
this.modification=function(new_position) {
this.case=new_position;
}

}

dame_noir=new Dame_noir();

$(dame_noir_piece).draggable({ disabled: false });

//****************dame blanc

function Dame_blanc() {

this.nom="dame_blanc";
this.positions="";
this.case=60;
this.modification=function(new_position) {
this.case=new_position;
}
}

dame_blanc=new Dame_blanc();

$(dame_blanc_piece).draggable({ disabled: false });

//****************tour blanc d

function Tour_blanc_d() {

this.nom="tour_blanc_d";
this.positions="";
this.case=64;
this.modification=function(new_position) {
this.case=new_position;
}

}

tour_blanc_d=new Tour_blanc_d();

$(tour_blanc_d_piece).draggable({ disabled: false });

//****************tour blanc d

function Tour_blanc_g() {

this.nom="tour_blanc_g";
this.positions="";
this.case=57;
this.modification=function(new_position) {
this.case=new_position;
}

}

tour_blanc_g=new Tour_blanc_g();


$(tour_blanc_g_piece).draggable({ disabled: false });
//****************tour noir g

function Tour_noir_g() {

this.nom="tour_noir_g";
this.positions="";
this.case=64;
this.modification=function(new_position) {
this.case=new_position;
}

}

tour_noir_g=new Tour_noir_g();

$(tour_noir_g_piece).draggable({ disabled: false });

//****************tour noir d

function Tour_noir_d() {

this.nom="tour_noir_d";
this.positions="";
this.case=57;
this.modification=function(new_position) {
this.case=new_position;
}

}

tour_noir_d=new Tour_noir_d();

$(tour_noir_d_piece).draggable({ disabled: false });

//*******************************Liste des pièces *************************************************************

//********** pieces blanches ***************

pions_blancs=[pion_blanc_49,pion_blanc_50,pion_blanc_51,pion_blanc_52,pion_blanc_53,
pion_blanc_54,pion_blanc_55,pion_blanc_56];

cavaliers_blancs=[cavalier_blanc_d,cavalier_blanc_g];

fous_blancs=[fou_blanc_d,fou_blanc_g];

pieces_blanches=pions_blancs.concat(cavaliers_blancs).concat(fous_blancs);


//********** pieces noires ***************

pions_noirs=[pion_noir_9,pion_noir_10,pion_noir_11,pion_noir_12,pion_noir_13,
pion_noir_14,pion_noir_15,pion_noir_16]

cavaliers_noirs=[cavalier_noir_d,cavalier_noir_g]

fous_noirs=[fou_noir_d,fou_noir_g];

pieces_noires=pions_noirs.concat(cavaliers_noirs).concat(fous_noirs);

//********************************************************************************************


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


coup=historique[tour];


search(coup);

tour+=1;


}

function gauche() {

tour-=1;
numero=tour-1;

coup=historique[tour];

search(coup);

}


function search(coup) {



//######################################################tour des blancs


if (tour%2==0) {

//################coup des pions blancs sans prise#########################################

if (coup.length==2) {

numero_case=plateau[coup];

console.log(numero_case);

colonne=numero_case%8;

for (i=0;i<pions_blancs.length;i++) {

if (pions_blancs[i].colonne ===colonne) {

piece_position_depart=pions_blancs[i]
}
  
}

}	


//################coup des pions blancs avec prise d'une pièce noire

if (coup.length==4) {

prises_noires+=1;

prise=1

colonnes=["a","b","c","d","e","f","g","h"];

depart=coup[0];

coup=coup.substring(2,4);

numero_case=plateau[coup];

ligne=Math.floor(numero_case/8)+1;

colonne=colonnes.indexOf(depart)+1;

for (i=0;i<pions_blancs.length;i++) {

if (pions_blancs[i].colonne == colonne && pions_blancs[i].ligne==ligne+1) {

piece_position_depart=pions_blancs[i]
}
 
}

for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 


// #########################################################################################

//##################################################coup des cavaliers blancs#########################################


//##############coup des cavaliers blancs sans prise###################

if (coup[0]=="N" && coup.length==3) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<cavaliers_blancs.length;i++) {

console.log(cavaliers_blancs[i].positions);

if (cavaliers_blancs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=cavaliers_blancs[i];


}
  
}

}

//##################################################coup des fous blancs#########################################


//##############coup des fous blancs sans prise###################

if (coup[0]=="B" && coup.length==3) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<fous_blancs.length;i++) {

console.log(fous_blancs[i].positions);

if (fous_blancs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=fous_blancs[i];


}
  
}

}






// ##############################################fin du tour des blancs ###########################################

}



//################################################################################tour des noirs


if (tour%2==1) {

//################coup des pions noirs sans prise

if (coup.length==2) {

numero_case=plateau[coup];

console.log(numero_case);

colonne=numero_case%8;

for (i=0;i<pions_noirs.length;i++) {

if (pions_noirs[i].colonne == colonne) {

piece_position_depart=pions_noirs[i]
}


  
}

} 

//################coup des pions noirs avec prise d'une pièce blanche

if (coup.length==4) {

prises_blanches+=1;

prise=1

colonnes=["a","b","c","d","e","f","g","h"];

depart=coup[0];

coup=coup.substring(2,4);

numero_case=plateau[coup];

ligne=Math.floor(numero_case/8)+1;

colonne=colonnes.indexOf(depart)+1;

for (i=0;i<pions_noirs.length;i++) {

if (pions_noirs[i].colonne == colonne && pions_noirs[i].ligne==ligne-1) {

piece_position_depart=pions_noirs[i]
}
 
}

for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_blanche_à_retirer",piece_a_retirer);
} 


//#######################################coup des cavaliers noirs#########################################



// ###############################coup des cavaliers noirs sans prise###################

if (coup[0]=="N" && coup.length==3) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<cavaliers_noirs.length;i++) {

console.log(cavaliers_noirs[i].positions);

if (cavaliers_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=cavaliers_noirs[i];


}
  
}

}






// ###################################fin du tour des noirs ######################################################


}



// ################################deplacement de la pièce ############################


var gauche=$('#div'+numero_case).offset().left+11-$("#"+piece_position_depart.nom+"_piece").offset().left;
var haut=$('#div'+numero_case).offset().top+11-$("#"+piece_position_depart.nom+"_piece").offset().top;

$("#"+piece_position_depart.nom+"_piece").animate({top:"+="+haut,left:"+="+gauche},600);

// ###################  mise à jour de la position de la pièce déplacée

piece_position_depart.modification(numero_case);

console.log("piece_position_depart",piece_position_depart);

console.log("case d'arrivée",numero_case);


// ################### déplacement et mise à jour de la pièce retirée ###################


if (piece_a_retirer !== null && prise==1) {


if (tour%2==1) {

x=99+prises_blanches;

}

if (tour%2==0) {

x=-34-prises_noires;


}

chaine='#div'+x.toString();

$("#"+piece_a_retirer.nom+"_piece").offset({top:$(chaine).offset().top+11,left: $(chaine).offset().left+11 });

piece_a_retirer.case=x;

prise=0;

}



// ###############################################################

}



//+++++++++++++++++++++++++Fin
  }); 
