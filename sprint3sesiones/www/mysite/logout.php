<?php
session_start();
session_destroy(); // Borra la sesión [cite: 176]
header('Location: login.html'); // Redirige [cite: 177]
?>
