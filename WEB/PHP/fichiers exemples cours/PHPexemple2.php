<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title> Moyenne </title>
        <style> 
            table
            {
                border-collapse: collapse;
            }
            th
            {
                
                border: 1px solid black
            }
        </style>
    </head>
    <body>
        <h1> un classique : calcul de moyenne</h1>
        <?php
            // code PHP
            $nom = "Job";
            $prenom ="Sébastien";
            $matieres =array('francais', 'NSI', 'Physique', 'Maths', 'NSI', 'Sport');
            $moyennes =[12, 16, 19, 20, 17, 18];

            echo ("<p>Bonjour ".$prenom." ".$nom."</p>");
        ?>
        <p>Voici vos notes :</p>
        <table >
            <tr>
                <th>Matière</th>
            <?php 
                for($i=0;$i<sizeof($matieres);$i++)
                {
                    echo("<th>".$matieres[$i]."</th>");
                }
            ?>
            </tr>
            <tr>
                <th>Moyenne</th>
            <?php 
                $moygale=0;
                for($i=0;$i<sizeof($moyennes);$i++)
                {
                    $moygale=$moygale+$moyennes[$i];
                    echo("<th>".$moyennes[$i]."</th>");
                }
                $moygale=$moygale/sizeof($moyennes);
            ?>            
            </tr>
        </table>

        <?php

            echo("<p> Votre moyenne générale est de :".$moygale); 
            if ($moygale>12)
            {
                echo("<p> Bravo, avec cette moyenne, vous obtiendriez une mention au bac.</p>");
            }
            elseif ($moygale>10)
            {
                echo("<p> Avec cette moyenne, vous obtiendriez votre bac.</p>");
            }
            else
            {
                echo("<p>Attention, avec cette moyenne, vous n'auriez pas votre bac.</p>");
            }
        ?>
    </body>
</html>