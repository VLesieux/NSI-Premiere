pari=[];
lancement=false;
choix=0;
nombre=0;
initial=100;

document.getElementById("portefeuille").innerHTML =initial;

mise=document.getElementById("mise").value;

document.addEventListener("click", function(event) {
str=event.target.id;
console.log(str);
//////////////////////////////////////
if (str !="plateau" && str !="mise"  && str.length<=8 && str !="bouton0") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";

  if (str.length==8) {valeur=parseInt(str.substr(str.length - 2)); }
  else {  valeur=parseInt(str.substr(str.length - 1)); }
  console.log(valeur);
  pari.push(valeur);
  console.log(pari);
  document.getElementById("pari").innerHTML=pari
}
//////////////////////////////////////
if (str=="boutonpremiere12") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[1,2,3,4,5,6,7,8,9,10,11,12];
choix=1;
nombre=12;
}

//////////////////////////////////////
if (str=="boutondeuxieme12") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[13,14,15,16,17,18,19,20,21,22,23,24];
choix=2;
nombre=12;
}

//////////////////////////////////////
if (str=="boutontroisieme12") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[25,26,27,28,29,30,31,32,33,34,35,36];
choix=3;
nombre=12;
}

//////////////////////////////////////
if (str=="boutona18") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];
choix=4;
nombre=18;
}
//////////////////////////////////////
if (str=="boutonPair") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
for (j = 1; j < 19; j++) {
pari.push(j*2)
}
choix=5;
nombre=18;
}
//////////////////////////////////////
if (str=="boutonImpair") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
for (j = 0; j < 18; j++) {
pari.push(j*2+1)
};
choix=6;
nombre=18;
}
//////////////////////////////////////
if (str=="boutonRouge") {
      var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36];
choix=7;
nombre=18;
}
//////////////////////////////////////
if (str=="boutonNoir") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[2,6,4,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35];
choix=8;
nombre=18;
}
//////////////////////////////////////
if (str=="boutona36") {
  var button = document.getElementById(event.target.id);
  button.style.backgroundColor = "blue";
pari=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36];
choix=9;
nombre=18;
}
//////////////////////////////////////
console.log(pari);
console.log(choix);
console.log(nombre);
document.getElementById("pari").innerHTML=pari

});


tirage=0


document.getElementById("boutonroulette").addEventListener("click", action);



document.getElementById("Recommencer").addEventListener("click", reinitialise);


function reinitialise() {

pari=[];
choix=0;
x=["bouton3","bouton9","bouton12","bouton18","bouton21","bouton27","bouton30","bouton36","bouton5","bouton14","bouton23","bouton32","bouton1","bouton7","bouton16","bouton19","bouton25","bouton34","boutonpremiere12","boutondeuxieme12","boutontroisieme12","boutona18","boutonPair","boutonRouge","boutonNoir","boutonImpair","boutona36"];
y=["bouton6","bouton15","bouton24","bouton33","bouton2","bouton8","bouton11","bouton17","bouton20","bouton26","bouton29","bouton35","bouton4","bouton10","bouton13","bouton22","bouton28","bouton31"]

for(var i= 0; i < x.length; i++)
{
var button = document.getElementById(x[i]);
button.style.backgroundColor = "red";
}

for(var i= 0; i < y.length; i++)
{
var button = document.getElementById(y[i]);
button.style.backgroundColor = "black";
}


}




function action() {

//////////////////////////////////////
if (pari.length==1) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur un seul numéro : numéro plein";
lancement=true
}

/////////////////////////////////////
if (pari.length==2) {

if (Math.abs(pari[1]-pari[0])==3) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur deux numéros (cheval)";
lancement=true
}

else {

document.getElementById("commentaire").innerHTML = "Les deux numéros choisis doivent être adjacents. Rejouez !"


}
}

//////////////////////////////////////
if (pari.length==3) {

pari.sort((a, b) => a - b);

liste=[1,4,7,10,13,16,19,22,25,28,31,34];

if (pari[1]-pari[0]==1 && pari[2]-pari[1]==1 &&  liste.includes(pari[0]) ) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur trois numéros (transversale).";
lancement=true

}

else {

document.getElementById("commentaire").innerHTML = "Les trois numéros choisis doivent être disposés en colonne. Rejouez !"


}
}
//////////////////////////////////////
if (pari.length==4) {

pari.sort((a, b) => a - b);

if (pari[1]-pari[0]==1 && pari[2]-pari[1]==2 && pari[3]-pari[2]==1) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur quatre numéros (carré).";
lancement=true

}

else {

document.getElementById("commentaire").innerHTML = "Les quatre numéros choisis doivent être disposés en carré. Rejouez !"


}
}
//////////////////////////////////////
if (pari.length==6) {

pari.sort((a, b) => a - b);

if (pari[1]-pari[0]==1 && pari[2]-pari[1]==1 && pari[4]-pari[3]==1 && pari[5]-pari[4]==1) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur six numéros (sixain).";
lancement=true

}

else {

document.getElementById("commentaire").innerHTML = "Les six numéros joués doivent être disposés en deux colonnes de trois. Rejouez !"


}
}
//////////////////////////////////////


if (document.getElementById("mise").value>initial) {

    document.getElementById("commentaire").innerHTML = "Vous ne pouvez pas miser autant";
    lancement=false}


if (choix>=1 && pari.length==nombre) {lancement=true}

if (lancement==true) {
mise=document.getElementById("mise").value;
tirage=Math.floor(Math.random()*37+1)
document.getElementById("tirage").innerHTML = tirage

//////////////////////////////////////
if (pari.length==1) {

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez 35 fois votre mise."
initial=initial+35*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}

//////////////////////////////////////

else if (pari.length==2) {

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez 17 fois votre mise."
initial=initial+17*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }

}
//////////////////////////////////////

else if (pari.length==3) {

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez 11 fois votre mise."
initial=initial+11*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }

}

//////////////////////////////////////
else if (pari.length==4) {

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez 8 fois votre mise."
initial=initial+8*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }

}
//////////////////////////////////////
else if (pari.length==6) {

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez 5 fois votre mise."
initial=initial+5*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}
//////////////////////////////////////
else if (choix==1 || choix==2 || choix==3) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur une douzaine";

if (pari.includes(tirage)) {

document.getElementById("gain").innerHTML = "Bravo, vous gagnez 2 fois votre mise."
initial=initial+2*mise;
document.getElementById("portefeuille").innerHTML =initial;

}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
    initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}
//////////////////////////////////////
else if (choix==4 || choix==9) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur une moitié du plateau (sauf 0)";

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez votre mise."
initial=initial+1*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
    initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}
//////////////////////////////////////
else if (choix==5 || choix==6) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur la parité";

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez votre mise."
initial=initial+1*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
    initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}
//////////////////////////////////////
else if (choix==7 || choix==8) {

document.getElementById("commentaire").innerHTML = "Vous avez fait un pari sur la couleur";

if (pari.includes(tirage)) {
document.getElementById("gain").innerHTML = "Bravo, vous gagnez votre mise."
initial=initial+1*mise;
document.getElementById("portefeuille").innerHTML =initial;
}
else {
    document.getElementById("gain").innerHTML = "Désolé, vous perdez votre mise."
    initial=initial-mise;
document.getElementById("portefeuille").innerHTML =initial;
    }
}
//////////////////////////////////////   





  }

else 

{

    document.getElementById("commentaire").innerHTML = "Votre pari n'est pas correct";
}

}
 