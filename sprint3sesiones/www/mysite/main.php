<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');
?>
<html>
<body>
    <h1>Web de Canciones</h1>

    <?php
    // Comprobamos si el usuario está logueado para mostrar opciones [cite: 179, 232]
    if (isset($_SESSION['user_id'])) {
        echo "<p>Identificado como usuario: " . $_SESSION['user_id'] . "</p>";
        echo "<a href='changepassword.html'>Cambiar contraseña</a> | ";
        echo "<a href='logout.php'>Cerrar sesión</a>";
    } else {
        echo "<a href='login.html'>Iniciar sesión</a> | <a href='register.html'>Registrarse</a>";
    }
    ?>

    <h3>Lista de canciones:</h3>
    <ul>
        <?php
        // Listado básico del Sprint 2 [cite: 298-301]
        $query = "SELECT * FROM tCancion";
        $result = mysqli_query($db, $query);
        while ($row = mysqli_fetch_array($result)) {
            // Enlace dinámico a la página de detalle [cite: 487-488]
            echo "<li><a href='detail.php?cancion_id=".$row['id']."'>";
            echo $row['titulo'];
            echo "</a></li>";
        }
        ?>
    </ul>

    <?php mysqli_close($db); ?>
</body>
</html>
