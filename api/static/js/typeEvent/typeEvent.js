'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addTypeEventButton = document.getElementById("addTypeEvent");
    const editTypeEventButton = document.getElementById("editTypeEvent");
    const delTypeEventButton = document.getElementById("delTypeEvent");

    // Tabla de datos del Empleado
    const typeEventFormContainer = document.getElementById("typeEventTable");

    // Formularios del CRUD de Empleados
    const addTypeEventFormContainer = document.getElementById("addTypeEventForm");
    const editTypeEventFormContainer = document.getElementById("editTypeEventForm");

    // Botones de cancelación de formularios
    const addCancelButtonTypeEvent = document.getElementById("addCancelButtonTypeEvent");
    const editCancelButtonTypeEvent = document.getElementById("editCancelButtonTypeEvent");
    const delCancelButtonTypeEvent = document.getElementById("delCancelButtonTypeEvent");
    const confirmDeleteButtonTypeEvent = document.getElementById("confirmDeleteButtonTypeEvent");

    // Variable de la paginación de Empleados
    const paginationTypeEvent = document.getElementById("paginationTypeEvent");

    // Interacción del botón y formulario de Agregar Empleado
    addTypeEventButton.addEventListener("click", function() {
        typeEventFormContainer.style.display = "none";
        paginationTypeEvent.style.display = "none";
        addTypeEventFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editTypeEventButton.addEventListener("click", function() {
        typeEventFormContainer.style.display = "none";
        paginationTypeEvent.style.display = "none";
        editTypeEventFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonTypeEvent.addEventListener("click", function() {
        addTypeEventFormContainer.style.display = "none";
        typeEventFormContainer.style.display = "block";
        paginationTypeEvent.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonTypeEvent.addEventListener("click", function() {
        editTypeEventFormContainer.style.display = "none";
        typeEventFormContainer.style.display = "block";
        paginationTypeEvent.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.typeE-checkbox');
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
            editTypeEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delTypeEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editTypeEventButton.disabled = false;
            delTypeEventButton.disabled = false;
        } else {
            editTypeEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delTypeEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editTypeEventButton.disabled = true;
            delTypeEventButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/typeEvent/${selectedId}/edit/`;
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
    function deleteTypeEvent() {
        if (selectedId) {
            fetch(`/typeEvent/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#typeEvent-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delTypeEventButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteTypeEvent();
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
        const typeEventFormContainer = document.getElementById("typeEventTable");
        const editTypeEventForm = document.getElementById("editTypeEventForm");

        typeEventFormContainer.style.display = "none"; // Oculta la tabla
        paginationTypeEvent.style.display = "none"; // Oculta la paginación
        editTypeEventForm.hidden = false; // Muestra el formulario de edición
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
    editTypeEventButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonTypeEvent.addEventListener("click", function() {
        window.location.href = "/typeEvent/";
    });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
    getCookie();
});