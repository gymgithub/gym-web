<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php
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

//CONEXIÓN A LA BD
include 'includes/iniciar_BD.inc.php';

// LECTURA BASE DE DATOS DE ALIMENTOS

/*$consulta   = "SELECT NOMBRE FROM Alimentos";
$alim_name  = mysqli_query($enlace, $consulta) or die(mysqli_error($enlace));
$alim_prot  = mysqli_query($enlace, "SELECT GR_PROT_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));
$alim_carbo = mysqli_query($enlace, "SELECT GR_CARBO_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));
$alim_gras  = mysqli_query($enlace, "SELECT GR_GRAS_100GRPROD FROM Alimentos") or die(mysqli_error($enlace));*/    
?>

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
                $consulta   = "SELECT NOMBRE FROM Alimentos";
                $alim_name  = mysqli_query($enlace, $consulta) or die(mysqli_error($enlace));
                        while ($fila = mysqli_fetch_array($alim_name)) {
                            echo "<option value=\"$fila[0]\">$fila[0]</option>";
                        }
                mysqli_free_result($alim_name);
                mysqli_close($enlace);  
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
</body>
</html>
