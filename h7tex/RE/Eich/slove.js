const fs = require('fs');

// Hàm A: Tạo khóa từ chuỗi D
function A(D, length) {     
    let key = '';     
    for (let i = 0; i < length; i++) {         
        key += D.charAt(i % D.length);     
    }     
    return key; 
}

// Hàm B: Mã hóa hoặc giải mã nội dung F bằng khóa D
function B(F, D) {     
    let key = A(D, F.length);     
    let G = '';      
    for (let i = 0; i < F.length; i++) {         
        let charCode = F.charCodeAt(i);         
        let keyCode = key.charCodeAt(i);         
        let GChar = String.fromCharCode(charCode ^ keyCode);         
        G += GChar;     
    }      
    return G; 
}

// Đọc nội dung từ tệp C.txt
let C = fs.readFileSync('C.txt', 'utf8'); 
let D = "6aef677b2c8b645384e713aece4322b045a79f48";  

// Mã hóa nội dung
let E = B(C, D); 
console.log("Reward: ", E);