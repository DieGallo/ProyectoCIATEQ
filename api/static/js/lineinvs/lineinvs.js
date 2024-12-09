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
    const checkboxes = document.querySelectorAll('.lineinvs-checkbox');
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
            editLineInvButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delLineInvButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editLineInvButton.disabled = false;
            delLineInvButton.disabled = false;
        } else {
            editLineInvButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delLineInvButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editLineInvButton.disabled = true;
            delLineInvButton.disabled = true;
            selectedId = null;
        }
    }

    // ------------------------------- EDIT -----------------------------
    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/lineinvs/${selectedId}/edit/`;
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
    function deleteLineInv() {
        if (selectedId) {
            fetch(`/lineinvs/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#lineinv-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delLineInvButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteLineInv();
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
        const lineInvTableContainer = document.getElementById("lineInvTable");
        const editLineInvFormContainer = document.getElementById("editLineInvForm");

        lineInvTableContainer.style.display = "none"; // Oculta la tabla
        paginationLineInv.style.display = "none"; // Oculta la paginación
        editLineInvFormContainer.hidden = false; // Muestra el formulario de edición
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
    editLineInvButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonLineInv.addEventListener("click", function() {
        window.location.href = "/lineinvs/";
    });




    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
});