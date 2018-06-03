$.KittenTeach.Account = {
  init: function () {
    console.log('account init')

    var $header = $('header')
    var $footer = $('footer')
    var $logo = $header.find('.header__logo-svg')

    var topStyleActivated = true
    $header.addClass('header--account')
    $logo.addClass('header__logo-svg--brown')
    $footer.addClass('footer--account')

    $(window).on('scroll', function (e) {
      if ($(this).scrollTop() <= 45) {
        if (!topStyleActivated) {
          $header.addClass('header--account')
          $header.removeClass('header--account-secondary')

          topStyleActivated = true
        }
      } else {
        if (topStyleActivated) {
          $header.removeClass('header--account')
          $header.addClass('header--account-secondary')

          topStyleActivated = false
        }
      }
    })
  }
}