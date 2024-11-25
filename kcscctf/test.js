const http = require('http');

const url = 'http://recruit.osiris.bar:32003/flag.txt';

http.get(url, (response) => {
    let data = '';

    response.on('data', (chunk) => {
        data += chunk;
    });

    response.on('end', () => {
        console.log(data); // In nội dung của file
    });
}).on('error', (error) => {
    console.error(`Đã xảy ra lỗi: ${error}`);
});
