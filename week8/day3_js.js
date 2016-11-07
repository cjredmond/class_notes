console.log('hey how you doin');
var myNumber = 10;
console.log(myNumber);
var myArray = [10, 'connor', [2, 3], 'zoe'];
console.log(myArray);



for(var i = 0; i < myArray.length; i++) {
  var item = myArray[i];
  console.log(item)
};

var myObject = {
  myName: "connor",
  myAge: "24"
};

console.log(myObject['myAge']);

var myFunc = function(x, y) {
  return x * y;
};

console.log(myFunc(9, 4));

var newArray = [15,5,6,711,515,21];

var loopFunc = function(item) {
  console.log(item);
};

newArray.forEach(loopFunc);

newArray.forEach(function(item) {
  console.log(item);
})
