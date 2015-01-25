/**
By SmoiZ
Custom rowreader and rowwriter with javascript to make the
table rows clickable.
**/

function clickableRowWriter(rowIndex, record, columns, cellWriter) {
  var tr = '';

  // grab the record's attribute for each column
  for (var i = 0, len = columns.length; i < len; i++) {
    tr += cellWriter(columns[i], record);
  }

  return '<tr class=' + record.class + ' data-href=' + record.hrefData + '>' + tr + '</tr>';
};

function clickableRowReader(rowIndex, rowElement, record) {
  record.hrefData = $(rowElement).data('href');
  record.class = $(rowElement).attr('class')
};

$( document ).ready(function() {
  $("table").on( "click", ".clickableRow", function() {
    window.open($(this).data("href"), "windowName", "height=500,width=400");
  });
});
