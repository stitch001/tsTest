"use strict";
let a = 10;
console.log(a + 30);
class A {
    constructor() {
        this.name = "Abc";
        this.gender = "Bcd";
        this.age = 0;
    }
    get Name() {
        return this.name + "老六";
    }
}
function btnclick() {
    fetch("/data.json").then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        let datap = document.querySelector("#datap");
        if (datap != null) {
            datap.innerHTML = data.oses;
        }
    }).catch(err => {
        console.error(err);
    });
}
function bodyLoad() {
    let b = new A();
    console.log(b.Name);
    let p1 = document.getElementById("p2");
    if (p1 != null) {
        p1.innerHTML = b.gender + "6666性别，自认为的，可能很多，进化到中国魏晋阶段";
    }
    let bt1 = document.querySelector("#bt1");
    if (bt1 != null && bt1 instanceof HTMLElement) {
        bt1.onclick = btnclick;
    }
}
//# sourceMappingURL=index.js.map