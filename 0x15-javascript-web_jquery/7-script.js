/* fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag DIV#character */
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (data) {
    $('div#character').text(data.name);
  },
  error: function () {
    window.alert('Error loading information from API');
  }
});
