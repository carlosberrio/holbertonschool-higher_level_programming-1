/*  */
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (data) {
    $('div#hello').text(data.hello);
  },
  error: function () {
    window.alert('Error loading data from URL');
  }
});
