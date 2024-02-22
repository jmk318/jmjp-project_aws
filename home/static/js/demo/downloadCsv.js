// const fs = require('fs')
// const AWS = require('aws-sdk')
// const s3 = new AWS.S3 ({
//     // region_name="ap-northeast-2",
//     accessKeyId:"",
//     secretAccessKey:""
// })
   



// const downloadfile = (fileName) => {
//     var filename = company_name + '_포괄손익계산서.csv';
//     const params = {

//         Bucket:'jmjp-bucket',        
//         Key: fileName, //버킷에서 다운받을 이름
//     };
// s3.getObject(params, function(err,data){

//     if(err) {
//         throw err;
//     }
//     console.log(data);
//     // var contents = data['Body'].read().decode('utf-8');
//     fs.writeFileSync(fileName,data.Body.toString()); 

// });


// };

// // 경로.../원하는파일저장이름
// downloadfile("../../csv/"+ filename)
