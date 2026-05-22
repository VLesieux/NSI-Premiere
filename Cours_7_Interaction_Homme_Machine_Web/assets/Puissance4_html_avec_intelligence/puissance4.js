/* =====================Déclaration des variables======================== */
var interval;
var choix_colonne;
var ligne;
var table = [];//représente le plateau de jeu
var liste_rouge = [];//liste des positions occupées par les jetons rouges
var liste_jaune = [];//liste des positions occupées par les jetons jaunes
var cas;
var joueur;
joueur = 1;
var animationEnCours = false;

/* =====================Initialisation de la partie======================== */

init();

/* =====================SELECTION D'UNE COLONNE LORS DU SURVOL======================== */
//Rappel : chiffre des dizaines = colonne à partir de 1 ; chiffre des unités = ligne à partir de 0

function selection(colonne){

    for (j=1;j<=7;j++) {//parcours des colonnes à partir de 1 jusque 7 compris
        for(i=0;i<=6; i++) {//parcours des lignes à partir de 0 jusque 6 compris
            document.getElementById(j+""+i+"").style.opacity= '1';
            document.getElementById(j + "" + 0 + "").innerHTML = '<img src="vide.png" />';
            //on met du vide sur la première ligne
        }
    }

    for (i=0;i<=6; i++) {

        document.getElementById(colonne+""+i+"").style.opacity = '0.7';
        //on rend la colonne choisie de plus faible opacité pour la distinguer
        if (joueur == 1) {
            document.getElementById(colonne + "" + 0 + "").innerHTML = '<img src="rouge1.png" />';
        //dans la première ligne, on met un jeton rouge
        } else {
            document.getElementById(colonne + "" + 0 + "").innerHTML = '<img src="jaune1.png" />';
        //dans la première ligne, on met un jeton jaune
        }
    }
}

/* =====================EFFET DU CLIC SUR UNE COLONNE#======================== */
function jeu(colonne){

    if(animationEnCours) return;//le clic sur la colonne est inactif au cours de l'animation

    choix_colonne = colonne;
    ligne = 0;

    if(table[choix_colonne+""+1] == "vide"){
// On vérifie que la colonne n'est pas pleine
// (la case supérieure du plateau réel doit être libre).
        animationEnCours = true;//l'animation peut être lancée
        interval = setInterval(anim,150);//l'animation se poursuit toutes les 150 ms
    } else {
        alert("Coup impossible");//alert lance un message d'erreur à l'écran
    }
}

/* =====================L'ANIMATION QUI FAIT DESCENDRE LE JETON======================== */
function anim(){

    ligne += 1;//on descend d'une ligne à chaque fois que anim est lancé

    if (joueur == 1){
        document.getElementById(choix_colonne + "" + ligne).innerHTML = '<img src="rouge.png" />';
        //on utilise une image de jeton rouge qui s'insère dans le plateau

    } else {
        document.getElementById(choix_colonne + "" + ligne).innerHTML = '<img src="jaune.png" />';
        //on utilise une image de jeton jaune qui s'insère dans le plateau
    }

    document.getElementById(choix_colonne + "" + (ligne-1)).innerHTML = '<img src="trou.png" />';
    //on met un trou à la ligne précédente dans cette colonne
    document.getElementById(choix_colonne + "" + 0).innerHTML = '<img src="vide.png" />';
    //on met un vide à la première ligne dans cette colonne

    cas = parseInt(choix_colonne + "" + ligne);
    // Construction de l'identifiant de la case
    // (exemple : colonne 3, ligne 5 → case 35).

    if (ligne>=6 || table[cas+1] != "vide") {
// Le jeton s'arrête s'il atteint le bas du plateau
// ou si la case située juste en dessous est déjà occupée.

        if (joueur == 1) {
            table[cas] = "rouge";
        } else {
            table[cas] = "jaune";
        }

        clearInterval(interval);

        if (joueur == 1){

            liste_rouge.push(cas);//push est l'équivalent de append en JavaScript

if (detection(liste_rouge)) {//détection d'un alignement pour les rouges
    setTimeout(function() {
        alert("Rouge gagne");
    }, 200);//affichage d'alerte après 200 ms

    animationEnCours = false;//fin de l'animation
    return;
}

        } else {

            liste_jaune.push(cas);

if (detection(liste_jaune)) {//détection d'un alignement pour les jaunes
    setTimeout(function() {
        alert("Jaune gagne");
    }, 200);//affichage d'alerte après 200 ms

    animationEnCours = false;//fin de l'animation
    return;
}
        }

        joueur = -joueur;//changement du joueur
        animationEnCours = false;//fin de l'animation

        // CAS DU TOUR DE LA MACHINE
        if(joueur == -1){
            setTimeout(jouerMachine, 500);
        }
    }
}

/* =====================LA DETECTION DES CAS GAGNANTS======================== */

function detection(liste) {//la détection est faite sur liste_rouge et sur liste_jaune

    // la verticale
    for (var i=0;i<liste.length;i++) {
        if (//on regarde si les trois suivants consécutifs sont dans la liste
            liste.indexOf(liste[i]+1) !=-1 &&
            liste.indexOf(liste[i]+2) !=-1 &&
            liste.indexOf(liste[i]+3) !=-1
        ) {
            return true;
        }
    }

    // l'horizontale
    for (var i=0;i<liste.length;i++) {
        if (//on regarde si les trois suivants en ajoutant à chaque fois 10 sont dans la liste
            liste.indexOf(liste[i]+10) !=-1 &&
            liste.indexOf(liste[i]+20) !=-1 &&
            liste.indexOf(liste[i]+30) !=-1
        ) {
            return true;
        }
    }

    // la diagonale gauche
    for (var i=0;i<liste.length;i++) {
        if (//on regarde si les trois suivants en ajoutant à chaque fois 11 sont dans la liste
            liste.indexOf(liste[i]+11) !=-1 &&
            liste.indexOf(liste[i]+22) !=-1 &&
            liste.indexOf(liste[i]+33) !=-1
        ) {
            return true;
        }
    }

    // la diagonale droite
    for (var i=0;i<liste.length;i++) {
        if (//on regarde si les trois suivants en ajoutant à chaque fois 9 sont dans la liste
            liste.indexOf(liste[i]+9) !=-1 &&
            liste.indexOf(liste[i]+18) !=-1 &&
            liste.indexOf(liste[i]+27) !=-1
        ) {
            return true;
        }
    }

    return false;
}

// Initialise toutes les cases du plateau à l'état "vide".

function init() {

    for(j=10;j<77;j++){
        table[j] = "vide";
    }
}

/* ========================================================= */
/* ===================== IA MINIMAX ======================== */
/*
MinMax sert à choisir le meilleur coup pour l’ordinateur.
L’algorithme simule plusieurs coups possibles à l’avance :
- quand c’est le tour de l’ordinateur, il choisit le coup qui donne le meilleur score ;
- quand c’est le tour de l’adversaire, il suppose que celui-ci choisira le coup le plus dangereux.
Le but est donc de maximiser les chances de l’ordinateur tout en minimisant celles de l’adversaire.
*/
/* ========================================================= */

/* =========================RECHERCHE DES COUPS POSSIBLES=============== */

function coupsPossibles(){

    var coups = [];

    for(var c=1;c<=7;c++){
        if(table[c+""+1] == "vide"){
            coups.push(c);
        }
    }

// Une colonne est jouable si sa case supérieure
// (11, 21, 31...) est encore vide.
return coups;

}
/* ========================= COPIE DU TABLEAU=============== */
// Crée une copie indépendante du plateau
// afin que Minimax puisse simuler des coups sans modifier le vrai jeu.

function copierTableau(obj){
    return JSON.parse(JSON.stringify(obj));
}

/* ========================= RECHERCHE DE LA LIGNE OÙ TOMBE LE JETON =============== */

function trouverLigne(colonne, plateau){

    for(var l=6;l>=1;l--){//on part du bas vers le haut

        var caseID = parseInt(colonne + "" + l);

        if(plateau[caseID] == "vide"){
            return l;//on renvoie la ligne dès que l'on tombe sur du vide
        }
    }

    return null;
}
/* ========================= SIMULATION D'UN COUP =============== */

function simulerCoup(colonne, couleur, plateau){//renvoie l'état du plateau sur une copie

    var nouveau = copierTableau(plateau);

    var l = trouverLigne(colonne, nouveau);

    if(l == null) return null;

    var caseID = parseInt(colonne + "" + l);

    nouveau[caseID] = couleur;

    return nouveau;
}
/* ========================= LISTES DES POSITIONS OCCUPÉEs PAR LES ROUGES ET LES JAUNES =============== */

function listeCouleur(plateau, couleur){

    var liste = [];

    for(var i in plateau){
        if(plateau[i] == couleur){
            liste.push(parseInt(i));
        }
    }

    return liste;//renvoie la liste des positions occupées par les jetons rouges ou jaunes
}

/* ========================= FONCTION D'ÉVALUATION =============== */


function compterAlignements(plateau, couleur, taille){

    var total = 0;

    var directions = [1,10,11,9];

    for(var caseID in plateau){

        caseID = parseInt(caseID);

        if(plateau[caseID] != couleur) continue;

        for(var d=0; d<directions.length; d++){

            var direction = directions[d];
            var ok = true;

            for(var k=1; k<taille; k++){

                var suivante = caseID + direction*k;

                if(plateau[suivante] != couleur){
                    ok = false;
                    break;
                }
            }

            if(ok){
                total++;
            }
        }
    }

    return total;
}

function evaluation(plateau){

// Attribue un score au plateau.
// Plus le score est élevé, plus la position est favorable à la machine (jaune).
// Version simple : compte uniquement le nombre de jetons.

    var score = 0;

    // bonus centre

    if(plateau[43]=="jaune") score += 3;

    // alignements

    score += compterAlignements(plateau,"jaune",3)*50;

    score += compterAlignements(plateau,"jaune",2)*10;

    score -= compterAlignements(plateau,"rouge",3)*50;

    score -= compterAlignements(plateau,"rouge",2)*10;

    return score;

}
/* ========================= FONCTION MINIMAX =============== */
function minimax(plateau, profondeur, maximisant){
//maximisant vaut true pour les jaunes (machine)
// et false pour les rouges (joueur humain)
// Explore récursivement les coups possibles jusqu'à une profondeur donnée
// puis renvoie le score estimé du plateau obtenu.

    var jaune = listeCouleur(plateau, "jaune");
    var rouge = listeCouleur(plateau, "rouge");

    if(detection(jaune)) return 1000;
    if(detection(rouge)) return -1000;

    if(profondeur == 0){
//la condition d'arrêt qui permet de sortir de la fonction récursive
// on limite la profondeur de recherche
// pour éviter une récursion infinie et réduire le temps de calcul

        return evaluation(plateau);
    }

    var coups = [];

    for(var c=1;c<=7;c++){
        if(plateau[c+""+1] == "vide"){
            coups.push(c);
        }
    }

    if(maximisant){//    maximisant == true → joue JAUNE (la machine)

        var meilleur = -9999;

        for(var i=0;i<coups.length;i++){

            var nouveau = simulerCoup(coups[i], "jaune", plateau);

            var val = minimax(nouveau, profondeur-1, false);//fonction récursive

            if(val > meilleur){
                meilleur = val;
            }
        }

        return meilleur;

    } else {//    maximisant == false → joue ROUGE (l’humain)

        var meilleur = 9999;

        for(var i=0;i<coups.length;i++){

            var nouveau = simulerCoup(coups[i], "rouge", plateau);

            var val = minimax(nouveau, profondeur-1, true);

            if(val < meilleur){
                meilleur = val;
            }
        }

        return meilleur;
    }
}
/* ========================= FONCTION COUP MACHINE =============== */
function coupMachineMinimax(){
// Teste chaque colonne disponible
// et conserve celle qui obtient le meilleur score Minimax.

    var coups = coupsPossibles();

    var meilleurScore = -9999;
    var meilleurCoup = coups[0];

    for(var i=0;i<coups.length;i++){

        var nouveau = simulerCoup(coups[i], "jaune", table);

        var score = minimax(nouveau, 3, false);

        // exploration sur 3 coups d'avance

        if(score > meilleurScore){
            meilleurScore = score;
            meilleurCoup = coups[i];
        }
    }

    return meilleurCoup;
}

// Lance automatiquement le tour de l'ordinateur.
function jouerMachine(){

    var colonne = coupMachineMinimax();

    jeu(colonne);
}