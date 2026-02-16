<?php
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');
$email = $_POST['f_email'];
$pass = $_POST['f_password'];
$pass_conf = $_POST['f_password_repeat'];

// Validaciones básicas [cite: 219]
if (empty($email) || empty($pass)) { die("Error: campos vacíos"); }
if ($pass !== $pass_conf) { die("Error: las contraseñas no coinciden"); }

// Comprobar si el email ya existe [cite: 219]
$stmt = $db->prepare("SELECT id FROM tUsuarios WHERE email = ?");
$stmt->bind_param("s", $email);
$stmt->execute();
if ($stmt->get_result()->num_rows > 0) { die("Error: el email ya existe"); }

// Cifrar y guardar 
$hash = password_hash($pass, PASSWORD_DEFAULT);
$stmt = $db->prepare("INSERT INTO tUsuarios (email, contraseña) VALUES (?, ?)");
$stmt->bind_param("ss", $email, $hash);
$stmt->execute();

header('Location: main.php'); // Redirige al finalizar [cite: 220]
?>
