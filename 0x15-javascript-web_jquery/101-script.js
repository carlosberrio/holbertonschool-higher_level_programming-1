/* Updates the text color of the HTML tag HEADER to red (#FF0000): */

$(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li').last().remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
