/* crm_user/js/JavaScript.js */

// To style all selects
$(function () {
  $.fn.selectpicker.Constructor.BootstrapVersion = '5';
  $('select').removeClass('form-select');
  $('select').addClass('v-select');
  $('select').attr('data-style', 'v-select-btn');
  $('select').selectpicker();
});