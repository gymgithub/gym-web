<?php

echo "<pre>";
    
print_r($_POST);

echo"</pre>";
//CONEXIÓN A LA BD
include 'includes/iniciar_BD.inc.php';
$email           = $_POST["email"];
$prot_gram_mant  = $_POST["prot_gram_mant"];
$carbo_gram_mant = $_POST["carbo_gram_mant"];
$gras_gram_mant  = $_POST["gras_gram_mant"];
$prot_por_mant   = $_POST["prot_por_mant"];
$carbo_por_mant  = $_POST["carbo_por_mant"];
$gras_por_mant   = $_POST["gras_por_mant"];
$prot_por_new    = $_POST["prot_por_new"];
$carbo_por_new   = $_POST["carbo_por_new"];
$gras_por_new    = $_POST["grasa_por_new"];

$gram_total = $prot_gram_mant + $carbo_gram_mant + $gras_gram_mant;

$prot_gram_new  = $gram_total * ($prot_por_new/100);
$carbo_gram_new = $gram_total * ($carbo_por_new/100);
$gras_gram_new  = $gram_total * ($gras_por_new/100);

$linkid = "SELECT ID FROM Users WHERE EMAIL='$email'";
$result = mysqli_query($enlace, $linkid) or die(mysqli_error($enlace));
$res    = mysqli_fetch_assoc($result);
$id     = $res["ID"];

echo "<pre>";
    
print_r($result);

echo"</pre>";

$link = "INSERT INTO Usuarios_Nutrientes ( ID, CLAVE_NUTRIENTES, PROT_GRAM_MANT, CARBO_GRAM_MANT, GRAS_GRAM_MANT, PROT_POR_MANT, CARBO_POR_MANT, GRAS_POR_MANT, PROT_GRAM_NEW, CARBO_GRAM_NEW, GRAS_GRAM_NEW, PROT_POR_NEW, CARBO_POR_NEW, GRAS_POR_NEW, FECHA ) VALUES ('$id', NULL, '$prot_gram_mant', '$carbo_gram_mant', '$gras_gram_mant', '$prot_por_mant', '$carbo_por_mant', '$gras_por_mant', '$prot_gram_new', '$carbo_gram_new', '$gras_gram_new', '$prot_por_new', '$carbo_por_new', '$gras_por_new', NULL)";
    
mysqli_query($enlace, $link) or die(mysqli_error($enlace));

?>
