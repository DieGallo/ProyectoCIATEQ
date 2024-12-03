'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addStudentButton = document.getElementById("addStudent");
    const editStudentButton = document.getElementById("editStudent");
    const delStudentButton = document.getElementById("delStudent");

    // Tabla de datos del Empleado
    const studentTableContainer = document.getElementById("studentTable");

    // Formularios del CRUD de Empleados
    const addStudentFormContainer = document.getElementById("addStudentForm");
    const editStudentFormContainer = document.getElementById("editStudentForm");

    // Botones de cancelación de formularios
    const addCancelButton = document.getElementById("addCancelButtonStudent");
    const editCancelButton = document.getElementById("editCancelButtonStudent");

    // Variable de la paginación de Empleados
    const paginationStudent = document.getElementById("paginationStudent");

    // Tabs de los detalles del Empleado
    const tabsStudent = document.getElementById("tabsStudent");

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

    // Interacción del botón y formulario de Agregar Empleado
    addStudentButton.addEventListener("click", function() {
        studentTableContainer.style.display = "none";
        paginationStudent.style.display = "none";
        tabsStudent.style.display = "none";
        addStudentFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editStudentButton.addEventListener("click", function() {
        studentTableContainer.style.display = "none";
        paginationStudent.style.display = "none";
        tabsStudent.style.display = "none";
        editStudentFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButton.addEventListener("click", function() {
        addStudentFormContainer.style.display = "none";
        studentTableContainer.style.display = "block";
        paginationStudent.style.display = "block";
        tabsStudent.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButton.addEventListener("click", function() {
        editStudentFormContainer.style.display = "none";
        studentTableContainer.style.display = "block";
        paginationStudent.style.display = "block";
        tabsStudent.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.student-checkbox');

    // Función para habilitar/deshabilitar los botones
    function toggleButtons() {
        let anyChecked = false;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                anyChecked = true;
            }
        });

        if (anyChecked) {
            editStudentButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delStudentButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editStudentButton.disabled = false;
            delStudentButton.disabled = false;
        } else {
            editStudentButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delStudentButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editStudentButton.disabled = true;
            delStudentButton.disabled = true;
        }
    }

    function getSelectedStudentId() {
        let selectedId = null;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedId = checkbox.closest('input').getAttribute('data-id');
            }
        });
        return selectedId;
    }

    editStudentButton.addEventListener('click', function() {
        const studentId = getSelectedStudentId();
        if (studentId) {
            fetch(`/students/${studentId}/`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('first_name').value = data.name;
                    document.getElementById('last_name').value = data.lastName;
                    document.getElementById('photo').value = data.photo;
                    document.getElementById('birthdate').value = data.birthdate;
                    document.getElementById('sex').value = data.sex;
                    document.getElementById('phone').value = data.phone;
                    document.getElementById('email').value = data.email;
                    document.getElementById('address').value = data.address;
                    document.getElementById('city').value = data.city;
                    document.getElementById('country').value = data.country;
                    document.getElementById('startDate').value = data.startDate;
                    document.getElementById('endDate').value = data.endDate;
                    document.getElementById('area_id').value = data.area_id;
                    document.getElementById('studies_id').value = data.studies_id;
                    editForm.style.display = 'block';
                });
        }
    });


    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });


    const delConfirmButtonStudent = document.getElementById('delConfirmStudent');

    delConfirmButtonStudent.addEventListener('click', function() {
        const studentId = modal.getAttribute('data-employee-id');
        const url = `/students/${studentId}/`;

        fetch(url, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Necesitas incluir el token CSRF para la solicitud DELETE
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
    //     const studentId = this.getAttribute('data-employee-id');
    //     const url = `/employees/${studentId}/`;

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


    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
});