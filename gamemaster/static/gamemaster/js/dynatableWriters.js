function clickableRowWriter(rowIndex, record, columns, cellWriter) {
  var tr = '';

  // grab the record's attribute for each column
  for (var i = 0, len = columns.length; i < len; i++) {
    tr += cellWriter(columns[i], record);
  }

  return '<tr class="' + record.class + '" data-href="' + record.hrefData + '">' + tr + '</tr>';
};

function clickableRowReader(rowIndex, rowElement, record) {
  record.hrefData = $(rowElement).data('href');
  record.class = $(rowElement).attr('class');
};
