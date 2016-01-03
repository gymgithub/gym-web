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

$link = "INSERT INTO Usuarios_Nutrientes ( ID, CLAVE_NUTRIENTES, PROT_GRAM_MANT, CARBO_GRAM_MANT, GRAS_GRAM_MANT, PROT_POR_MANT, CARBO_POR_MANT, GRAS_POR_MANT, PROT_GRAM_NEW, CARBO_GRAM_NEW, GRAS_GRAM_NEW, PROT_POR_NEW, CARBO_POR_NEW, GRAS_POR_NEW, FECHA ) VALUES ('$id', NULL, '$prot_gram_mant', '$carbo_gram_mant', '$gras_gram_mant', '$prot_por_mant', '$carbo_por_mant', '$gras_por_mant', '$prot_gram_new', '$carbo_gram_new', '$gras_gram_new', '$prot_por_new', '$carbo_por_new', '$gras_por_new', NULL)";
    
mysqli_query($enlace, $link) or die(mysqli_error($enlace));

// DEFINICION DE LA DIETA

//DECLARACIÓN DE CONSTANTES
define("DESAYUNO_PROT", 30);
define("DESAYUNO_CARBO", 50);
define("DESAYUNO_GRAS", 20);
define("MEDIAMAN_PROT", 10);
define("MEDIAMAN_CARBO", 10);
define("MEDIAMAN_GRAS", 25);
define("ALMUERZO_PROT", 25);
define("ALMUERZO_CARBO",30);
define("ALMUERZO_GRAS", 25);
define("MEDIATARDE_PROT", 10);
define("MEDIATARDE_CARBO", 5);
define("MEDIATARDE_GRAS", 15);
define("CENA_PROT", 25);
define("CENA_CARBO", 5);
define("CENA_GRAS", 15);

// LECTURA BASE DE DATOS DE ALIMENTOS
$alim_name  = mysqli_query($enlace, "SELECT NOMBRE FROM Alimentos") or die(mysqli_error($enlace));
$alim_prot  = mysqli_query($enlace, "SELECT GR_PROT_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));
$alim_carbo = mysqli_query($enlace, "SELECT GR_CARBO_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));
$alim_gras  = mysqli_query($enlace, "SELECT GR_GRAS_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));

$alim_name_res  = mysql_fetch_array($alim_name);
    
    
echo <<<FORMULARIO

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-e3zv{font-weight:bold}
.tg .tg-hgcj{font-weight:bold;text-align:center}
</style>
<table class="tg">
  <tr>
    <th class="tg-031e" rowspan="2"></th>
    <th class="tg-hgcj" colspan="2">LUNES</th>
  </tr>
  <tr>
    <td class="tg-031e">alimentos</td>
    <td class="tg-031e">gramos</td>
  </tr>
  <tr>
    <td class="tg-e3zv" rowspan="3">DESAYUNO</td>
    <td class="tg-031e"> 
        <input list="alimentos" name="alimentos">
        <datalist id="alimentos">
            <?php 
                foreach ($alim_name_res as $value){
                echo "$value<br>";
            } 
            ?>  
        </datalist>
    </td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-e3zv" rowspan="3">MEDIAMAÑANA</td>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
  </tr>
</table>

FORMULARIO;

echo "</pre>";

?>