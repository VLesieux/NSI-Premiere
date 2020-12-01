
document.getElementById("executer").addEventListener("click", action);

function action() {
  document.getElementById("demo").innerHTML = document.getElementById("montant").value*document.getElementById("taux").value
}
