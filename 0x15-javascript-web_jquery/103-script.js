$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (ent) {
      if (ent.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const lan = $('INPUT#language_code').val();
  $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lan}`, function (data) {      $('DIV#hello').html(data.hello);
  });
}
