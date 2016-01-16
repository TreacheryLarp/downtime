/**
By SmoiZ
Custom rowreader and rowwriter with javascript to make the
table rows clickable.
**/
$( document ).ready(function() {
  $("table").on( "click", ".clickableRow", function() {
    window.open($(this).data("href"), "_blank", "width=400,height=700,toolbar=0,status=0,scrollbars=1,resizable=0,menubar=0,resizable=1");
  });
});
