<!DOCTYPE html>
<html lang="en">
    
<head>
<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/jquery.reject.min.js"></script>
	<script type="text/javascript" src="js/jquery.reject.options.js"></script>
	
   	


	<!-- Basic Page Needs
  ================================================== -->
	
	<meta name="description" />
	<meta name="author" />

	<!-- Mobile Specific Metas
  ================================================== -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
	<link rel="shortcut icon" href="" />

	<!-- CSS
  ================================================== -->
	<link rel="stylesheet" type="text/css" href="css/EstilosTa.css" />
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script src='ajax.js'></script>
	<title>SIGE</title>
  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  
</head>

<?php $codigo_est = 11111; ?>
<body  onload="traerDatos(<?php 
echo $codigo_est; ?>);" >
<div id="antorcha"></div>
	<div id="bandera"></div>

<header>
		<a href="http://www.unicauca.edu.co" id="logoU"></a>
		<p class="separador"></p>
		<p id="desc">Sistema Integrado de gestión de electivas</p>
</header>
<div class="container">
  <h1>Salas y salones disponibles </h1>
  <h2>Agrega tu horario</h2>
  <h2>Electiva -- </h2>
  <div class="login-form">
    <form action="" method="post">
    <div id = "contenido" class="contenidoT">	  
    
    
    </div>
      <button type="submit" class="btn btn-primary btn-lg   " >Guardar</button>
    </form>
  </div>
  <!-- Footer -->
  <footer>
		<p>2019  | Grupo de trabajo Dragones Infernales  <br />
			<a href="http://www.unicauca.edu.co">Universidad del Cauca</a>  | Versión: 1.0  <br /><span style="display: none"></span> 
		</p>
	</footer>
	
  </div>
</body>

</html>
