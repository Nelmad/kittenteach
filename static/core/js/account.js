$.KittenTeach.Account = {
  init: function () {
    console.log('account init')

    var $header = $('header')
    var $logo = $header.find('.header__logo-svg')

    var topStyleActivated = true
    $header.addClass('header--account')
    $logo.addClass('header__logo-svg--brown')

    $(window).on('scroll', function (e) {
      if ($(this).scrollTop() <= 45) {
        if (!topStyleActivated) {
          $header.addClass('header--account')
          $logo.removeClass('header__logo-svg--white')
          $logo.addClass('header__logo-svg--brown')
          topStyleActivated = true
        }
      } else {
        if (topStyleActivated) {
          $header.removeClass('header--account')
          $logo.removeClass('header__logo-svg--brown')
          $logo.addClass('header__logo-svg--white')
          topStyleActivated = false
        }
      }
    })
  }
}