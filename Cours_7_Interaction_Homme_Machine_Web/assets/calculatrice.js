

function ajout_calcul(j) {
ligne+=j
console.log(ligne);
}


function evaluer() {
resultat=eval(ligne);
console.log(resultat);
ligne=""

document.getElementById("affichage").innerHTML=resultat

}


function erase_dernier() {
ligne=ligne.slice(0, -1);
console.log(ligne);
}

function erase_tout() {
ligne="";
console.log(ligne);
}

function memorise() {
ligne+=resultat
console.log(ligne);
}

function signe() {
	
}