/*  */
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (data) {
    $.each(data.results, function (index, film) {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    });
  },
  error: function () {
    window.alert('Error loading information from API');
  }
});
