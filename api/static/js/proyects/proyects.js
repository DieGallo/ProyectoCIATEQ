'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addProyectButton = document.getElementById("addProyect");
    const editProyectButton = document.getElementById("editProyect");
    const delProyectButton = document.getElementById("delProyect");

    // Tabla de datos del Empleado
    const proyectTableContainer = document.getElementById("proyectTable");

    // Formularios del CRUD de Empleados
    const addProyectFormContainer = document.getElementById("addProyectForm");
    const editProyectFormContainer = document.getElementById("editProyectForm");

    // Botones de cancelación de formularios
    const addCancelButtonProyect = document.getElementById("addCancelButtonProyect");
    const editCancelButtonProyect = document.getElementById("editCancelButtonProyect");

    // Variable de la paginación de Empleados
    const paginationProyect = document.getElementById("paginationProyect");

    // Interacción del botón y formulario de Agregar Empleado
    addProyectButton.addEventListener("click", function() {
        proyectTableContainer.style.display = "none";
        paginationProyect.style.display = "none";
        addProyectFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editProyectButton.addEventListener("click", function() {
        proyectTableContainer.style.display = "none";
        paginationProyect.style.display = "none";
        editProyectFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonProyect.addEventListener("click", function() {
        addProyectFormContainer.style.display = "none";
        proyectTableContainer.style.display = "block";
        paginationProyect.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonProyect.addEventListener("click", function() {
        editProyectFormContainer.style.display = "none";
        proyectTableContainer.style.display = "block";
        paginationProyect.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.proyect-checkbox');
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
            editProyectButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delProyectButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editProyectButton.disabled = false;
            delProyectButton.disabled = false;
        } else {
            editProyectButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delProyectButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editProyectButton.disabled = true;
            delProyectButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/proyects/${selectedId}/edit/`;
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
    function deleteProyect() {
        if (selectedId) {
            fetch(`/proyects/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#proyect-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delProyectButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteProyect();
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
        const proyectTableContainer = document.getElementById("proyectTable");
        const editProyectFormContainer = document.getElementById("editProyectForm");

        proyectTableContainer.style.display = "none"; // Oculta la tabla
        paginationProyect.style.display = "none"; // Oculta la paginación
        editProyectFormContainer.hidden = false; // Muestra el formulario de edición
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


    editProyectButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    editCancelButtonProyect.addEventListener("click", function() {
        window.location.href = "/proyects/";
    });

    // --------------------------------- DELETE --------------------------------
    delProyectButton.addEventListener('click', function() {
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