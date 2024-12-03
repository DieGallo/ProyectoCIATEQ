'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addLineInvButton = document.getElementById("addLineInv");
    const editLineInvButton = document.getElementById("editLineInv");
    const delLineInvButton = document.getElementById("delLineInv");

    // Tabla de datos del Empleado
    const lineInvTableContainer = document.getElementById("lineInvTable");

    // Formularios del CRUD de Empleados
    const addLineInvFormContainer = document.getElementById("addLineInvForm");
    const editLineInvFormContainer = document.getElementById("editLineInvForm");

    // Botones de cancelación de formularios
    const addCancelButtonLineInv = document.getElementById("addCancelButtonLineInv");
    const editCancelButtonLineInv = document.getElementById("editCancelButtonLineInv");

    // Variable de la paginación de Empleados
    const paginationLineInv = document.getElementById("paginationLineInv");

    // Interacción del botón y formulario de Agregar Empleado
    addLineInvButton.addEventListener("click", function() {
        lineInvTableContainer.style.display = "none";
        paginationLineInv.style.display = "none";
        addLineInvFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editLineInvButton.addEventListener("click", function() {
        lineInvTableContainer.style.display = "none";
        paginationLineInv.style.display = "none";
        editLineInvFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonLineInv.addEventListener("click", function() {
        addLineInvFormContainer.style.display = "none";
        lineInvTableContainer.style.display = "block";
        paginationLineInv.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonLineInv.addEventListener("click", function() {
        editLineInvFormContainer.style.display = "none";
        lineInvTableContainer.style.display = "block";
        paginationLineInv.style.display = "block";
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
            editLineInvButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delLineInvButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editLineInvButton.disabled = false;
            delLineInvButton.disabled = false;
        } else {
            editLineInvButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delLineInvButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editLineInvButton.disabled = true;
            delLineInvButton.disabled = true;
        }
    }

    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });

    delLineInvButton.addEventListener('click', function() {
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