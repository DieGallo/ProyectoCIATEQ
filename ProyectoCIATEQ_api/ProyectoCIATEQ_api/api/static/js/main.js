'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addEmployeeButton = document.getElementById("addEmployee");
    const editEmployeeButton = document.getElementById("editEmployee");
    const delEmployeeButton = document.getElementById("delEmployee");

    // Tabla de datos del Empleado
    const employeeTableContainer = document.getElementById("employeeTable");

    // Formularios del CRUD de Empleados
    const addEmployeeFormContainer = document.getElementById("addEmployeeForm");
    const editEmployeeFormContainer = document.getElementById("editEmployeeForm");

    // Botones de cancelación de formularios
    const addCancelButton = document.getElementById("addCancelButton");
    const editCancelButton = document.getElementById("editCancelButton");

    // Variable de la paginación de Empleados
    const pagination = document.getElementById("paginationEmployee");

    // Tabs de los detalles del Empleado
    const tabsEmployee = document.getElementById("tabsEmployee");

    // Interacción del botón y formulario de Agregar Empleado
    addEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        pagination.style.display = "none";
        tabsEmployee.style.display = "none";
        addEmployeeFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        pagination.style.display = "none";
        tabsEmployee.style.display = "none";
        editEmployeeFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButton.addEventListener("click", function() {
        addEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        pagination.style.display = "block";
        tabsEmployee.style.display = "block";
    });

    // Editar
    editCancelButton.addEventListener("click", function() {
        editEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        pagination.style.display = "block";
        tabsEmployee.style.display = "block";
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.employee-checkbox');

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            toggleButtons();
        });
    });

    editEmployeeButton.addEventListener('click', function() {
        const selectedId = getSelectedEmployeeId();
        if (selectedId) {
            loadEmployeeData(selectedId);
        }
    });

    // Función para habilitar/deshabilitar los botones
    function toggleButtons() {
        let anyChecked = false;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                anyChecked = true;
            }
        });

        if (anyChecked) {
            editEmployeeButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delEmployeeButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editEmployeeButton.disabled = false;
            delEmployeeButton.disabled = false;
        } else {
            editEmployeeButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delEmployeeButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editEmployeeButton.disabled = true;
            delEmployeeButton.disabled = true;
        }
    }

    function getSelectedEmployeeId() {
        let selectedId = null;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedId = checkbox.closest('input').getAttribute('data-id');
            }
        });
        return selectedId;
    }

    function loadEmployeeData(id) {
        fetch(`/employees/edit/${id}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('name').value = data.name;
                document.getElementById('lastName').value = data.lastName;
                document.getElementById('photo').value = data.photo;
                document.getElementById('birthdate').value = data.birthdate;
                document.getElementById('sex').value = data.sex;
                document.getElementById('phone').value = data.phone;
                document.getElementById('email').value = data.email;
                document.getElementById('address').value = data.address;
                document.getElementById('city').value = data.city;
                document.getElementById('country').value = data.country;
                document.getElementById('startDate').value = data.startDate;
                document.getElementById('area_id').value = data.area_id;
                document.getElementById('studies_id').value = data.studies_id;
            })
            .catch(error => console.error('Error:', error));
    }


    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });


    const delConfirmButton = document.getElementById('delConfirmEmployee');

    delConfirmButton.addEventListener('click', function(){
        const employeeId = modal.getAttribute('data-employee-id');
        const url = `/employees/${employeeId}/`;

        fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Necesitas incluir el token CSRF para la solicitud DELETE
            }
        })
        .then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                alert('Error al eliminar el empleado.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // confirmButton.addEventListener('click', function() {
    //     const employeeId = this.getAttribute('data-employee-id');
    //     const url = `/employees/${employeeId}/`;

    //     fetch(url, {
    //         method: 'DELETE',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de incluir el token CSRF
    //         },
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         if (data.success) {
    //             alert('Empleado eliminado exitosamente');
    //             // Aquí puedes agregar lógica adicional, como recargar la página o eliminar el elemento del DOM
    //             window.location.reload();  // Recargar la página
    //         } else {
    //             alert('Hubo un error al eliminar el empleado');
    //         }
    //     })
    //     .catch((error) => {
    //         console.error('Error:', error);
    //     });
    // });

    // Función para obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    loadEmployeeData();
});
