$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-mahasiswa .modal-content").html("");
        $("#modal-mahasiswa").modal("show");
      },
      success: function (data) {
        $("#modal-mahasiswa .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#mahasiswa-table tbody").html(data.html_mahasiswa_list);
          $("#modal-mahasiswa").modal("hide");
        }
        else {
          $("#modal-mahasiswa .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Add Mahasiswa
  $(".js-create-mahasiswa").click(loadForm);
  $("#modal-mahasiswa").on("submit", ".js-mahasiswa-create-form", saveForm);

  // Update mahasiswa
  $("#mahasiswa-table").on("click", ".js-update-mahasiswa", loadForm);
  $("#modal-mahasiswa").on("submit", ".js-mahasiswa-update-form", saveForm);

  // Delete mahasiswa
  $("#mahasiswa-table").on("click", ".js-delete-mahasiswa", loadForm);
  $("#modal-mahasiswa").on("submit", ".js-mahasiswa-delete-form", saveForm);

});
