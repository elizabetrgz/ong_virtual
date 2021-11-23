function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function deleteOng(id, name){
  
  
  var r = confirm("Estas seguro que desea eliminar la ong:" + name +"?")
  if (r == true){
    $.ajax({
      url: '/admin/ongs/delete/'+ id,
      type: 'DELETE',
      success: function(result) {
        location.reload();
      }
    });
  }
 
}

function deleteCategories(id, name){
  
  
  var r = confirm("Estas seguro que desea eliminar esta categoría:" + name +"?")
  if (r == true){
    $.ajax({
      url: '/admin/ongs/categories/delete/'+ id,
      type: 'DELETE',
      success: function(result) {
        location.reload();
      }
    });
  }
 
}

