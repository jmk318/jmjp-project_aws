var company_name = document.getElementById('searching').innerHTML;
var filename = company_name + '_포괄손익계산서.csv';

newData = [];

$.ajax({
  url:" ../static/csv/" + filename,
  async:false,
  dataType: "text",
}).done(successFunction)

function successFunction(data) {

var allRows = data.split(/\r?\n|\r/);

var table = "<table>";
for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
  if (singleRow === 0) {
    table += "<thead>";
    table += "<tr>";
  } else {
    table += "<tr>";
  }
  var rowCells = allRows[singleRow].split(",");
  newData = newData.concat(rowCells);
  
  }
}


const moneyFormat = (value) => {
  flag = false
  if (value<0)
  { 
    value = -value
    flag = true;
  }
  const numbers = [
      numbering(value % 100000000000000000000, 10000000000000000),
      numbering(value % 10000000000000000, 1000000000000),
      numbering(value % 1000000000000, 100000000),
      numbering(value % 100000000, 10000),
      value % 10000
  ]
  
  if (flag){ 
    return '-'+ setUnitText(numbers).filter(number => !!number).join(' ');}

  else {
      return setUnitText(numbers).filter(number => !!number).join(' ');
      }

}

const setUnitText = (numbers) => {
  const unit = ['원', '만', '억', '조', '경'];
  return numbers.map((number, index) => !!number ? numberFormat(number) + unit[(unit.length - 1) - index] : number)
}

const numbering = (value, division) => {
  const result = Math.floor(value / division);
  return result === 0 ? null : (result % division);
}

const NUMBER_FORMAT_REGX = /\B(?=(\d{3})+(?!\d))/g;

const numberFormat = (value) => {
  return value.toString().replace(NUMBER_FORMAT_REGX, ',');
}



// Change HTML

for (var k =1; k< 9; k++){
    $('#ai > tbody > tr:nth-child('+k+') > td:nth-child(1)').text(newData[5*k])

    for (var i=2; i < 6; i++) {
    fined_value = newData[5*k+i-1];
    fined_vaule_str = moneyFormat(fined_value)
    $('#ai > tbody > tr:nth-child('+k+') > td:nth-child('+i+')').text(fined_vaule_str);
    }

}



for(var i=0; i < 4; i++){
  var dict = {};
  var term = ['수익성','성장성','건전성','기업규모'];

  $.ajax({
    url:" ../static/csv/" + term[i] + ".csv",
    async:false,
    dataType: "text",
  }).done(successFunction2)

  
  function successFunction2(data) {
    var allRows = data.split(/\r?\n|\r/);
    var table = "<table>";
    for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
      if (singleRow === 0) {
        table += "<thead>";
        table += "<tr>";
      } else {
        table += "<tr>";
      }

      
      var rowCells = allRows[singleRow].split(",");
      dict['\uFEFF'+ rowCells[1]] = '\uFEFF'+rowCells[2];   
      
    }
   
    };


    $('#'+term[i]).text(dict['\uFEFF'+ company_name])
    
  
  
  
    }

    //감정분석값 바꾸기
var x = document.getElementById('어제').innerHTML; 
var y = document.getElementById('지난주').innerHTML; 
var z =  document.getElementById('지난달').innerHTML; 

$('#어제').text(x);
$('#지난주').text(y);
$('#지난달').text(z);

//ai 코멘트바꾸기 

var comment = document.getElementById('comment').innerText

removing_list = ['<b>','</b>','기사선택과 인사이트 제시:','기사선택: ',' 선택된: 기사']
removing_list2 = ['1. ', '2. ', '3. ','Insight 제시:']
for (var i =0; i < 5 ;i++){

  comment=comment.replace(removing_list[i],'');
  
};

for (var i =0; i< 4 ;i++){
  
  comment=comment.replace(removing_list2[i],'\n' +' '+ removing_list2[i] )
  
};

console.log(comment)
document.getElementById("comment").innerText = comment
