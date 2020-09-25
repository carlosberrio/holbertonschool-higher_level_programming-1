/* Fetches and prints how to say "Hello" depending of the language */
$(function () {
  $('input#btn_translate').click(() => {
    const language = $('input#language_code').val();
    const URL = `https://fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(URL, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
