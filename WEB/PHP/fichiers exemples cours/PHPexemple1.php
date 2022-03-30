<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title> Horloge </title>
    </head>
<body>
    <h1> Heure du serveur</h1>
 

    <?php
        // code PHP
        $heure = date("H:i:s");
        echo ("<p>D'après votre serveur PHP, Il est $heure.</p>");
    ?>
    <!-- reprise du code HTML -->
    <p>Remarques :</p>
    <ol>
        <li> Vous pouvez vous rendre compte que WAMP par défaut n'est pas réglé sur le fuseau horaire français. Pour modifier cela,  icône WAMP, PHP, configuration PHP,date.timezone puis choisissez Europe/Paris</li>
        <li>Avec cette instruction, si votre fichier PHP était hébergé dans un serveur située en Californie, vous verriez s'afficher l'heure de Californie !</li>
    </ol>
</body>
</html>