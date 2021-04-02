$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();



    
    $(".year").text((new Date).getFullYear());
  });

