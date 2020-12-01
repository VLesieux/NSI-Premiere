valeurs=["7","8","9","DEL","AC","4","5","6","*","/","1","2","3","+","-","0",".","**","(-)","EXE","(",")"]
var calcul="";

function action(x) {
calcul=calcul+valeurs[x];
document.getElementById("ecriture").innerHTML = calcul;
}	

function efface() {
calcul=""
document.getElementById("ecriture").innerHTML = "";
}


function resultat() {
calcul=calcul+"="+eval(calcul);
document.getElementById("ecriture").innerHTML = calcul;
}

function supprime() {
calcul=calcul.slice(0, -1);
document.getElementById("ecriture").innerHTML = calcul;
}

function inverse() {
calcul="-"+calcul;
document.getElementById("ecriture").innerHTML = calcul;
}