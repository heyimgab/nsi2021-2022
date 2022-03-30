<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Pizza Mendes France</title>
        <link rel="stylesheet" href="ex4style.css" />
        <link rel="icon" href="images\favicon.ico" />
    </head>

    <body>
    	<form action="ex_checkbox.php" method='get'>
	        <p>Exemple de manipulation de checbox avec PHP</p>
	        reponse1<input type="checkbox"  name="reponse[]" value="rep1"><br>
	        reponse2<input type="checkbox"  name="reponse[]" value="rep2"><br>
	        reponse3<input type="checkbox"  name="reponse[]" value="rep3"><br>
	        reponse4<input type="checkbox"  name="reponse[]" value="rep4"><br>
			<button type="submit">Envoyer</button>
		</form>
		<?php
		// si $_GET['reponse']) existe, donc si on a cliqué sur au moins un des boutons
		if (isset($_GET['reponse'])) 
		{
			// pour un input de type checbox la variable renvoyée est un tableau  (cf attribut name : "reponse[]")
			$nbreponses=count($_GET['reponse']);// longueur du tableau
			echo("<p>Vous avez coché ".$nbreponses." cases :");
			// parcours du tableau contenant les valeurs (value) des caches cochées
			for ($i=0;$i<$nbreponses;$i++)
			{
				// on affiche le ième élement du tableau
				echo ("<br> - ".$_GET['reponse'][$i]);
			}
		}
		?>
    </body>
</html>