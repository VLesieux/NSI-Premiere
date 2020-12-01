

var inconnu=Math.floor(Math.random()*100)

var compteur=0


document.getElementById("executer").addEventListener("click", action);

function action() {

compteur+=1;


console.log(inconnu,compteur)

if (compteur>=10) {document.getElementById("demo").innerHTML = "Perdu, vous avez dépassé les 10 propositions"}


else {

if (document.getElementById("proposition").value<inconnu)

{
  document.getElementById("demo").innerHTML = "Trop bas !"
}

if (document.getElementById("proposition").value>inconnu)

{
  document.getElementById("demo").innerHTML = "Trop grand !"
}


if (document.getElementById("proposition").value==inconnu)

{
  document.getElementById("demo").innerHTML = "Bravo, vous avez trouvé "+" en "+compteur+ " coups !"
}


}







}
