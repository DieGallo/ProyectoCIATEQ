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
        window.location.reload();
    });

    // Editar
    editCancelButton.addEventListener("click", function() {
        editEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        pagination.style.display = "block";
        tabsEmployee.style.display = "block";
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

    // Añadir event listeners a todos los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', toggleButtons);
    });

    delEmployeeButton.addEventListener('click', function() {
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