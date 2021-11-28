function addNewOngForm() {
    var r = confirm("Estás seguro que desea ingresar esta ONG")
    if (r == true) {
        $.ajax({
            url: '/ong/form/answer',
            type: 'GET',
            success: function (result) {
                alert('Su ONG ha sido ingresada correctamente a la brevedad nos podremos en contacto con usted')
                location.reload();
            },
        });
    }

}