function mobileMenuToggle() {
  var header_navigation = document.getElementById("header-navigation");
  if (header_navigation.style.display === "block") {
    header_navigation.style.display = "none";
    header_navigation.style.visibility = "hidden";

    document.getElementById("header-search").style.display = "none";
    document.getElementById("header-search").style.visibility = "hidden";

    document.getElementById("header").style.height = "1em";
  } else {
    header_navigation.style.display = "block";
    header_navigation.style.visibility = "visible";

    document.getElementById("header-search").style.display = "block";
    document.getElementById("header-search").style.visibility = "visible";

    // Transition animation does not work to/from unset/fit-content, must be
    // specific value.
    var navigation_lines = header_navigation.getElementsByClassName("navigation-element").length;
    document.getElementById("header").style.height = (1.1 * navigation_lines + 3.5) + "em";
  }
}
