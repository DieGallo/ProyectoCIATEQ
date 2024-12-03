'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addEventButton = document.getElementById("addEvent");
    const editEventButton = document.getElementById("editEvent");
    const delEventButton = document.getElementById("delEvent");

    // Tabla de datos del Empleado
    const eventTableContainer = document.getElementById("eventTable");

    // Formularios del CRUD de Empleados
    const addEventFormContainer = document.getElementById("addEventForm");
    const editEventFormContainer = document.getElementById("editEventForm");

    // Botones de cancelación de formularios
    const addCancelButtonEvent = document.getElementById("addCancelButtonEvent");
    const editCancelButtonEvent = document.getElementById("editCancelButtonEvent");

    // Variable de la paginación de Empleados
    const paginationEvent = document.getElementById("paginationEvent");

    // Interacción del botón y formulario de Agregar Empleado
    addEventButton.addEventListener("click", function() {
        eventTableContainer.style.display = "none";
        paginationEvent.style.display = "none";
        addEventFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editEventButton.addEventListener("click", function() {
        eventTableContainer.style.display = "none";
        paginationEvent.style.display = "none";
        editEventFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonEvent.addEventListener("click", function() {
        addEventFormContainer.style.display = "none";
        eventTableContainer.style.display = "block";
        paginationEvent.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonEvent.addEventListener("click", function() {
        editEventFormContainer.style.display = "none";
        eventTableContainer.style.display = "block";
        paginationEvent.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.employee-checkbox');
    const deleteForm = document.getElementById('delete-form');

    // Función para habilitar/deshabilitar los botones
    function toggleButtons() {
        let anyChecked = false;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                anyChecked = true;
            }
        });

        if (anyChecked) {
            editEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editEventButton.disabled = false;
            delEventButton.disabled = false;
        } else {
            editEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editEventButton.disabled = true;
            delEventButton.disabled = true;
        }
    }

    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });

    delEventButton.addEventListener('click', function() {
        let selectedEmployeeId = null;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedEmployeeId = checkbox.value;
            }
        });

        if (selectedEmployeeId) {
            delEmployeeModal(selectedEmployeeId);
        }
    });

    let deleteUrl = '';

    function delEmployeeModal(employeeId) {
        // Muestra el modal
        const modal = document.getElementById('popup-modal');
        modal.classList.remove('hidden');

        // Configura la URL de eliminación
        deleteUrl = `/employees/${employeeId}/delete/`;
    }

    function closeModal() {
        const modal = document.getElementById('popup-modal');
        modal.classList.add('hidden');
    }

    document.getElementById('confirmDeleteButton').addEventListener('click', function() {
        window.location.href = deleteUrl;
    });


    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
});