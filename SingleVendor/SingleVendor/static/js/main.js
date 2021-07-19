$(document).on("click", ".room", function () {
  $.ajax({
    url: "register",
    dataType: "json",
    data: {},
    success: function (data) {
      console.log(data);
      $("#mmm .modal-content").html(data.html_form);
    },
  });
});

$(document).on("click", ".log", function () {
  console.log("amallogin");

  $.ajax({
    url: "login",
    dataType: "json",
    data: {},
    success: function (data) {
      console.log(data);
      $("#login .modal-content").html(data.html_form);
    },
  });
});

$(document).on("click", ".logi", function () {
  $("#logform").submit(function (e) {
    e.preventDefault();
    console.log("response");

    var serializedData = $(this).serialize();
    console.log("serializedData:", serializedData);
    $.ajax({
      url: "login",
      type: "POST",
      data: serializedData,

      dataType: "json",
      success: function (data) {
        window.location.replace("http://127.0.0.1:8000/registered");
      },
    });
  });
});

$(document).on("change", ".brnch", function () {
  var values = $("#agileinfo-nav_search :selected").val();
  console.log("changed:", values);

  $.ajax({
    url: "selectbranch",
    dataType: "json",
    data: {
      values: values,
    },
    success: function (data) {
      console.log("data");
    },
  });
});

$(document).on("click", ".reg", function () {
  $("#fdata").submit(function (e) {
    e.preventDefault();

    console.log("response");
    profile = document.getElementById("id_profile").files;
    console.log("profile:", profile);

    var serializedData = $(this).serialize();
    console.log("serializedData:", serializedData);
    $.ajax({
      url: "register",
      type: "POST",
      data: serializedData,

      // dataType: "json",
      success: function (data) {
        console.log(data);
        $("#mmm .modal-content").html(data.html_form);
      },
    });
  });
});
