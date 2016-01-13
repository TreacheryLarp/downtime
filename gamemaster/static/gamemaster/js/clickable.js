/**
By SmoiZ
Custom rowreader and rowwriter with javascript to make the
table rows clickable.
**/
$( document ).ready(function() {
  $("table").on( "click", ".clickableRow", function() {
    window.open($(this).data("href"), "editor", "width=400,height=700");
  });
});
