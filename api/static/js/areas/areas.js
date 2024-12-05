'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addAreaButton = document.getElementById("addArea");
    const editAreaButton = document.getElementById("editArea");
    const delAreaButton = document.getElementById("delArea");

    // Tabla de datos del Empleado
    const areaTableContainer = document.getElementById("areaTable");

    // Formularios del CRUD de Empleados
    const addAreaFormContainer = document.getElementById("addAreaForm");
    const editAreaFormContainer = document.getElementById("editAreaForm");

    // Botones de cancelación de formularios
    const addCancelButtonArea = document.getElementById("addCancelButtonArea");
    const editCancelButtonArea = document.getElementById("editCancelButtonArea");

    // Variable de la paginación de Empleados
    const paginationArea = document.getElementById("paginationArea");

    // Interacción del botón y formulario de Agregar Empleado
    addAreaButton.addEventListener("click", function() {
        areaTableContainer.style.display = "none";
        paginationArea.style.display = "none";
        addAreaFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editAreaButton.addEventListener("click", function() {
        areaTableContainer.style.display = "none";
        paginationArea.style.display = "none";
        editAreaFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonArea.addEventListener("click", function() {
        addAreaFormContainer.style.display = "none";
        areaTableContainer.style.display = "block";
        paginationArea.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonArea.addEventListener("click", function() {
        editAreaFormContainer.style.display = "none";
        areaTableContainer.style.display = "block";
        paginationArea.style.display = "block";
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
            editAreaButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delAreaButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editAreaButton.disabled = false;
            delAreaButton.disabled = false;
        } else {
            editAreaButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delAreaButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editAreaButton.disabled = true;
            delAreaButton.disabled = true;
        }
    }

    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });

    delAreaButton.addEventListener('click', function() {
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