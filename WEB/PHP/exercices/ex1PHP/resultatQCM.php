<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>résultat QCM</title>
    </head>

    <body>
        <h2>  QCM PHP : résultats</h2>

        <p> Voici votre résultat :</p>

        <php
        // tableau associatif des bonnes réponses
        $correctes=["q1"=>"rep12","q2"=>";","q3"=>"rep32","q4"=>["rep43","rep44"],"q5"=>"\$_POST","q6"=>"rep63"]

        // calcul des points correspondant aux réponses du QCM
        resultat=0;
        foreach ($_POST as $question => $reponse) {
            if ($reponse==$correctes[$question])
            {
                resultat+=1;
                echo "Question $question : réponse correcte<br> ";
            }
            else 
            {
                echo "Question $question : réponse fausse<br> ";
            }
        }
        echo (<p>Vous avez obtenu $resultat /6<p>);
        
        // commentaires sur le résultat

        ?>
    </body>
</html>
   