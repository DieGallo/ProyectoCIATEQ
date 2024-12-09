'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addSpecialtyButton = document.getElementById("addSpecialty");
    const editSpecialtyButton = document.getElementById("editSpecialty");
    const delSpecialtyButton = document.getElementById("delSpecialty");

    // Tabla de datos del Empleado
    const specialtyTableContainer = document.getElementById("specialtyTable");

    // Formularios del CRUD de Empleados
    const addSpecialtyFormContainer = document.getElementById("addSpecialtyForm");
    const editSpecialtyFormContainer = document.getElementById("editSpecialtyForm");

    // Botones de cancelación de formularios
    const addCancelButtonSpecialty = document.getElementById("addCancelButtonSpecialty");
    const editCancelButtonSpecialty = document.getElementById("editCancelButtonSpecialty");
    const delCancelButtonSpecialty = document.getElementById("delCancelButtonSpecialty");
    const confirmDeleteButtonSpecialty = document.getElementById("confirmDeleteButtonSpecialty");

    // Variable de la paginación de Empleados
    const paginationSpecialty = document.getElementById("paginationSpecialty");

    // Interacción del botón y formulario de Agregar Empleado
    addSpecialtyButton.addEventListener("click", function() {
        specialtyTableContainer.style.display = "none";
        paginationSpecialty.style.display = "none";
        addSpecialtyFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editSpecialtyButton.addEventListener("click", function() {
        specialtyTableContainer.style.display = "none";
        paginationSpecialty.style.display = "none";
        editSpecialtyFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonSpecialty.addEventListener("click", function() {
        addSpecialtyFormContainer.style.display = "none";
        specialtyTableContainer.style.display = "block";
        paginationSpecialty.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonSpecialty.addEventListener("click", function() {
        editSpecialtyFormContainer.style.display = "none";
        specialtyTableContainer.style.display = "block";
        paginationSpecialty.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.specialty-checkbox');
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
            editSpecialtyButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delSpecialtyButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editSpecialtyButton.disabled = false;
            delSpecialtyButton.disabled = false;
        } else {
            editSpecialtyButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delSpecialtyButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editSpecialtyButton.disabled = true;
            delSpecialtyButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/specialty/${selectedId}/edit/`;
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
    function deleteSpecialty() {
        if (selectedId) {
            fetch(`/specialty/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#specialty-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delSpecialtyButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteSpecialty();
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
        const specialtyTableContainer = document.getElementById("specialtyTable");
        const editSpecialtyForm = document.getElementById("editSpecialtyForm");

        specialtyTableContainer.style.display = "none"; // Oculta la tabla
        paginationSpecialty.style.display = "none"; // Oculta la paginación
        editSpecialtyForm.hidden = false; // Muestra el formulario de edición
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
    editSpecialtyButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonSpecialty.addEventListener("click", function() {
        window.location.href = "/specialty/";
    });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
    getCookie();
});