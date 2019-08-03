
function traerDatos(codigo_est){
    console.log(codigo_est);
    console.log('dentro de la funcion');

    const xhttp = new XMLHttpRequest();
    
    xhttp.onreadystatechange = function (){
        if(this.readyState == 4 && this.status == 200 ){
            miFuncion(this);
        }
    };
    xhttp.open('GET','./horarioSalons.json',true);

    xhttp.send();

    function miFuncion(json){
            var datos1 
            datos1 = JSON.parse(json.responseText);
            
            let contenedor = document.getElementById('contenido');  
            contenedor.innerHTML = generar_html(datos1);
            
            var materias = document.querySelectorAll(".materia");        
            materias.forEach((materia) => {
                materia.addEventListener('click', () => {                
                    var id = $(materia).attr("id");
                    var res = modificar_estado_materia(codigo_est, id);
                    materia.classList.toggle('active');                
                });
            });
            
        
    }
}
function generar_html(datos){
    let hora=5;
    let aux="am";
    var clase = "materia active";
    var bandera=0;
    nuevo_html = '';

    nuevo_html = `<table id="mitabla" class="table table-bordered table-responsive mb-4">
              
      <tr  class="table-warning ">
          <th>Hora</th>
          <th>Lunes</th>
          <th>Martes</th>
          <th>Miercoles</th>
          <th>Jueves</th>
          <th>Viernes</th>
          <th>Sabado</th>
      </tr>
      <tbody>`
    for (var i = 1; i <8; i++) {
       hora=hora+2;
      
       if(hora==13){
        aux="pm";
        estilo="style='background:#777x '";
       }
      nuevo_html += `
      <tr >
          <td > `+hora+`:00 `+aux+`</td>`
        if(hora==13){
            hora=12;
            i--;
        }
    
    for (var j = 1; j <7; j++) {
        bandera=0;
      datos.forEach(mat => {

         
          if(mat.hora1 == hora && j==mat.dia){ 
                bandera=1;
                nuevo_html += `<td  class="materia active" style="background:`+getRandomColor()+`; text-align:center; font-size:20px;  ">${mat.sala} </td>`;     
            }
            
        });
        if(bandera!=1){
            console.log(hora+" "+j);
            nuevo_html +=`<td style="background:#FCFAFA"></td>`;
        }
        
    }
    
    `</tr>`
    
    }
    `</tbody>`
    return nuevo_html;
  }
  function getRandomColor() {
    var letters = '123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 15)];
    }
    return color;
  }
  function cambioColor(){

  }
  