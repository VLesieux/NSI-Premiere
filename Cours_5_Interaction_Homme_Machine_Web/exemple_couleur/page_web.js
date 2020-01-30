document.getElementById("executer").addEventListener("click", myFunction);

function myFunction() {
document.getElementById("demo").innerHTML = 'Vous avez décidé de colorier le fond en : <b>'+ document.getElementById('couleur_fond').value+ '</b>, le texte en : <b>'+ document.getElementById('couleur_texte').value +'</b> et la bordure en : <b>'+ document.getElementById('couleur_bordure').value+'</b>';

document.getElementById('zone').style.backgroundColor= document.getElementById('couleur_fond').value;

document.getElementById('zone').style.color= document.getElementById('couleur_texte').value;

document.getElementById('zone').style.borderColor= document.getElementById('couleur_bordure').value;
}