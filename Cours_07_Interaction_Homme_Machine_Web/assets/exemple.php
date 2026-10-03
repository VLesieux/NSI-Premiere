<?php
$r=$_GET["r"];
$g=$_GET["g"];
$b=$_GET["b"];
$rgb="rgb(".$r.",".$g.",".$b.")";
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<style>
#couleur {
	
width: 100px;
height: 100px;
border:1 px solid black;
}
</style>
</head>
<body>
<form>
	R: <input type="text" name="r" id="r"></input><br/>
	G: <input type="text" name="g" id="g"></input><br/>
	R: <input type="text" name="b" id="b"></input><br/>
<button id="bouton">Afficher</button>
</form>
<div id="couleur">
<?php echo "style='background:".$rgb."'"; ?>
</div>
</body>
</html>
