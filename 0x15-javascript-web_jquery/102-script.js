/* Updates the text color of the HTML tag HEADER to red (#FF0000): */
/*  */
$(function () {
  $('input#btn_translate').click(() => {
    const language = $('input#language_code').val();
    const URL = `https://fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(URL, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
