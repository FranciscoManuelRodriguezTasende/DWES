<?php
session_start();

// 1. Verificar que el usuario tiene una sesión activa [cite: 150]
if (empty($_SESSION['user_id'])) {
    die("Debes iniciar sesión para cambiar tu contraseña. <a href='login.html'>Ir al login</a>");
}

$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');
$user_id = $_SESSION['user_id'];

// 2. Recuperar datos del formulario
$old_pass = $_POST['f_old_pass'];
$new_pass = $_POST['f_new_pass'];
$new_pass_repeat = $_POST['f_new_pass_repeat'];

// 3. Validar que las nuevas contraseñas coincidan
if ($new_pass !== $new_pass_repeat) {
    die("Error: Las nuevas contraseñas no coinciden. <a href='changepassword.html'>Volver</a>");
}

// 4. Obtener la contraseña actual de la base de datos para verificarla
$stmt = $db->prepare("SELECT contraseña FROM tUsuarios WHERE id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_assoc();

// 5. Verificar la contraseña antigua 
if (password_verify($old_pass, $row['contraseña'])) {
    // 6. Si es correcta, hashear la nueva contraseña 
    $new_hash = password_hash($new_pass, PASSWORD_DEFAULT);
    
    // 7. Actualizar la base de datos [cite: 193]
    $update_stmt = $db->prepare("UPDATE tUsuarios SET contraseña = ? WHERE id = ?");
    $update_stmt->bind_param("si", $new_hash, $user_id);
    $update_stmt->execute();
    
    echo "Contraseña actualizada con éxito. <a href='main.php'>Volver al inicio</a>";
    $update_stmt->close();
} else {
    echo "Error: La contraseña actual es incorrecta. <a href='changepassword.html'>Reintentar</a>";
}

$stmt->close();
mysqli_close($db);
?>
