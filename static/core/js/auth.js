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
                        that.validate();
                    }
                });
            },
            signUp: function () {
                var that = this;
                $.ajax({
                    url: '/api/' + this.role + '/create',
                    type: 'post',
                    data: JSON.stringify({}),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    dataType: 'json',
                    success: that.onSignUpSuccess,
                    error: that.onSignUpError
                });
            },
            validate: function () {
                this.onValidationSuccess();
            },

            onValidationSuccess: function () {
                this.signUp();
            },
            onValidationError: function () {
                // validation errors
            },

            onSignUpSuccess: function (data) {
                // redirect
                // set token to local storage
            },
            onSignUpError: function (data) {
                // sign up errors
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
                        that.validate();
                    }
                });
            },
            signIn: function () {
                var that = this;
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
                    success: that.onSignInSuccess,
                    error: that.onSignInError
                });
            },
            validate: function () {
                this.onValidationSuccess();
            },

            onValidationSuccess: function () {
                this.signIn();
            },
            onValidationError: function () {
                // validation errors
            },

            onSignInSuccess: function (data) {

            },
            onSignInError: function (data) {
                // sign in errors
            }
        };

        $.KittenTeach.Auth.registration.init();
        $.KittenTeach.Auth.login.init();
    }
};


