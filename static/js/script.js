
/* MATERIALIZE JQUERY CODE FOR ACTIVATE ELEMENTS*/
$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();

    /* MODAL FUNCTION FOR DELETE CONFIRMATION*/
    $('.modal').modal();

    /* ADD CURRENT YEAR TO FOOTER CODE */
    $(".year").text((new Date).getFullYear());

    /* ZOOM IN ON IMAGE RECIPES , BUTTONS ON HOVER*/
    $(".image-card, .btn-submit, .btn-error ").hover(
        function() {
            $(this).animate({"zoom": 1.2 }, 300);
        },
        function() {
            $(this).animate({"zoom": 1 }, 300);
        });

    





    /* MATERIALIZE VALIDATION CODE TO ACTIVATE VALIDATION ON DROP DOWN MENU. 
        CODE TAKEN FROM CI TUTORIAL*/
        
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
  });

