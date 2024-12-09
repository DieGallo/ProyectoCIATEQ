'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addTypeProyectButton = document.getElementById("addTypeProyect");
    const editTypeProyectButton = document.getElementById("editTypeProyect");
    const delTypeProyectButton = document.getElementById("delTypeProyect");

    // Tabla de datos del Empleado
    const typeProyectFormContainer = document.getElementById("typeProyectTable");

    // Formularios del CRUD de Empleados
    const addTypeProyectFormContainer = document.getElementById("addTypeProyectForm");
    const editTypeProyectFormContainer = document.getElementById("editTypeProyectForm");

    // Botones de cancelación de formularios
    const addCancelButtonTypeProyect = document.getElementById("addCancelButtonTypeProyect");
    const editCancelButtonTypeProyect = document.getElementById("editCancelButtonTypeProyect");
    const delCancelButtonTypeProyect = document.getElementById("delCancelButtonTypeProyect");
    const confirmDeleteButtonTypeProyect = document.getElementById("confirmDeleteButtonTypeProyect");

    // Variable de la paginación de Empleados
    const paginationTypeProyect = document.getElementById("paginationTypeProyect");

    // Interacción del botón y formulario de Agregar Empleado
    addTypeProyectButton.addEventListener("click", function() {
        typeProyectFormContainer.style.display = "none";
        paginationTypeProyect.style.display = "none";
        addTypeProyectFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editTypeProyectButton.addEventListener("click", function() {
        typeProyectFormContainer.style.display = "none";
        paginationTypeProyect.style.display = "none";
        editTypeProyectFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonTypeProyect.addEventListener("click", function() {
        addTypeProyectFormContainer.style.display = "none";
        typeProyectFormContainer.style.display = "block";
        paginationTypeProyect.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonTypeProyect.addEventListener("click", function() {
        editTypeProyectFormContainer.style.display = "none";
        typeProyectFormContainer.style.display = "block";
        paginationTypeProyect.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.typeP-checkbox');
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
            editTypeProyectButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delTypeProyectButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editTypeProyectButton.disabled = false;
            delTypeProyectButton.disabled = false;
        } else {
            editTypeProyectButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delTypeProyectButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editTypeProyectButton.disabled = true;
            delTypeProyectButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/typeProyect/${selectedId}/edit/`;
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
    function deleteTypeProyect() {
        if (selectedId) {
            fetch(`/typeProyect/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#typeProyect-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delTypeProyectButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteTypeProyect();
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
        const typeProyectFormContainer = document.getElementById("typeProyectTable");
        const editTypeProyectForm = document.getElementById("editTypeProyectForm");

        typeProyectFormContainer.style.display = "none"; // Oculta la tabla
        paginationTypeProyect.style.display = "none"; // Oculta la paginación
        editTypeProyectForm.hidden = false; // Muestra el formulario de edición
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
    editTypeProyectButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonTypeProyect.addEventListener("click", function() {
        window.location.href = "/typeProyect/";
    });

    // ------------------------------------ delete --------------------------

    // Función para redirigir a la URL de edición
    function redirectToDelete() {
        if (selectedId) {
            window.location.href = `/typeProyect/${selectedId}/delete/`;
        }
    }

    // Verificar la URL actual
    const currentURLDelete = window.location.href;

    // Ocultar la tabla si la URL contiene '/delete/'
    if (currentURLDelete.includes('/delete/')) {
        const typeProyectFormContainer = document.getElementById("typeProyectTable");
        const editTypeProyectFormContainer = document.getElementById("editTypeProyectFormContainer");

        typeProyectFormContainer.style.display = "none"; // Oculta la tabla
        paginationTypeProyect.style.display = "none"; // Oculta la paginación
        editTypeProyectFormContainer.hidden = false; // Muestra el formulario de edición
    }

    // // Mostrar el modal cuando se hace clic en el botón de eliminar
    // delTypeProyectButton.addEventListener("click", function() {
    //     // Se extrae el ID de la especialidad seleccionada
    //     const specialtyId = selectedId;
    //     confirmDeleteButtonTypeProyect.setAttribute("data-specialty-id", specialtyId);
    //     // Mostrar modal
    //     document.getElementById("popup-modal").classList.remove("hidden");
    // });

    // // Confirmar eliminación y hacer la solicitud de eliminación
    // confirmDeleteButtonTypeProyect.addEventListener("click", function() {
    //     const specialtyId = confirmDeleteButtonTypeProyect.getAttribute("data-specialty-id");

    //     if (specialtyId) {
    //         fetch(`/specialty/${specialtyId}/delete/`, {
    //                 method: "DELETE",
    //                 headers: {
    //                     "X-CSRFToken": getCookie("csrftoken"),
    //                 },
    //             })
    //             .then(response => {
    //                 if (response.ok) {
    //                     window.location.href = "/specialty/";
    //                     modal.classList.add("hidden");
    //                     // Recarga la página automáticamente
    //                     window.location.reload();
    //                 } else {
    //                     console.error("Error deleting specialty");
    //                 }
    //             })
    //             .catch(error => {
    //                 console.error("Error:", error);
    //             });
    //     }
    // });

    // // Función para obtener el token CSRF
    // function getCookie(name) {
    //     let cookieValue = null;
    //     if (document.cookie && document.cookie !== '') {
    //         const cookies = document.cookie.split(';');
    //         for (let i = 0; i < cookies.length; i++) {
    //             const cookie = cookies[i].trim();
    //             if (cookie.substring(0, name.length + 1) === (name + '=')) {
    //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //                 break;
    //             }
    //         }
    //     }
    //     return cookieValue;
    // }

    // // Añadir event listeners a todos los checkboxes
    // checkboxes.forEach(function(checkbox) {
    //     checkbox.addEventListener('change', function() {
    //         if (this.checked) {
    //             // Deselecciona todos los demás checkboxes
    //             checkboxes.forEach(function(otherCheckbox) {
    //                 if (otherCheckbox !== checkbox) {
    //                     otherCheckbox.checked = false;
    //                 }
    //             });
    //         }
    //         toggleButtons();
    //     });
    // });

    // // Evento de cancelar (ocultar modal)
    // document.querySelectorAll('[data-modal-hide="popup-modal"]').forEach(function(button) {
    //     button.addEventListener("click", function() {
    //         document.getElementById("popup-modal").classList.add("hidden");
    //     });
    // });

    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    delEmployeeModal();
    closeModal();
    getCookie();
});