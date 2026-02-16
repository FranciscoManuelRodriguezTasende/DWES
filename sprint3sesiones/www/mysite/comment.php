<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');

$comentario = $_POST['new_comment'];
$cancion_id = $_POST['cancion_id'];
$usuario_id = isset($_SESSION['user_id']) ? $_SESSION['user_id'] : NULL;

// Inserción preparada para seguridad [cite: 200, 214]
$stmt = $db->prepare("INSERT INTO tComentarios (comentario, cancion_id, usuario_id) VALUES (?, ?, ?)");
$stmt->bind_param("sii", $comentario, $cancion_id, $usuario_id);
$stmt->execute();

echo "Comentario añadido con éxito. <a href='detail.php?cancion_id=$cancion_id'>Volver</a>";
mysqli_close($db); [cite: 449]
?>
