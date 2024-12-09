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
    const checkboxes = document.querySelectorAll('.event-checkbox');
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
            editEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delEventButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editEventButton.disabled = false;
            delEventButton.disabled = false;
        } else {
            editEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delEventButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editEventButton.disabled = true;
            delEventButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/events/${selectedId}/edit/`;
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
    function deleteEvent() {
        if (selectedId) {
            fetch(`/events/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#event-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delEventButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteEvent();
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
        const eventTableContainer = document.getElementById("eventTable");
        const editEventForm = document.getElementById("editEventForm");

        eventTableContainer.style.display = "none"; // Oculta la tabla
        paginationEvent.style.display = "none"; // Oculta la paginación
        editEventForm.hidden = false; // Muestra el formulario de edición
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

    editEventButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    editCancelButtonEvent.addEventListener("click", function() {
        window.location.href = "/events/";
    });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    closeModal();
});