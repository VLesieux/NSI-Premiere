var interval;
var choix_colonne;
var ligne ;
var tabl = [] ;
var liste_rouge = [] ;
var liste_jaune = [] ;
var cas;
var joueur ;


joueur = 1 ;

init();

function selection(colonne){

     

        for (j=1;j<=7;j++) 
{
        for(i=0;i<=6; i++)
    {
        document.getElementById(j+""+i+"").style.opacity= '1';
        document.getElementById(j + "" + 0 + "").innerHTML = '<img src="vide.png" />';
    }
}

       for (i=0;i<=6; i++) /*i = 1 car on commence par la case : 11 et non 10*/
        {
            document.getElementById(colonne+""+i+"").style.opacity = '0.7'; /*on change l'opacitÃ© des cases dont le chiffre des dizaines est la conolonne sÃ©lectionnÃ©e et le chiffre des unitÃ©s allant de 1 Ã  6 : i. En gros on change l'opacitÃ© de la colonne sÃ©lectionnÃ©*/
            if (joueur == 1) {
                document.getElementById(colonne + "" + 0 + "").innerHTML = '<img src="rouge1.png" />';
            } else {
                document.getElementById(colonne + "" + 0 + "").innerHTML = '<img src="jaune1.png" />';
            }

        }
}

function jeu(colonne){
choix_colonne=colonne;
ligne=0;
    if(tabl[choix_colonne+""+1+""] == "vide"){
        interval= setInterval(anim,150); 
    }else{
        alert("Coup impossible");
    }
}

function anim(){

ligne += 1;
if (joueur == 1){
    document.getElementById(choix_colonne + "" + ligne + "").innerHTML = '<img src="rouge.png" />';
} else {
    document.getElementById(choix_colonne + "" + ligne + "").innerHTML = '<img src="jaune.png" />';
}
document.getElementById(choix_colonne + "" + (ligne-1) + "").innerHTML = '<img src="trou.png" />';
document.getElementById(choix_colonne + "" + 0 + "").innerHTML = '<img src="vide.png" />';  

cas = parseInt(choix_colonne+""+ligne);

if (ligne>=6 || tabl[cas+1] != "vide") { 
    if (joueur == 1) {
        tabl[cas] = "rouge" ;
    } else {
        tabl[cas] = "jaune" ;
    }

    clearInterval(interval);

    if (joueur == 1){
        liste_rouge.push(cas);
if (detection(liste_rouge)) {

        setTimeout(function() {
        alert("Rouge gagne");
    }, 200);
}

    } else {
        liste_jaune.push(cas);
if (detection(liste_jaune)) {

       setTimeout(function() {
        alert("Jaune gagne");
    }, 200);
}

    }
    console.log(liste_rouge);
    console.log(liste_jaune);
    joueur = -joueur;
    }

}

function detection(liste) {


/* dÃ©tection verticale : */

for (var i=0;i<liste.length;i++) {

    if (liste.indexOf(liste[i]+1) !=-1 && liste.indexOf(liste[i]+2) !=-1 && liste.indexOf(liste[i]+3) !=-1) {

        return true;
    }

}

/* dÃ©tection horizontale*/

for (var i=0;i<liste.length;i++) {

    if (liste.indexOf(liste[i]+10) !=-1 && liste.indexOf(liste[i]+20) !=-1 && liste.indexOf(liste[i]+30) !=-1) {

        return true;
    }

}


/* dÃ©tection diagonale gauche*/

for (var i=0;i<liste.length;i++) {

    if (liste.indexOf(liste[i]+11) !=-1 && liste.indexOf(liste[i]+22) !=-1 && liste.indexOf(liste[i]+33) !=-1) {

        return true;
    }

}

/* dÃ©tection diagonale droite*/

for (var i=0;i<liste.length;i++) {

    if (liste.indexOf(liste[i]+9) !=-1 && liste.indexOf(liste[i]+18) !=-1 && liste.indexOf(liste[i]+27) !=-1) {

        return true;
    }

}

}

function init() {

    for(j=10;j<77;j++){ 
        tabl[j]="vide" ;
    }
}
