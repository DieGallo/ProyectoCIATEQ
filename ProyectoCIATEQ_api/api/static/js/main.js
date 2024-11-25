'use strict'

document.addEventListener("DOMContentLoaded", function() {
    const addEmployeeButton = document.getElementById("addEmployee");
    const employeeTableContainer = document.getElementById("employeeTable");
    const addEmployeeFormContainer = document.getElementById("addEmployeeForm");
    const cancelButton = document.getElementById("cancelButton");
    const pagination = document.getElementById("paginationEmployee");
    const tabsEmployee = document.getElementById("tabsEmployee");

    // Eventos del botón de edición.
    const editEmployeeButton = document.getElementById("editEmployee");

    addEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        pagination.style.display = "none";
        tabsEmployee.style.display = "none";
        addEmployeeFormContainer.style.display = "block";
    });

    editEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        pagination.style.display = "none";
        tabsEmployee.style.display = "none";
        addEmployeeFormContainer.style.display = "block";
    });

    cancelButton.addEventListener("click", function() {
        addEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        pagination.style.display = "block";
        tabsEmployee.style.display = "block";
    });
});


document.getElementById('submitButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevenir que el formulario se envíe de forma tradicional
    const formData = {
        name: document.getElementById('name').value,
        lastName: document.getElementById('lastName').value,
        photo: document.getElementById('photo').value,
        birthdate: document.getElementById('birthdate').value,
        sex: document.getElementById('sex').value,
        phone: document.getElementById('phone').value,
        email: document.getElementById('email').value,
        address: document.getElementById('address').value,
        city: document.getElementById('city').value,
        country: document.getElementById('country').value,
        startDate: document.getElementById('startDate').value,
        endDate: document.getElementById('endDate').value,
        area_id: document.getElementById('area_id').value,
        studies_id: document.getElementById('studies_id').value,
    };

    fetch('/employees/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}', // Asegúrate de incluir el token CSRF
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.message) {
            alert("Datos guardados")
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});