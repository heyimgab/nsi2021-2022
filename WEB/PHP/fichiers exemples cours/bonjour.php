<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title> Bonjour </title>
    </head>
    <body>
        <h1> Petit exemple de récupération de données via la méthode GET</h1>
        
        <?php
        if  (isset($_GET['nom']) and isset($_GET['prenom']) and isset($_GET['age']))   // on vérifie que les variables GET à utiliser existent
        {
            if ($_GET['age']<18)
            {
                echo "<p>Désolé, vous ne pouvez pas rentrer: vous devez avoir plus de 18 ans.<p>";
            }
            
            else
            {
                echo "<p>Bonjour ".$_GET['prenom']." ".$_GET['nom']."</p>";
            } 
        }
        else
        {
            echo("Mais t'es qui toi ?");
        }
        ?>
       
    </body>
</html>