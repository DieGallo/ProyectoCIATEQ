'use strict'

document.addEventListener("DOMContentLoaded", function() {
    // Botones del CRUD de Empleados
    const addStudentButton = document.getElementById("addStudent");
    const editStudentButton = document.getElementById("editStudent");
    const delStudentButton = document.getElementById("delStudent");

    // Tabla de datos del Empleado
    const studentTableContainer = document.getElementById("studentTable");

    // Formularios del CRUD de Empleados
    const addStudentFormContainer = document.getElementById("addStudentForm");
    const editStudentFormContainer = document.getElementById("editStudentForm");

    // Botones de cancelación de formularios
    const addCancelButton = document.getElementById("addCancelButtonStudent");
    const editCancelButton = document.getElementById("editCancelButtonStudent");

    // Variable de la paginación de Empleados
    const paginationStudent = document.getElementById("paginationStudent");

    // Tabs de los detalles del Empleado
    const tabsStudent = document.getElementById("tabsStudent");

    // Función para obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Interacción del botón y formulario de Agregar Empleado
    addStudentButton.addEventListener("click", function() {
        studentTableContainer.style.display = "none";
        paginationStudent.style.display = "none";
        tabsStudent.style.display = "none";
        addStudentFormContainer.style.display = "block";
    });

    // Interacción del botón y formulario para Editar un Empleado
    editStudentButton.addEventListener("click", function() {
        studentTableContainer.style.display = "none";
        paginationStudent.style.display = "none";
        tabsStudent.style.display = "none";
        editStudentFormContainer.style.display = "block";
    });

    // Botones de cancelación de interacciones
    // Nuevo
    addCancelButton.addEventListener("click", function() {
        addStudentFormContainer.style.display = "none";
        studentTableContainer.style.display = "block";
        paginationStudent.style.display = "block";
        tabsStudent.style.display = "block";
        window.location.reload();
    });

    // Editar
    editCancelButton.addEventListener("click", function() {
        editStudentFormContainer.style.display = "none";
        studentTableContainer.style.display = "block";
        paginationStudent.style.display = "block";
        tabsStudent.style.display = "block";
        window.location.reload();
    });

    // Eventos para las interacciones de los botones de Editar - Eliminar
    const checkboxes = document.querySelectorAll('.student-checkbox');
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
            editStudentButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            delStudentButton.className = 'focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-4 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800';
            editStudentButton.disabled = false;
            delStudentButton.disabled = false;
        } else {
            editStudentButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400 cursor-not-allowed dark:text-gray-500';
            delStudentButton.className = 'font-medium text-sm px-5 py-2.5 me-2 mb-4 inline-block p-4 text-gray-400  cursor-not-allowed dark:text-gray-500';
            editStudentButton.disabled = true;
            delStudentButton.disabled = true;
            selectedId = null;
        }
    }

    // Función para redirigir a la URL de edición
    function redirectToEdit() {
        if (selectedId) {
            window.location.href = `/students/${selectedId}/edit/`;
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
    function deleteStudent() {
        if (selectedId) {
            fetch(`/students/${selectedId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken // Obtén el token CSRF del contexto de Django
                }
            }).then(response => {
                if (response.ok) {
                    // Eliminar la fila del empleado de la tabla
                    document.querySelector(`#students-row-${selectedId}`).remove();
                    hideModal();
                    window.location.reload();
                } else {
                    window.location.reload();
                }
            });
        }
    }

    // Añadir event listener al botón de eliminación
    delStudentButton.addEventListener('click', function(event) {
        event.preventDefault();
        showModal();
    });

    // Añadir event listener al botón de confirmación de eliminación
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function(event) {
        event.preventDefault();
        deleteStudent();
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
        const studentTableContainer = document.getElementById("studentTable");
        const editStudentButton = document.getElementById("editStudentForm");

        studentTableContainer.style.display = "none"; // Oculta la tabla
        paginationStudent.style.display = "none"; // Oculta la paginación
        editStudentFormContainer.hidden = false; // Muestra el formulario de edición
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
    editStudentButton.addEventListener('click', function(event) {
        event.preventDefault();
        redirectToEdit();
    });

    // Agrega un evento de clic al botón de cancelar
    editCancelButton.addEventListener("click", function() {
        window.location.href = "/students/";
    });

    // ------------------------------------- DELETE --------------------------------
    const delConfirmButtonStudent = document.getElementById('delConfirmStudent');

    delConfirmButtonStudent.addEventListener('click', function() {
        const studentId = modal.getAttribute('data-employee-id');
        const url = `/students/${studentId}/`;

        fetch(url, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Necesitas incluir el token CSRF para la solicitud DELETE
                }
            })
            .then(response => {
                if (response.ok) {
                    window.location.reload();
                } else {
                    alert('Error al eliminar el empleado.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    // confirmButton.addEventListener('click', function() {
    //     const studentId = this.getAttribute('data-employee-id');
    //     const url = `/employees/${studentId}/`;

    //     fetch(url, {
    //         method: 'DELETE',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de incluir el token CSRF
    //         },
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         if (data.success) {
    //             alert('Empleado eliminado exitosamente');
    //             // Aquí puedes agregar lógica adicional, como recargar la página o eliminar el elemento del DOM
    //             window.location.reload();  // Recargar la página
    //         } else {
    //             alert('Hubo un error al eliminar el empleado');
    //         }
    //     })
    //     .catch((error) => {
    //         console.error('Error:', error);
    //     });
    // });


    // Llama a la función al cargar la página por si hay algún checkbox preseleccionado
    toggleButtons();
});