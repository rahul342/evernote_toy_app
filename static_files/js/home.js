function load_big_image(guid) {
	$.colorbox({photo:true, maxWidth:"95%",maxHeight:"95%", href:big_image_url+guid+token_req});
}

$('#load-more-button').click(load_more);

function no_more_images() {
	$("#load-more-block").hide();
	$("#no-more-data-block").show();
}

function load_more() {
	$("#load-more-button").addClass("disabled").attr("disabled", true).text("Loading..");
	$.ajax({
	  url: '/load_more/'+note_offset+'/'+resource_offset+'/',
	  statusCode: {
	    403: function() {
	      window.location="/login/";
	    }
	  },
	  success: function(data) {
		  if(data.length == 0) {
		  	no_more_images();
		  }
		  else {
		  	  note_offset = data.note_offset;
		  	  resource_offset = data.resource_offset;
		  	  $('#image-container').append(data.rows);
		  	  if(data.no_more_images) {
			  	 no_more_images();
			  }
			  else {
			  	$("#load-more-button").text("Load More").attr("disabled", false).removeClass("disabled");
			  }
		  }
	  }	
	});
}