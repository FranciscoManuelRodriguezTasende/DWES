<?php
// Conexión a la base de datos [cite: 105, 139]
$db = mysqli_connect('localhost', 'root', '1234', 'web_canciones') or die('Fail');

// Recuperamos las credenciales enviadas por el usuario [cite: 79-81, 106-107]
$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];

// Evitamos SQL Injection usando Prepared Statements [cite: 191-193, 214]
$stmt = $db->prepare("SELECT id, contraseña FROM tUsuarios WHERE email = ?");
$stmt->bind_param("s", $email_posted); // "s" porque el email es un string [cite: 211-212]
$stmt->execute();
$result = $stmt->get_result();

// Comprobamos si el email existe en la base de datos [cite: 91, 110, 223]
if ($row = $result->fetch_array()) {
    // Verificamos la contraseña usando la función password_verify [cite: 97, 229]
    if (password_verify($password_posted, $row['contraseña'])) {
        // Autenticación correcta: iniciamos sesión y guardamos el ID [cite: 98, 100-101]
        session_start();
        $_SESSION['user_id'] = $row['id'];
        
        // Redirigimos a la página principal [cite: 113, 220, 222]
        header('Location: main.php');
        exit();
    } else {
        // Error: Contraseña incorrecta 
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    // Error: Usuario no encontrado 
    echo '<p>Usuario no encontrado con ese email</p>';
}

$stmt->close();
mysqli_close($db);
?>
