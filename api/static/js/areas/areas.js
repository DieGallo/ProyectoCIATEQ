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
    const checkboxes = document.querySelectorAll('.area-checkbox');
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
            editAreaButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delAreaButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editAreaButton.disabled = false;
            delAreaButton.disabled = false;
        } else {
            editAreaButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delAreaButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editAreaButton.disabled = true;
            delAreaButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/areas/${selectedId}/edit/`;
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
    function deleteArea() {
        if (selectedId) {
            fetch(`/areas/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#area-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delAreaButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteArea();
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
        const areaTableContainer = document.getElementById("areaTable");
        const editAreaFormContainer = document.getElementById("editAreaForm");

        areaTableContainer.style.display = "none"; // Oculta la tabla
        paginationArea.style.display = "none"; // Oculta la paginación
        editAreaFormContainer.hidden = false; // Muestra el formulario de edición
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

    editAreaButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    editCancelButtonArea.addEventListener("click", function() {
        window.location.href = "/areas/";
    });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
});