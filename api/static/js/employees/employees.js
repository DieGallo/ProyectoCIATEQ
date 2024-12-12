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
    const addCancelButtonEmployee = document.getElementById("addCancelButtonEmployee");
    const editCancelButtonEmployee = document.getElementById("editCancelButtonEmployee");

    // Variable de la paginación de Empleados
    const paginationEmployee = document.getElementById("paginationEmployee");

    // Tabs
    const tabsEmployee = document.getElementById("tabsEmployee");
    const dashboardEmployee = document.getElementById("dashboard");
    const articlesEmployee = document.getElementById("articles");
    const lineinvsEmployee = document.getElementById("lineInvs");
    const studentsEmployee = document.getElementById("students");
    const profileEmployee = document.getElementById("profile");

    // Interacción del botón y formulario de Agregar Empleado
    addEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        paginationEmployee.style.display = "none";
        tabsEmployee.style.display = "none";
        profileEmployee.style.display = "none";
        addEmployeeFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editEmployeeButton.addEventListener("click", function() {
        employeeTableContainer.style.display = "none";
        paginationEmployee.style.display = "none";
        tabsEmployee.style.display = "none";
        editEmployeeFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonEmployee.addEventListener("click", function() {
        addEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        paginationEmployee.style.display = "block";
        tabsEmployee.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonEmployee.addEventListener("click", function() {
        editEmployeeFormContainer.style.display = "none";
        employeeTableContainer.style.display = "block";
        paginationEmployee.style.display = "block";
        tabsEmployee.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.employee-checkbox');
    let selectedId = null;

    // Función para habilitar/deshabilitar los botones
    function toggleButtons() {
        let anyChecked = false;

        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                anyChecked = true;
                selectedId = checkbox.value;
            }
        });

        if (anyChecked) {
            editEmployeeButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delEmployeeButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            dashboardEmployee.className = "focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800";
            articlesEmployee.className = "focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800";
            lineinvsEmployee.className = "focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800";
            studentsEmployee.className = "focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800";
            editEmployeeButton.disabled = false;
            delEmployeeButton.disabled = false;
        } else {
            editEmployeeButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delEmployeeButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            dashboardEmployee.className = "inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500";
            articlesEmployee.className = "inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500";
            lineinvsEmployee.className = "inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500";
            studentsEmployee.className = "inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500";
            editEmployeeButton.disabled = true;
            delEmployeeButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/employees/${selectedId}/edit/`;
        }
    }

    // Función para mostrar el modal
    function showModal() {
        document.getElementById('popup-modal').classList.remove('hidden');
    }

    // Función para ocultar el modal
    function hideModal() {
        document.getElementById('popup-modal').classList.add('hidden');
    }

    // Función para eliminar el empleado
    function deleteEmployee() {
        if (selectedId) {
            fetch(`/employees/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#employee-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delEmployeeButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteEmployee();
    });

    // Añadir event listener al botón de cancelación de eliminación
    const cancelDeleteButton = document.getElementById('cancelDeleteButton');
    cancelDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        hideModal();
    });

    // Obtener el token CSRF del contexto de Django
    const csrfToken = '{{ csrf_token }}';

    // Verificar la URL actual
    const currentURLEdit = window.location.href;

    // Ocultar la tabla si la URL contiene '/edit/'
    if (currentURLEdit.includes('/edit/')) {
        const employeeTableContainer = document.getElementById("employeeTable");
        const editEmployeeForm = document.getElementById("editEmployeeForm");

        employeeTableContainer.style.display = "none"; // Oculta la tabla
        paginationEmployee.style.display = "none"; // Oculta la paginación
        editEmployeeForm.hidden = false; // Muestra el formulario de edición
    }

    // Añadir event listeners a todos los checkboxes
    // Función para que solamente esté un checkbox seleccionado a la vez.
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                // Deselecciona todos los demás checkboxes
                checkboxes.forEach(function(otherCheckbox) {
                    if (otherCheckbox !== checkbox) {
                        otherCheckbox.checked = false;
                    }
                });
            }
            toggleButtons();
        });
    });

    // Añadir event listener al botón de edición
    editEmployeeButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonEmployee.addEventListener("click", function() {
        window.location.href = "/employees/";
    });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    closeModal();
});