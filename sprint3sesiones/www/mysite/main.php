<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');
?>
<html>
<head>
	<style>
li {
    transition: all 0.3s ease; /* Transición suave [cite: 238] */
}
li:hover {
    opacity: 0.7;
    transform: translateX(10px); /* Pequeño desplazamiento al pasar el ratón */
}
</style>
</head>
<body>
    <h1>Canciones Disponibles</h1>
    
    <?php if (isset($_SESSION['user_id'])): ?>
        <p>Conectado como ID: <?php echo $_SESSION['user_id']; ?> | <a href="logout.php">Logout</a></p>
    <?php else: ?>
        <p><a href="login.html">Login</a> | <a href="register.html">Registro</a></p>
    <?php endif; ?>

    <ul>
        <?php
        $query = "SELECT * FROM tCancion";
        $result = mysqli_query($db, $query);
        // Recorrer el resultado con while 
        while ($row = mysqli_fetch_array($result)) {
            echo "<li>";
            echo "<a href='detail.php?cancion_id=".$row['id']."'>";
            echo $row['titulo']." (".$row['artista'].")"; // Acceso por nombre de columna [cite: 315]
            echo "</a></li>";
        }
        ?>
    </ul>
</body>
</html>
