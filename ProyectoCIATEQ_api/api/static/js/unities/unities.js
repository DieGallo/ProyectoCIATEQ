'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addUnityButton = document.getElementById("addUnity");
    const editUnityButton = document.getElementById("editUnity");
    const delUnityButton = document.getElementById("delUnity");

    // Tabla de datos del Empleado
    const unityTableContainer = document.getElementById("unityTable");

    // Formularios del CRUD de Empleados
    const addUnityFormContainer = document.getElementById("addUnityForm");
    const editUnityFormContainer = document.getElementById("editUnityForm");

    // Botones de cancelación de formularios
    const addCancelButtonUnity = document.getElementById("addCancelButtonUnity");
    const editCancelButtonUnity = document.getElementById("editCancelButtonUnity");
    const delCancelButtonUnity = document.getElementById("delCancelButtonUnity");
    const confirmDeleteButtonUnity = document.getElementById("confirmDeleteButtonUnity");

    // Variable de la paginación de Empleados
    const paginationUnity = document.getElementById("paginationUnity");

    // Interacción del botón y formulario de Agregar Empleado
    addUnityButton.addEventListener("click", function() {
        unityTableContainer.style.display = "none";
        paginationUnity.style.display = "none";
        addUnityFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editUnityButton.addEventListener("click", function() {
        unityTableContainer.style.display = "none";
        paginationUnity.style.display = "none";
        editUnityFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonUnity.addEventListener("click", function() {
        addUnityFormContainer.style.display = "none";
        unityTableContainer.style.display = "block";
        paginationUnity.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonUnity.addEventListener("click", function() {
        editUnityFormContainer.style.display = "none";
        unityTableContainer.style.display = "block";
        paginationUnity.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.unity-checkbox');
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
            editUnityButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delUnityButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editUnityButton.disabled = false;
            delUnityButton.disabled = false;
        } else {
            editUnityButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delUnityButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editUnityButton.disabled = true;
            delUnityButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/unities/${selectedId}/edit/`;
        }
    }

    // Verificar la URL actual
    const currentURLEdit = window.location.href;

    // Ocultar la tabla si la URL contiene '/edit/'
    if (currentURLEdit.includes('/edit/')) {
        const unityTableContainer = document.getElementById("unityTable");
        const editUnityForm = document.getElementById("editUnityForm");

        unityTableContainer.style.display = "none"; // Oculta la tabla
        paginationUnity.style.display = "none"; // Oculta la paginación
        editUnityForm.hidden = false; // Muestra el formulario de edición
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
    editUnityButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonUnity.addEventListener("click", function() {
        window.location.href = "/unities/";
    });

    // ------------------------------------ delete --------------------------

    // Función para redirigir a la URL de edición
    function redirectToDelete() {
        if (selectedId) {
            window.location.href = `/unities/${selectedId}/delete/`;
        }
    }

    // Verificar la URL actual
    const currentURLDelete = window.location.href;

    // Ocultar la tabla si la URL contiene '/delete/'
    if (currentURLDelete.includes('/delete/')) {
        const unityTableContainer = document.getElementById("unityTable");
        const editUnityForm = document.getElementById("editUnityForm");

        unityTableContainer.style.display = "none"; // Oculta la tabla
        paginationUnity.style.display = "none"; // Oculta la paginación
        editUnityForm.hidden = false; // Muestra el formulario de edición
    }

    // // Mostrar el modal cuando se hace clic en el botón de eliminar
    // delUnityButton.addEventListener("click", function() {
    //     // Se extrae el ID de la especialidad seleccionada
    //     const specialtyId = selectedId;
    //     confirmDeleteButtonSpecialty.setAttribute("data-specialty-id", specialtyId);
    //     // Mostrar modal
    //     document.getElementById("popup-modal").classList.remove("hidden");
    // });

    // // Confirmar eliminación y hacer la solicitud de eliminación
    // confirmDeleteButtonSpecialty.addEventListener("click", function() {
    //     const specialtyId = confirmDeleteButtonSpecialty.getAttribute("data-specialty-id");

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