$.KittenTeach.Home = {
    init: function() {
        console.log("home init");

        var $header = $('header');
        var $logo = $header.find('.header__logo-svg')

        var topStyleActivated = true;
        $header.addClass('header--main');
        $logo.addClass('header__logo-svg--dark')

        $(window).on('scroll', function (e) {
          if ($(this).scrollTop() <= 45) {
              if (!topStyleActivated) {
                  $header.addClass('header--main');
                  $logo.removeClass('header__logo-svg--white')
                  $logo.addClass('header__logo-svg--dark')
                  topStyleActivated = true;
              }
          } else {
              if (topStyleActivated) {
                  $header.removeClass('header--main');
                  $logo.removeClass('header__logo-svg--dark')
                  $logo.addClass('header__logo-svg--white')
                  topStyleActivated = false;
              }
          }
        })
    }
};