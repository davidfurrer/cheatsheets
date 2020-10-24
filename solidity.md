# Solidity

online editor: https://remix.ethereum.org/

## Hello World with update function

```javascript
pragma solidity 0.5.12;

contract HelloWorld{
    string public message = "Hello World";

    function getMessage() public view returns(string memory){
        return message;
    }

    function setMessage(string memory newMessage) public{
        message = newMessage;
    }
}
```

## arrays

```javascript
pragma solidity 0.5.12;

contract arrays{
    uint[] public numbers = [1, 23, 25];

    function getNumber(uint index) public view returns(uint){
        return numbers[index];
    }

    function setNumber(uint index, uint newNumber) public{
        numbers[index] = newNumber;
    }
}
```

## structs

Same as class in python, object in javascript.

```javascript
pragma solidity 0.5.12;

contract structs{
    // struct definition
    struct Person{
        uint id;
        string name;
        int height;
    }


    Person[] public people;

    function createPerson(string memory name, int height) public{
        people.push(Person(people.length, name, height));
    }
}
```
