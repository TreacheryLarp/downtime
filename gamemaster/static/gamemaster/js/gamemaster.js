/**
By SmoiZ
**/

$( document ).ready(function() {

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

  $('#my-table').dynatable({
    writers: {
      _rowWriter: myRowWriter
    },
    readers: {
      _rowReader: myRowReader
    }
  });

  // Clickable rows
  $(".clickableRow").click(function() {
    window.document.location = $(this).attr("href");
  });
});
