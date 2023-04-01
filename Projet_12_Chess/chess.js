


$(function() {


var plateau={"a1":57,"b1":58,"c1":59,"d1":60,"e1":61,"f1":62,"g1":63,"h1":64,"a2":49,"b2":50,"c2":51,"d2":52,"e2":53,"f2":54,"g2":55,"h2":56,"a3":41,"b3":42,"c3":43,"d3":44,"e3":45,"f3":46,"g3":47,"h3":48,"a4":33,"b4":34,"c4":35,"d4":36,"e4":37,"f4":38,"g4":39,"h4":40,"a5":25,"b5":26,"c5":27,"d5":28,"e5":29,"f5":30,"g5":31,"h5":32,"a6":17,"b6":18,"c6":19,"d6":20,"e6":21,"f6":22,"g6":23,"h6":24,"a7":9,"b7":10,"c7":11,"d7":12,"e7":13,"f7":14,"g7":15,"h7":16,"a8":1,"b8":2,"c8":3,"d8":4,"e8":5,"f8":6,"g8":7,"h8":8}


var retour=[];
prise=0;
tour=0;

petit_roque_blanc=0;
grand_roque_blanc=0;
petit_roque_noir=0;
grand_roque_noir=0;

coup="";
numero_case=0;
numero_coup=1;

prises_noires=0;
prises_blanches=0;

piece_a_retirer=null;

pieces_autres_pions=["N","B","R","Q","K"];

colonnes=["a","b","c","d","e","f","g","h"];

var historique=[];


document.getElementById('colonnes').innerHTML = "&nbsp;a b c d e f g h" ;
document.getElementById('lignes').innerHTML = "<br><br>8<br><br><br><br><br>7<br><br><br><br>6<br><br><br><br><br>5<br><br><br><br><br>4<br><br><br><br>3<br><br><br><br><br>2<br><br><br><br>1" ;


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
white=lines[4].replaceAll('"',' ').replaceAll(']',' ').replaceAll('[',' ').replaceAll('White',' ')
black=lines[5].replaceAll('"',' ').replaceAll(']',' ').replaceAll('[',' ').replaceAll('Black',' ')

console.log(white)
console.log(black)

document.getElementById('blanc').innerHTML=white;
document.getElementById('noir').innerHTML=black;
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


if (historique[indice][0]==".") {

historique[indice]=historique[indice].substring(1);

 }  

if (historique[indice]=="") {

historique.splice(indice,1)

 }

}

console.log(historique)
  };
  reader.readAsText(file);
};

// **************************************************

function renvoie(table,numero) {

sortie=[]

for (i=0;i<table.length;i++) {

if (table[i][0]==numero) {

sortie.push(table[i])
}

}  

return sortie
}



// **************************************************

function case_vide(case_depart,case_arrivee) {

sortie="vide";

colonne_depart=case_depart%8;
ligne_depart=Math.floor(case_depart/8)+1;
colonne_arrivee=case_arrivee%8;
ligne_arrivee=Math.floor(case_arrivee/8)+1;


if (ligne_depart==ligne_arrivee) {

if (colonne_depart>colonne_arrivee) {

for (i=0;i<toutes_pieces.length;i++) {

if (toutes_pieces[i].ligne==ligne_depart && toutes_pieces[i].colonne <= colonne_depart-1 && toutes_pieces[i].colonne >=colonne_arrivee+1  ) {

sortie="non vide";

}
  
}

} 

else 

{

for (i=0;i<toutes_pieces.length;i++) {

if (toutes_pieces[i].ligne==ligne_depart && toutes_pieces[i].colonne >= colonne_depart+1 && toutes_pieces[i].colonne <=colonne_arrivee-1 ) {

sortie="non vide";

}
  
}

}

}


if (colonne_depart==colonne_arrivee) {


if (ligne_arrivee>ligne_depart) {

for (i=0;i<toutes_pieces.length;i++) {

if (toutes_pieces[i].colonne==colonne_depart && toutes_pieces[i].ligne >= ligne_depart+1 && toutes_pieces[i].ligne <=ligne_arrivee-1  ) {

sortie=toutes_pieces[i];


 }

} 

}

else 

{

for (i=0;i<toutes_pieces.length;i++) {

if (toutes_pieces[i].colonne==colonne_depart && toutes_pieces[i].ligne <= ligne_depart-1 && toutes_pieces[i].ligne >= ligne_arrivee+1) {

sortie="non vide"; 

}

}
  
}

}



return sortie;

}


// ***************************************************

function deplacement(numero_case,piece_position_depart) {

var gauche=$('#div'+numero_case).offset().left+11-$("#"+piece_position_depart.nom+"_piece").offset().left;
var haut=$('#div'+numero_case).offset().top+11-$("#"+piece_position_depart.nom+"_piece").offset().top;

$("#"+piece_position_depart.nom+"_piece").animate({top:"+="+haut,left:"+="+gauche},600);

initial=piece_position_depart.case;

piece_position_depart.modification(numero_case);

element=toutes_pieces.indexOf(piece_position_depart);

retour.push([tour,element,initial,numero_case]);

}

// ***************************************************
function deplacement_back(numero_case,piece_position_depart) {

var gauche=$('#div'+numero_case).offset().left+11-$("#"+piece_position_depart.nom+"_piece").offset().left;
var haut=$('#div'+numero_case).offset().top+11-$("#"+piece_position_depart.nom+"_piece").offset().top;

$("#"+piece_position_depart.nom+"_piece").animate({top:"+="+haut,left:"+="+gauche},600);

piece_position_depart.modification(numero_case);


}

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

// ***************************************************
function possibles_tour(position) {

var valeurs = [ 0,1,2,3,4,5,6,7,8]
function vers_lhorizontale_droite(x) {
  return position + x
}
function vers_lhorizontale_gauche(x) {
  return position - x
}
function vers_laverticale_haut(x) {
  return position - x * 8
}
function vers_laverticale_bas(x) {
  return position + x * 8
}
horizontale_droite=valeurs.map(vers_lhorizontale_droite);
horizontale_gauche=valeurs.map(vers_lhorizontale_gauche);
verticale_haut=valeurs.map(vers_laverticale_haut);
verticale_bas=valeurs.map(vers_laverticale_bas);
positions=horizontale_droite.concat(horizontale_gauche).concat(verticale_haut).concat(verticale_bas);

return positions
}
//****************cavalier blanc_g

function Cavalier_blanc_g() {

this.case=58;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.nom="cavalier_blanc_g";
this.ligne=8;
this.colonne=1;
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

cavalier_blanc_g=new Cavalier_blanc_g();

$(cavalier_blanc_g_piece).draggable({ disabled: false });

//****************cavalier blanc_d

function Cavalier_blanc_d() {

this.case=63;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.nom="cavalier_blanc_d";
this.ligne=8;
this.colonne=7;
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

cavalier_blanc_d=new Cavalier_blanc_d();

$(cavalier_blanc_d_piece).draggable({ disabled: false });

//****************fou noir_g

function Fou_noir_g() {

this.case=3;
this.nom="fou_noir_g";
this.ligne=1;
this.colonne=3;
this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

fou_noir_g=new Fou_noir_g();

$(fou_noir_g_piece).draggable({ disabled: false });

//****************fou noir_d

function Fou_noir_d() {
this.case=6;
this.nom="fou_noir_d";
this.ligne=1;
this.colonne=6;
this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

fou_noir_d=new Fou_noir_d();

$(fou_noir_d_piece).draggable({ disabled: false });

//****************fou blanc_g

function Fou_blanc_g() {
this.case=59;
this.nom="fou_blanc_g";
this.ligne=8;
this.colonne=3;
this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

fou_blanc_g=new Fou_blanc_g();

$(fou_blanc_g_piece).draggable({ disabled: false });


//****************fou blanc_d

function Fou_blanc_d() {

this.case=62;
this.nom="fou_blanc_d";
this.ligne=8;
this.colonne=6;
this.positions=possibles_fou(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_fou(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

fou_blanc_d=new Fou_blanc_d();

$(fou_blanc_d_piece).draggable({ disabled: false });
//****************roi blanc

function Roi_blanc() {

this.nom="roi_blanc";
this.case=61;
this.ligne=8;
this.colonne=5;
this.modification=function(new_position) {
this.case=new_position;
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}
}

pion_blanc_56=new Pion_blanc_56();

$(pion_blanc_56_piece).draggable({ disabled: false });
//****************cavalier noirg

function Cavalier_noir_g() {

this.nom="cavalier_noir_g";
this.case=2;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

cavalier_noir_g=new Cavalier_noir_g();

$(cavalier_noir_g_piece).draggable({ disabled: false });

//****************cavalier noird

function Cavalier_noir_d() {

this.nom="cavalier_noir_d";
this.case=7;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=[this.case-17,this.case-10,this.case+6,this.case+15,this.case+17,this.case+10,this.case-6,this.case-15];
this.modification=function(new_position) {
this.case=new_position;
this.positions=[new_position-17,new_position-10,new_position+6,new_position+15,new_position+17,new_position+10,new_position-6,new_position-15];
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}
}

pion_noir_16=new Pion_noir_16();

$(pion_noir_16_piece).draggable({ disabled: false });
//****************roi noir

function Roi_noir() {

this.nom="roi_noir";
this.case=5;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.modification=function(new_position) {
this.case=new_position;
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

roi_noir=new Roi_noir();

$(roi_noir_piece).draggable({ disabled: false });

//****************dame noire

function Dame_noir() {

this.nom="dame_noir";
this.positions="";
this.case=4;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.modification=function(new_position) {
this.case=new_position;
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

dame_noir=new Dame_noir();

$(dame_noir_piece).draggable({ disabled: false });

//****************dame blanc

function Dame_blanc() {

this.nom="dame_blanc";
this.positions="";
this.case=60;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.modification=function(new_position) {
this.case=new_position;
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}
}

dame_blanc=new Dame_blanc();

$(dame_blanc_piece).draggable({ disabled: false });

//****************tour blanc d

function Tour_blanc_d() {

this.nom="tour_blanc_d";
this.case=64;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=possibles_tour(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_tour(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

tour_blanc_d=new Tour_blanc_d();

$(tour_blanc_d_piece).draggable({ disabled: false });

//****************tour blanc d

function Tour_blanc_g() {

this.nom="tour_blanc_g";
this.case=57;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=possibles_tour(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_tour(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

tour_blanc_g=new Tour_blanc_g();


$(tour_blanc_g_piece).draggable({ disabled: false });
//****************tour noir g

function Tour_noir_g() {

this.nom="tour_noir_g";
this.case=1;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=possibles_tour(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_tour(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
}

}

tour_noir_g=new Tour_noir_g();

$(tour_noir_g_piece).draggable({ disabled: false });

//****************tour noir d

function Tour_noir_d() {

this.nom="tour_noir_d";
this.case=8;
this.colonne=this.case%8;
this.ligne=Math.floor(this.case/8)+1;
this.positions=possibles_tour(this.case);

this.modification=function(new_position) {
this.case=new_position;
this.positions=possibles_tour(new_position);
this.colonne=new_position%8;
this.ligne=Math.floor(new_position/8)+1;
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

tours_blancs=[tour_blanc_g,tour_blanc_d];

pieces_blanches=pions_blancs.concat(cavaliers_blancs).concat(fous_blancs).concat(tours_blancs);


pieces_blanches.push(dame_blanc,roi_blanc);

//********** pieces noires ***************

pions_noirs=[pion_noir_9,pion_noir_10,pion_noir_11,pion_noir_12,pion_noir_13,
pion_noir_14,pion_noir_15,pion_noir_16]

cavaliers_noirs=[cavalier_noir_d,cavalier_noir_g];

fous_noirs=[fou_noir_d,fou_noir_g];

tours_noirs=[tour_noir_g,tour_noir_d];

pieces_noires=pions_noirs.concat(cavaliers_noirs).concat(fous_noirs).concat(tours_noirs);

pieces_noires.push(dame_noir,roi_noir);


toutes_pieces=pieces_blanches.concat(pieces_noires);

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


numero_coup=Math.trunc(tour/2)+1;


if (tour%2==0) {
document.getElementById("coup").innerHTML=numero_coup+ ". blanc : " + coup; 
} else {
document.getElementById("coup").innerHTML=numero_coup+ ". noir : " + coup;   
}

if (coup.includes('+')) 
{

coup=coup.replace('+','');  
}

console.log(coup);

fin=["1-0","0-1","0-0"];

if (fin.indexOf(coup) == -1) {

search(coup);

tour+=1;


}




}

function gauche() {


tour-=1;
numero=tour-1;

numero_coup=Math.trunc(tour/2)+1;
coup=historique[tour];

if (tour%2==0) {
document.getElementById("coup").innerHTML=numero_coup+ ". blanc : " + coup; 
} else {
document.getElementById("coup").innerHTML=numero_coup+ ". noir : " + coup;   
}


liste=renvoie(retour,tour);

for (i=0;i<liste.length;i++) {

piece_position_depart=toutes_pieces[liste[i][1]];

deplacement_back(liste[i][2],piece_position_depart);

}

console.log(tour);


retour=retour.filter(function(value) {return value[0] !==tour});

console.log(retour);



}


function search(coup) {



//######################################################tour des blancs


if (tour%2==0) {

//################coup des pions blancs sans prise#########################################

if (! coup.includes('O') && ! coup.includes('x') && ! pieces_autres_pions.includes(coup[0])) {

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

if (coup.includes('x') && ! pieces_autres_pions.includes(coup[0])) {

prises_noires+=1;

prise=1 ;

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

if (coup[0]=="N" && ! coup.includes('x')) {

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


//################coup des cavaliers blancs avec prise d'une pièce noire

if (coup[0]=="N" && coup.includes('x') ) {

prises_noires+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);

for (i=0;i<cavaliers_blancs.length;i++) {

if (cavaliers_blancs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=cavaliers_blancs[i];


}
}

for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 



//##################################################coup des fous blancs#########################################


//##############coup des fous blancs sans prise###################

if (coup[0]=="B" && ! coup.includes('x')) {

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


//################coup des fous blancs avec prise d'une pièce noire

if (coup[0]=="B" && coup.includes('x') ) {

prises_noires+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);

for (i=0;i<fous_blancs.length;i++) {

if (fous_blancs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=fous_blancs[i];


}
}

for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 

//##################################################coup des tours blanches#########################################


//##############coup des tours blanches sans prise###################

if (coup[0]=="R" && ! coup.includes('x')) {


if (coup.length==4) {

depart=coup[1];

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log(numero_case);

colonne=colonnes.indexOf(depart)+1;

for (i=0;i<tours_blancs.length;i++) {

if (tours_blancs[i].colonne == colonne) {

piece_position_depart=tours_blancs[i];

}
}
  
}


if (coup.length==3) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

possibles=[];

possibles[0]=case_vide(numero_case,tours_blancs[0].case);

possibles[1]=case_vide(numero_case,tours_blancs[1].case);

for (i=0;i<tours_blancs.length;i++) {


if (tours_blancs[i].positions.indexOf(numero_case) != -1 && possibles[i]=="vide") {

piece_position_depart=tours_blancs[i];

}


}
  
}


}


//################coup des tours blanches avec prise d'une pièce noire

if (coup[0]=="R" && coup.includes('x') ) {

prises_noires+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);

for (i=0;i<tours_blancs.length;i++) {

if (tours_blancs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=tours_blancs[i];


}
}

for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 



// #############################################coup du petit roque des blancs#############

if (coup[0]=="O" && coup.length==3 ) {

petit_roque_blanc=1;

}

// #############################################coup du grand roque des blancs#############

if (coup[0]=="O" && coup.length==5 ) {

grand_roque_blanc=1;

}


//#######################################coup de la dame blanche #########################################



// ###############################coup de la dame blanche sans prise###################

if (coup[0]=="Q" && ! coup.includes('x')) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log("case_de_départ ",numero_case);

piece_position_depart=dame_blanc;

}


// ################################coup de la dame blanche avec prise #################

if (coup[0]=="Q" && coup.includes('x') ) {

prises_noires+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);


piece_position_depart=dame_blanc;


for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 


//#######################################coup du roi blanc #########################################



// ###############################coup du roi blanc sans prise###################

if (coup[0]=="K" && ! coup.includes('x')) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log("case_de_départ ",numero_case);

piece_position_depart=roi_blanc;

}


// ################################coup du roi blanc avec prise #####################

if (coup[0]=="K" && coup.includes('x') ) {

prises_noires+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);


piece_position_depart=roi_blanc;


for (i=0;i<pieces_noires.length;i++) {

if (pieces_noires[i].case == numero_case) {

piece_a_retirer=pieces_noires[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 



// ##############################################fin du tour des blancs ###########################################

}



//################################################################################tour des noirs


if (tour%2==1) {

//################coup des pions noirs sans prise

if (! coup.includes('O') && ! coup.includes('x') && ! pieces_autres_pions.includes(coup[0]) ) {

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

if (coup.includes('x') && ! pieces_autres_pions.includes(coup[0]) ) {

prises_blanches+=1;

prise=1;

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


if (coup[0]=="N" && ! coup.includes('x')) {

if (coup.length==3) {


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

if (coup.length==4) {

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<cavaliers_noirs.length;i++) {

console.log(cavaliers_noirs[i].positions);

if (cavaliers_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=cavaliers_noirs[i];


}
  
}

}



}



if (coup[0]=="N" && coup.includes('x')) {


if (coup.length==4) {

prises_blanches+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_arrivee",numero_case);

for (i=0;i<cavaliers_noirs.length;i++) {

if (cavaliers_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=cavaliers_noirs[i];


}
}

for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_blanche_à_retirer",piece_a_retirer);

}

if (coup.length==5) {

depart=coup[1];

prises_blanches+=1;

prise=1;

coup=coup.substring(3,5);

numero_case=plateau[coup];

console.log("case_arrivee",numero_case);

colonne=colonnes.indexOf(depart)+1;

console.log(colonne);


for (i=0;i<cavaliers_noirs.length;i++) {

console.log(cavaliers_noirs[i]);

if (cavaliers_noirs[i].colonne == colonne) {

piece_position_depart=cavaliers_noirs[i];


}
}

for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_blanche_à_retirer",piece_a_retirer);

}

}



//##################################################coup des fous noirs#########################################


//##############coup des fous noirs sans prise###################

if (coup[0]=="B" && ! coup.includes('x')) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<fous_noirs.length;i++) {

console.log(fous_noirs[i].positions);

if (fous_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=fous_noirs[i];


}
  
}

}


//################coup des fous noirs avec prise d'une pièce blanche

if (coup[0]=="B" && coup.includes('x') ) {

prises_blanches+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);

for (i=0;i<fous_noirs.length;i++) {

if (fous_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=fous_noirs[i];


}
}

for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_blanche_à_retirer",piece_a_retirer);
} 


//##################################################coup des tours noires#########################################


//##############coup des tours noires sans prise###################

if (coup[0]=="R" && ! coup.includes('x')) {


if (coup.length==4) {//coup avec indication de colonne

depart=coup[1];

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log(numero_case);

colonne=colonnes.indexOf(depart)+1;

for (i=0;i<tours_noirs.length;i++) {

if (tours_noirs[i].case%8 == colonne) {

piece_position_depart=tours_noirs[i];

}
}
  
}


if (coup.length==3) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log(numero_case);

for (i=0;i<tours_noirs.length;i++) {

console.log(tours_noirs[i].positions);

if (tours_noirs[i].positions.indexOf(numero_case) != -1 ) {

piece_position_depart=tours_noirs[i];

console.log(case_vide(tours_noirs[i].case,numero_case))

}
}
  
}


}


//################coup des tours noires avec prise d'une pièce blanche

if (coup[0]=="R" && coup.includes('x') ) {

prises_blanches+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);

for (i=0;i<tours_noirs.length;i++) {

if (tours_noirs[i].positions.indexOf(numero_case) != -1) {

piece_position_depart=tours_noirs[i];


}
}

for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 






//#######################################coup de la dame noire #########################################



// ###############################coup de la dame noire sans prise###################

if (coup[0]=="Q" && ! coup.includes('x')) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log("case_de_départ ",numero_case);

piece_position_depart=dame_noir;

}


// ################################coup de la dame noire avec prise #################

if (coup[0]=="Q" && coup.includes('x') ) {

prises_blanches+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);


piece_position_depart=dame_noir;


for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 

//#######################################coup du roi noir #########################################



// ###############################coup du roi noir sans prise###################

if (coup[0]=="K" && ! coup.includes('x')) {

coup=coup.substring(1,3);

numero_case=plateau[coup];

console.log("case_de_départ ",numero_case);

piece_position_depart=roi_noir;

}

// ################################coup du roi nboir avec prise #################

if (coup[0]=="K" && coup.includes('x') ) {

prises_blanches+=1;

prise=1;

coup=coup.substring(2,4);

numero_case=plateau[coup];

console.log("case_de_départ",numero_case);


piece_position_depart=roi_noir;


for (i=0;i<pieces_blanches.length;i++) {

if (pieces_blanches[i].case == numero_case) {

piece_a_retirer=pieces_blanches[i];

}
 
}

console.log("piece_noire_à_retirer",piece_a_retirer);
} 



// #############################################coup du petit roque des noirs#############

if (coup[0]=="O" && coup.length==3 ) {

petit_roque_noir=1;

}

// #############################################coup du grand roque des blancs#############

if (coup[0]=="O" && coup.length==5 ) {

grand_roque_noir=1;

}


// ###################################fin du tour des noirs ######################################################


}



// #############################################deplacement de la pièce ############################

// ########################################### cas général

if (petit_roque_noir==0 && petit_roque_blanc==0 && grand_roque_noir==0 && grand_roque_blanc==0) {

var gauche=$('#div'+numero_case).offset().left+11-$("#"+piece_position_depart.nom+"_piece").offset().left;
var haut=$('#div'+numero_case).offset().top+11-$("#"+piece_position_depart.nom+"_piece").offset().top;

var initial=piece_position_depart.case;
$("#"+piece_position_depart.nom+"_piece").animate({top:"+="+haut,left:"+="+gauche},600);

// ###################  mise à jour de la position de la pièce déplacée

piece_position_depart.modification(numero_case);

console.log("piece_position_depart",piece_position_depart);

element=toutes_pieces.indexOf(piece_position_depart);

retour.push([tour,element,initial,numero_case]);

}



// ######################################### fin du cas général 
//
// ######################################### cas du petit roque blanc 

if (petit_roque_blanc==1) {

console.log("petit_roque_blanc");

// ##################### mouvement du roi blanc au petit roque

deplacement(63,roi_blanc)


// ##################### mouvement de la tour blanche au petit roque

deplacement(62,tour_blanc_d)

// ########## fin du petit roque blanc
petit_roque_blanc=0;

}



// ######################################### cas du petit roque blanc 

if (petit_roque_noir==1) {

console.log("petit_roque_noir");

// ##################### mouvement du roi noir au petit roque

deplacement(7,roi_noir);

// ##################### mouvement de la tour noire au petit roque

deplacement(6,tour_noir_d);

// ########## fin du petit roque blanc
petit_roque_noir=0;

}


if (grand_roque_blanc==1) {

console.log("grand_roque_blanc");

// ##################### mouvement du roi blanc au grand roque

deplacement(59,roi_blanc)

// ##################### mouvement de la tour blanche au petit roque

deplacement(60,tour_blanc_g)

// ########## fin du petit roque blanc

grand_roque_blanc=0;

}

if (grand_roque_noir==1) {

console.log("grand_roque_noir");

// ##################### mouvement du roi blanc au grand roque

deplacement(3,roi_noir)

// ##################### mouvement de la tour noir au grand roque

deplacement(4,tour_noir_g)

// ########## fin du petit roque blanc

grand_roque_noir=0;

}




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



element=toutes_pieces.indexOf(piece_a_retirer);

retour.push([tour,element,piece_a_retirer.case,x]);

piece_a_retirer.modification(x);

prise=0;

//var index = pieces_blanches.indexOf(piece_a_retirer);
//if (index > -1) {
//  pieces_blanches.splice(index, 1);
//}

//var index = pieces_noires.indexOf(piece_a_retirer);
//if (index > -1) {
//  pieces_noires.splice(index, 1);

//}



}


console.log(retour);


// ###############################################################

}



//+++++++++++++++++++++++++Fin
  }); 
