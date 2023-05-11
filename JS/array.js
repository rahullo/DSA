class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index]
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
        const last = this.data[this.length - 1]
        delete this.data[this.length - 1]
        this.length--
            return last;
    }

    remove(index) {
        const item = this.data[index];
        this.shiftItem(index);
        this.length--;
        return item;
    }

    shiftItem(index) {
        for (let i = index; i < this.length - 1; i++) {
            this.data[i] = this.data[i + 1]
        }
        this.pop(this.length)
    }

}


const newArray = new MyArray()
newArray.push(2)
newArray.push(4)
newArray.push(5)
newArray.push(6)
console.log(newArray);
// console.log(newArray.pop());
console.log(newArray.remove(0));
console.log(newArray);
// console.log(newArray.get(1))