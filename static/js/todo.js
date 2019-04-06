function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


let URL = "/app/";

$(document).ready(
    getTodos()
);

function getTodos() {
    $.getJSON(URL, {}, listTodos);
}

function listTodos(todos) {
    moment.locale('tr');
    $(".lists>tbody").html("");
    $.each(todos,
        function (idx, todo) {
            let added_at = moment(todo.added_at).format('L') + " " + moment(todo.added_at).format('LT');
            let done_at = moment(todo.done_at).format('L') + " " + moment(todo.done_at).format('LT');
            let done_button = "<button onclick='doneTodo(" + todo.pk + ")'>Done</button>";
            let delete_button = "<button onclick='deleteTodo(" + todo.pk + ")'>Delete</button>";

            if (todo.done === false) {
                $(".todo-list>tbody").append("<tr><td>" + todo.note + "</td><td>" +
                    added_at + "</td><td>" + done_button + "</td><td>" +
                    delete_button + "</td></tr>");
            } else {
                $(".done-list>tbody").append("<tr><td>" + todo.note + "</td><td>" +
                    added_at + "</td><td>" + todo.done_at + "</td><td>" +
                    delete_button + "</td></tr>");
            }
        }
    );
}

$('#submitButton').click(function () {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax(
        {
            "url": URL,
            "data": {
                "note": $("#todoNote").val(),
                "done": false,
            },
            "type": "post",
            "success": add_success,
            "error": add_error
        }
    ); // ajax()
});

function add_success() {
    getTodos();
    alert("Todo Added Successfully");
}

function add_error() {
    alert("Todo Could not added!");
}

function doneTodo(pk) {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax(
        {
            "url": URL + pk,
            "type": "PUT",
            "success": done_success,
            "error": done_error
        }
    ); // ajax()
}

function done_success() {
    getTodos();
    alert("Todo Deleted");
}

function done_error() {
    alert("Todo Unable to Delete!");
}


function deleteTodo(pk) {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax(
        {
            "url": URL + pk,
            "type": "delete",
            "success": delete_success,
            "error": delete_error
        }
    ); // ajax()
}

function delete_success() {
    getTodos();
    alert("Todo Deleted");
}

function delete_error() {
    alert("Todo Unable to Delete!");
}
