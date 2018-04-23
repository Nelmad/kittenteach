$.KittenTeach.Auth = {
    init: function () {
        $.KittenTeach.Auth.registration = {
            form: $("#registration-form"),
            submitButton: $("#registration-btn"),
            role: 'students',  // TODO role

            init: function () {
                var that = this;
                this.form.on('click', function (e) {
                    var $target = $(e.target);

                    if ($target.is(that.submitButton) || $target.parents(that.submitButton.selector).length > 0) {
                        that.signUp();
                    }
                });
            },
            signUp: function () {
                $.ajax({
                    url: '/api/' + this.role + '/create',
                    type: 'post',
                    data: JSON.stringify({}),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    dataType: 'json',
                    success: function (data) {
                        // redirect
                        // set token to local storage
                    },
                    error: function (data) {
                        // validation errors
                    }
                });
            },
            validate: function () {

            }
        };

        $.KittenTeach.Auth.login = {
            form: $("#login-form"),
            submitButton: $("#login-btn"),

            init: function () {
                var that = this;
                this.form.on('click', function (e) {
                    var $target = $(e.target);

                    if ($target.is(that.submitButton) || $target.parents(that.submitButton.selector).length > 0) {
                        that.signIn();
                    }
                });
            },
            signIn: function () {
                $.ajax({
                    url: '/api/auth',
                    type: 'post',
                    data: JSON.stringify({
                        'email': this.form.find('input[name="email"]').val(),
                        'password': this.form.find('input[name="password"]').val()
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    dataType: 'json',
                    success: function (data) {
                        // redirect
                        // set token to local storage
                    },
                    error: function (data) {
                        // validation errors
                    }
                });
            },
            validate: function () {

            }
        };

        $.KittenTeach.Auth.registration.init();
        $.KittenTeach.Auth.login.init();
    }
};


