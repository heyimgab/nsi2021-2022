<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
</head>

<body>
  <?php

  $nombre_pique = $_GET['nbPique'];
  if ($nombre_pique != "" && $nombre_pique != 0) {
    echo $nombre_pique . ' pizzas qui pique pour ' . $nombre_pique * 12 . ' eu</br>';
  }

  $nombre_fromage = $_GET['nbFromage'];
  if ($nombre_fromage != "" && $nombre_fromage != 0) {
    echo $nombre_fromage . ' pizzas beaucoup de fromage pour ' . $nombre_fromage * 10 . ' eu</br>';
  }

  $nombre_pas_chere = $_GET['nbPasChere'];
  if ($nombre_pas_chere != "" && $nombre_pas_chere != 0) {
    echo $nombre_pas_chere . ' pizzas pas chere pour ' . $nombre_pas_chere * 6 . ' eu</br></br></br>';
  }

  echo '</br></br>';
  $nombre_pizza_sur_mesure = $_GET['nbmesure'];
  $base_pizza = $_GET['base'];
  $viande_pizza = $_GET['viande'];
  $legume_pizza = $_GET['legume'];

  if ($nombre_pizza_sur_mesure != "" && $nombre_pizza_sur_mesure != 0) {
    $prix = 0;
    echo 'PIZZAS SUR MESURE:</br></br>';

    if ($base_pizza == "saucetomate") {
      echo 'BASE TOMATE</br>';
      $prix = $prix + 6;
    }
    if ($base_pizza == "creme") {
      echo 'BASE CREME</br>';
      $prix = $prix + 6;
    }

    $prix += (2 * count($viande_pizza));
    $prix += (0.5 * count($legume_pizza));

    echo '</br>VIANDES:</br>';
    foreach ($viande_pizza as &$value){
      switch ($value) {
        case "jambon":
          echo 'JAMBON</br>';
          break;
        case "lard":
          echo 'LARD</br>';
          break;
        case "chorizo":
          echo 'CHORIZO</br>';
          break;
        case "saumon":
          echo 'SAUMON</br>';
          break;
      }
    }

    echo '</br>LEGUMES:</br>';
    foreach ($legume_pizza as $key => $value) {
      switch ($value) {
        case "tomate":
          echo 'TOMATE</br>';
          break;
        case "oignon":
          echo 'OIGNON</br>';
          break;
        case "poivron":
          echo 'POIVRONS</br>';
          break;
        case "champignon":
          echo 'CHAMPIGNONS</br>';
          break;
        case "artichaud":
          echo 'ARTICHAUDS</br>';
          break;
        case "roquette":
          echo 'ROQUETTES</br>';
          break;
        case "brocoli":
          echo 'BROCOLIS</br>';
          break;
        case "aubergine":
          echo 'AUBERGINES</br>';
          break;
      }
    }

    echo '</br>Prix des pizza perso:' . ($nombre_pizza_sur_mesure * $prix) . ' eu soit ' . $nombre_pizza_sur_mesure . ' pizzas sur mesure</br>';
  }
  echo '</br></br></br>';

  if (($nombre_pizza_sur_mesure * $prix > 0) && ($nombre_pique * 12 + $nombre_fromage * 10 + $nombre_pas_chere * 6 > 0)) {
    echo 'TOTAL: ' . ($nombre_pizza_sur_mesure * $prix) + ($nombre_pique * 12 + $nombre_fromage * 10 + $nombre_pas_chere * 6) . ' eu';
  }
  ?>
  <html>