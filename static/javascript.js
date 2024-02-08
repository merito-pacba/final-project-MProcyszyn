function showForm(formId) {
    // Get all forms on the page
    let allForms = document.querySelectorAll('form');

    // Loop through all forms and hide them
    allForms.forEach(form => {
        form.style.display = "none";
    });

    // Show the specified form
    let formToShow = document.getElementById(formId);
    if (formToShow) {
        formToShow.style.display = "flex";
    }
}

//function fill_form(){
//    let id = document.getElementById('id').value
//    console.log(id + "AddressLine1")
//    document.getElementById("AddressLine1").value = document.getElementById(id + "AddressLine1").innerHTML
//    document.getElementById("AddressLine2").value = document.getElementById(id + "AddressLine2").innerHTML
//    document.getElementById("City").value = document.getElementById(id + "City").innerHTML
//    document.getElementById("StateProvince").value = document.getElementById(id + "StateProvince").innerHTML
//    document.getElementById("CountryRegion").value = document.getElementById(id + "CountryRegion").innerHTML
//    document.getElementById("PostalCode").value = document.getElementById(id + "PostalCode").innerHTML
//    document.getElementById("rowguid").value = document.getElementById(id + "rowguid").innerHTML
//    document.getElementById("ModifiedDate").value = document.getElementById(id + "ModifiedDate").innerHTML
//}

function submitForm(endpoint_url) {
    var form = document.getElementById("add_form");
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open("PUT", endpoint_url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Handle successful response
            console.log(xhr.responseText);
            location.reload(true);
        }
    window.location.reload();
    };

    xhr.send(formData);
}

function submitDeleteForm(endpoint_url) {
   var form = document.getElementById("delete_form");
   var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", endpoint_url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Handle successful response
            console.log(xhr.responseText);
        }
    window.location.reload();
    };

    xhr.send(formData);
}
