
var source_jsons = $("#jsons-template").html();
var template_jsons = Handlebars.compile(source_jsons);

$('#jsons').html(template_jsons(context));