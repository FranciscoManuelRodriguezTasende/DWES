<?php
session_start(); // Necesario para leer $_SESSION [cite: 149]
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');

$user_id = isset($_SESSION['user_id']) ? $_SESSION['user_id'] : NULL; // [cite: 152]
$cancion_id = $_POST['cancion_id'];
$comentario = $_POST['new_comment'];

$stmt = $db->prepare("INSERT INTO tComentarios (comentario, cancion_id, usuario_id) VALUES (?, ?, ?)");
$stmt->bind_param("sii", $comentario, $cancion_id, $user_id);
$stmt->execute();

echo "Comentario añadido. <a href='main.php'>Volver</a>";
?>
