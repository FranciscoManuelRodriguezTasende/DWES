<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');

if (!isset($_GET['cancion_id'])) { die('No se ha especificado canción'); }
$cancion_id = $_GET['cancion_id'];

// Obtener datos de la canción [cite: 353, 354]
$stmt = $db->prepare("SELECT * FROM tCancion WHERE id = ?");
$stmt->bind_param("i", $cancion_id);
$stmt->execute();
$cancion = $stmt->get_result()->fetch_assoc();
?>
<html>
<body>
    <h1><?php echo $cancion['titulo']; ?></h1>
    <p>Artista: <?php echo $cancion['artista']; ?> | Año: <?php echo $cancion['año']; ?></p>
    <a href="main.php">Volver</a>

    <h3>Comentarios:</h3>
    <ul>
        <?php
        // Mostramos comentario y fecha [cite: 499]
        $query2 = "SELECT * FROM tComentarios WHERE cancion_id = $cancion_id";
        $result2 = mysqli_query($db, $query2);
        while ($row = mysqli_fetch_array($result2)) {
            $user = $row['usuario_id'] ? "Usuario #".$row['usuario_id'] : "Anónimo";
            echo "<li><strong>$user</strong> (".$row['fecha']."): ".$row['comentario']."</li>";
        }
        ?>
    </ul>

    <hr>
    <form action="comment.php" method="post">
        <input type="hidden" name="cancion_id" value="<?php echo $cancion_id; ?>">
        <textarea name="new_comment" placeholder="Escribe tu comentario..." required></textarea><br>
        <input type="submit" value="Comentar">
    </form>
</body>
</html>
