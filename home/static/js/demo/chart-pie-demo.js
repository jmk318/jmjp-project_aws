// var newData=[];
// $.ajax({
//   url:" ../static/csv/kia.csv",
//   async:false,
//   dataType: "text",
// }).done(successFunction)


// function successFunction(data) {

// var allRows = data.split(/\r?\n|\r/);

// var table = "<table>";
// for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
//   if (singleRow === 0) {
//     table += "<thead>";
//     table += "<tr>";
//   } else {
//     table += "<tr>";
//   }
//   var rowCells = allRows[singleRow].split(",");
//   newData = newData.concat(rowCells);
  
// }


// }

// var positive =
// var negative = $('#negative')
var a = document.getElementById('positive').innerHTML
var b = document.getElementById('negative').innerHTML

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["긍정", "부정"],
    datasets: [{
      data: [a,b],
      backgroundColor: ['#4e73df', '#dc3545'],
      hoverBackgroundColor: ['#2e59d9', '#de0d20'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
