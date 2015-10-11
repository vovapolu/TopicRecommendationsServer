Handlebars.registerHelper('first_word', function(text) {
  return text.split(' ')[0];
});

Handlebars.registerHelper('format_date', function(date) {
  return moment(date).format("Do MMM YY")
});

var source_tabs = $("#topics-tabs-template").html();
var template_tabs = Handlebars.compile(source_tabs);

var source_content = $('#topics-content-template').html()
var template_content = Handlebars.compile(source_content)

var target = document.getElementById("topics-tabs")

var opts = {
  lines: 9, // The number of lines to draw
  length: 20, // The length of each line
  width: 10, // The line thickness
  radius: 30, // The radius of the inner circle
  color: '#3b5998', // #rgb or #rrggbb or array of colors
  speed: 0.5, // Rounds per second
  trail: 40, // Afterglow percentage
  className: 'spinner', // The CSS class to assign to the spinner
};

function generate_feed() {
    var spinner = new Spinner(opts).spin(target);
    $.getJSON(json_path, function(data) {
    	spinner.stop();		            
		$("#topics-tabs").html(template_tabs(data));
		$('#topics-content').html(template_content(data));
	});		    		    		  
}

generate_feed()
