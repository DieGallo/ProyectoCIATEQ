'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addArticleButton = document.getElementById("addArticle");
    const editArticleButton = document.getElementById("editArticle");
    const delArticleButton = document.getElementById("delArticle");

    // Tabla de datos del Empleado
    const articleTableContainer = document.getElementById("articleTable");

    // Formularios del CRUD de Empleados
    const addArticleFormContainer = document.getElementById("addArticleForm");
    const editArticleFormContainer = document.getElementById("editArticleForm");

    // Botones de cancelación de formularios
    const addCancelButtonArticle = document.getElementById("addCancelButtonArticle");
    const editCancelButtonArticle = document.getElementById("editCancelButtonArticle");

    // Variable de la paginación de Empleados
    const paginationArticle = document.getElementById("paginationArticle");

    // Interacción del botón y formulario de Agregar Empleado
    addArticleButton.addEventListener("click", function() {
        articleTableContainer.style.display = "none";
        paginationArticle.style.display = "none";
        addArticleFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editArticleButton.addEventListener("click", function() {
        articleTableContainer.style.display = "none";
        paginationArticle.style.display = "none";
        editArticleFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButtonArticle.addEventListener("click", function() {
        addArticleFormContainer.style.display = "none";
        articleTableContainer.style.display = "block";
        paginationArticle.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButtonArticle.addEventListener("click", function() {
        editArticleFormContainer.style.display = "none";
        articleTableContainer.style.display = "block";
        paginationArticle.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.article-checkbox');
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
            editArticleButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delArticleButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editArticleButton.disabled = false;
            delArticleButton.disabled = false;
        } else {
            editArticleButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delArticleButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editArticleButton.disabled = true;
            delArticleButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/articles/${selectedId}/edit/`;
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
    function deleteArticle() {
        if (selectedId) {
            fetch(`/articles/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#article-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delArticleButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteArticle();
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
        const articleTableContainer = document.getElementById("articleTable");
        const editArticleForm = document.getElementById("editArticleForm");

        articleTableContainer.style.display = "none"; // Oculta la tabla
        paginationArticle.style.display = "none"; // Oculta la paginación
        editArticleForm.hidden = false; // Muestra el formulario de edición
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
    editArticleButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButtonArticle.addEventListener("click", function() {
        window.location.href = "/articles/";
    });

    // ------------------------------------ delete --------------------------
    // function redirectToDelete() {
    //     if (selectedId) {
    //         window.location.href = `/specialty/${selectedId}/delete/`;
    //     }
    // }

    // // Añadir event listener al botón de edición
    // delArticleButton.addEventListener('click', function(event) {
    //     event.preventDefault();
    //     redirectToDelete();
    // });


    // delArticleButton.addEventListener('click', function() {
    //     let selectedEmployeeId = null;
    //     checkboxes.forEach(function(checkbox) {
    //         if (checkbox.checked) {
    //             selectedEmployeeId = checkbox.value;
    //         }
    //     });

    //     if (selectedEmployeeId) {
    //         delEmployeeModal(selectedEmployeeId);
    //     }
    // });

    // let deleteUrl = '';

    // function delEmployeeModal(employeeId) {
    //     // Muestra el modal
    //     const modal = document.getElementById('popup-modal');
    //     modal.classList.remove('hidden');

    //     // Configura la URL de eliminación
    //     deleteUrl = `/employees/${employeeId}/delete/`;
    // }

    // function closeModal() {
    //     const modal = document.getElementById('popup-modal');
    //     modal.classList.add('hidden');
    // }

    // document.getElementById('confirmDeleteButton').addEventListener('click', function() {
    //     window.location.href = deleteUrl;
    // });


    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
    closeModal();
});