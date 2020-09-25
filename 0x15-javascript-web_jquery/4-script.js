/* Updates the class of the HTML tag HEADER to #FF0000 when
the user clicks on the tag DIV#red_header: */
$('div#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
