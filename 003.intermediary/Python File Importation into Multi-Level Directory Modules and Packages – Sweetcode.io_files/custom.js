jQuery( document ).ready( function( $ ) {
"use strict";

	/////////////////////////////////
	// Accordion 
	/////////////////////////////////		
	jQuery(".accordionButton").click(function(){jQuery(".accordionButton").removeClass("on");jQuery(".accordionContent").slideUp("normal");if(jQuery(this).next().is(":hidden")==true){jQuery(this).addClass("on");jQuery(this).next().slideDown("normal")}});jQuery(".accordionButton").mouseover(function(){jQuery(this).addClass("over")}).mouseout(function(){jQuery(this).removeClass("over")});jQuery(".accordionContent").hide(); 

    // Sticky Sidebar
    jQuery('.sidebar').stick_in_parent({parent: '.wrap', spacer: '.sidebar-wrapper'});

}); // jQuery(document).