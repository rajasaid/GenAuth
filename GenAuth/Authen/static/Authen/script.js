$(document).ready(function () {
  var tabWrapper = $(".tab__content");
    var activeTab = tabWrapper.find(".active");
    var activeTabHeight = activeTab.outerHeight();

    // Show tab on page load
    activeTab.show();

    // Set height of wrapper on page load
    tabWrapper.height(activeTabHeight);
  $(".register-tab").click(function () {
    $(".register-box").show();
    $(".login-box").hide();
    $(".register-tab").addClass("active");
    $(".login-tab").removeClass("active");
  });
  $(".login-tab").click(function () {
    $(".login-box").show();
    $(".register-box").hide();
    $(".login-tab").addClass("active");
    $(".register-tab").removeClass("active");
  });
});
