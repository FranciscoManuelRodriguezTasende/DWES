<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');
?>
<html>
<head>
    <style>
        /* Ejercicio 7 Sprint 3: Animación hover  */
        li { transition: all 0.3s ease; padding: 10px; border-bottom: 1px solid #eee; }
        li:hover { background: #f9f9f9; transform: translateX(10px); opacity: 0.8; }
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
