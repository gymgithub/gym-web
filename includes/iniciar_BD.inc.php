<?php
//Conectar con el servidor de mysql
$enlace = mysqli_connect('db4free.net', 'gymweb', 'oYMP8O3H9k', 'gymweb');

//Comprobar si se ha realizado bien la conexión
if (!$enlace) {
    die('Error de Conexión'. mysqli_connect_error());
}
//para que saque la configuracion con los acentos y caracteres raros
//mysqli_query($enlace, "SET NAMES 'utf8'");
?>