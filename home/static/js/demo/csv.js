const fs = require('fs')
const path = require('path')
const filename = "pr.csv"


const csvPath = path.join(__dirname, '.', filename) // 두번째 인
const csv = fs.readFileSync(csvPath, "utf-8")
    
var allRows = csv.split(/\n|\r/)

rowData = []

for(var singleRow = 0; singleRow < allRows.length; singleRow++) {
   var rowCells = allRows[singleRow].split(',')
     
    if(singleRow === 0) {
           
    }
    
    rowData.push(rowCells)
    
}
console.log(rowCells)
module.exports.rowData = rowData