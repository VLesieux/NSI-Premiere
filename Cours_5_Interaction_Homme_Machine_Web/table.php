<html>
<head>
<title>Table</title>
</head>
<body>
<form action='table.php'>
	valeur :
	<input type="text" name='valeur'/>
	<button type='submit'>calculer</button>
</form>

<ul>
<?php
if (isset($_GET['valeur'])) {
	$valeur=$_GET['valeur'];
}
 else {
 $valeur=10;
 }

 for ($i=0; $i<=10;$i=$i+1) {

 	$style='';
 	if ($i %2 !=0) {
 		$style='background:gray;color:white'
 	}
 	echo '<li style=' ".$style."'>';
 	echo $valeur.'*'.$i.'='.($valeur*$i) 
 	echo '</li>\n'


 }
 ?>
</ul>
</body>
</html>