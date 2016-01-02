<?php
//CONEXIÓN A LA BD
include 'includes/iniciar_BD.inc.php';
$user = $_POST["user"];
$pass = $_POST["pass"];

$link = "INSERT INTO Users ( ID, EMAIL, PASS ) VALUES (NULL, '$user', '$pass')";

mysqli_query($enlace, $link);

//DECLARACIÓN DE CONSTANTES
define("PROT_STD_MAYOR25", 3);
define("CARBO_STD_MAYOR25", 2);
define("PROT_STD_MENOR25", 2.5);
define("CARBO_STD_MENOR25", 4);
//EN GRAMOS
define("PROT_CAL", 4);
define("CARBO_CAL", 4);
define("GRASA_CAL", 9);
//EN CALORÍAS POR GRAMO
$peso=$_POST["peso"];
$altura=$_POST["altura"];
    
$imc=$peso/($altura*$altura);

if($imc>=25){
    $prot_nece_gram=$peso*PROT_STD_MAYOR25;
    $carbo_nece_gram=$peso*CARBO_STD_MAYOR25*CARBO_CAL;
    $grasa_nece_gram=(($altura*100)-100)*GRASA_CAL;
    $prot_nece_cal=$prot_nece_gram*PROT_CAL;
    $carbo_nece_cal=$carbo_nece_gram*CARBO_CAL;    
    $grasa_nece_cal=$grasa_nece_gram*GRASA_CAL;    
}elseif($imc<25){
    $prot_nece_gram=$peso*PROT_STD_MENOR25;
    $carbo_nece_gram=$peso*CARBO_STD_MENOR25;
    $grasa_nece_gram=(($altura*100)-100);
    $prot_nece_cal=$prot_nece_gram*PROT_CAL;
    $carbo_nece_cal=$carbo_nece_gram*CARBO_CAL;    
    $grasa_nece_cal=$grasa_nece_gram*GRASA_CAL;  
}
//VALORES EN CALORÍAS

$cal_total=$prot_nece_cal+$carbo_nece_cal+$grasa_nece_cal;

$porcen_prot=($prot_nece_cal*100)/$cal_total;
$porcen_carbo=($carbo_nece_cal*100)/$cal_total;
$porcen_grasa=($grasa_nece_cal*100)/$cal_total;
//VALORES PORCENTUALES

echo "<pre>";
    
print_r($_POST);

echo"IMC= $imc \n";

echo "Proteínas(gramos): $prot_nece_gram gramos \n";
echo "Carbohidratos(gramos): $carbo_nece_gram gramos \n";
echo "Grasa(gramos): $grasa_nece_gram gramos \n";
echo "Proteínas: $prot_nece_cal calorías \n";
echo "Carbohidratos: $carbo_nece_cal calorías \n";
echo "Grasa: $grasa_nece_cal calorías \n";
echo "Calorías totales: $cal_total\n";
echo "%Proteínas: $porcen_prot \n";
echo "%Carbohidratos: $porcen_carbo \n";
echo "%Grasas: $porcen_grasa \n";



echo <<<FORMULARIO

<form action="proceso-pablo.php" enctype="multipart/form-data" method="post"><br>
            Nuevo porcentaje de proteína <input type="number" id="prot_new" name="prot_new"><br>
            Nuevo porcentaje de carbohidratos <input type="number" id="carbo_new" name="carbo_new"><br>
            Nuevo porcentaje de grasas <input type="number" id="grasa_new" name="grasa_new"><br>
            <input type="submit" name="enviar" id="enviar">
</form>

FORMULARIO;

echo "</pre>";
?>