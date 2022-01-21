$('a[rel="ajax:modal"]').click(function (event) {
    $.ajax({
        url: $(this).attr("href"),

        success: function (user, textStatus, jqXHR) {
            $(
                user.type === 1 ?
                `
                <form class="edit-user-form" action="/edit/${user.id}" method="post">
                    <input name="id" type="text" value="${user.id}" disabled />
                    <input name="username" type="text" value="${user.username}" />
                    <input name="name" type="text" value="${user.name}" />
                    <input name="password" type="text" value="${user.password}" />
                    <button type="submit"><h3>Update</h3></button>
                </form>
                `
                :
                `
                <form class="delete-user-form" action="/delete/${user.id}" method="post">
                    <h2>Are you sure you want to delete:</h2>
                    <table>
                    <tbody>
                        <tr>
                        <td>ID</td>
                        <td>Name</td>
                        <td>Username</td>
                        <td>Password</td>
                        </tr>
                        <tr>
                        <td>${user.id}</td>
                        <td>${user.name}</td>
                        <td>${user.username}</td>
                        <td>${user.password}</td>
                        </tr>
                    </tbody>
                    </table>
                    <button type="submit"><h3>DELETE</h3></button>
                </form>
                `)
                .appendTo("body")
                .modal();
        },
    });

    return false;
});
